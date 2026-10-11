# 合流後の塔を1個体として扱い、現在の塔から最遠のものを選び直す。
from collections import deque
import sys

DIRECTIONS = ((-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R"))
MAX_OPERATIONS = 100_000
MAX_HEIGHT = 8


def find_slimes_and_nests(board: list[str], color_count: int):
    """色ごとのスライムの初期位置と巣の位置を返す。"""
    slime_positions = [[] for _ in range(color_count)]
    nest_positions = [None] * color_count
    for row, line in enumerate(board):
        for column, cell in enumerate(line):
            if "a" <= cell <= "l":
                slime_positions[ord(cell) - ord("a")].append((row, column))
            elif "A" <= cell <= "L":
                nest_positions[ord(cell) - ord("A")] = (row, column)
    return slime_positions, nest_positions


def distances_from(board: list[str], start: tuple[int, int]):
    """start から各床マスまでの最短距離をBFSで求める。"""
    board_size = len(board)
    distances = [[-1] * board_size for _ in range(board_size)]
    start_row, start_column = start
    distances[start_row][start_column] = 0
    queue = deque([start])
    while queue:
        row, column = queue.popleft()
        for delta_row, delta_column, _ in DIRECTIONS:
            next_row = row + delta_row
            next_column = column + delta_column
            if not (0 <= next_row < board_size and 0 <= next_column < board_size):
                continue
            if board[next_row][next_column] == "#":
                continue
            if distances[next_row][next_column] != -1:
                continue
            distances[next_row][next_column] = distances[row][column] + 1
            queue.append((next_row, next_column))
    return distances


def make_operations(board: list[str], color_count: int):
    """合流後は最遠の同色スライムを呼び寄せる向きも比較する。"""
    slime_positions, nest_positions = find_slimes_and_nests(board, color_count)
    stacks = [[[] for _ in board] for _ in board]
    nest_colors = [[None for _ in board] for _ in board]
    slime_records = [[] for _ in range(color_count)]
    slime_positions_by_id = {}

    slime_id = 0
    for color, positions in enumerate(slime_positions):
        for row, column in positions:
            stacks[row][column].append((color, slime_id))
            slime_records[color].append((row, column, slime_id))
            slime_positions_by_id[slime_id] = (row, column)
            slime_id += 1
    for color, position in enumerate(nest_positions):
        row, column = position
        nest_colors[row][column] = color

    distances_by_color = [
        distances_from(board, nest_positions[color]) for color in range(color_count)
    ]
    distance_maps = {}
    operations = []

    def distance_map_to(position):
        if position not in distance_maps:
            distance_maps[position] = distances_from(board, position)
        return distance_maps[position]

    def move_once(row: int, column: int, color: int, distances):
        height = len(stacks[row][column])
        if not stacks[row][column] or stacks[row][column][-1][0] != color:
            raise RuntimeError("移動対象のスライムが塔の最上部にありません")

        moving_count = _top_same_color_count(stacks[row][column], color)
        leave_count = height - moving_count
        delta_row, delta_column, direction = _next_direction(
            board, distances, row, column
        )
        jump_distance = _straight_jump_distance(
            board,
            distances,
            row,
            column,
            delta_row,
            delta_column,
            leave_count + 1,
        )
        next_row = row + delta_row * jump_distance
        next_column = column + delta_column * jump_distance

        while len(stacks[next_row][next_column]) + moving_count > MAX_HEIGHT:
            blocking_color, blocking_id = stacks[next_row][next_column][-1]
            while slime_positions_by_id[blocking_id] is not None:
                blocking_row, blocking_column = slime_positions_by_id[blocking_id]
                move_once(
                    blocking_row,
                    blocking_column,
                    blocking_color,
                    distances_by_color[blocking_color],
                )

        operations.append((row, column, leave_count, direction, jump_distance))
        if len(operations) > MAX_OPERATIONS:
            raise RuntimeError("操作回数が100000回を超えました")

        moving_slimes = stacks[row][column][leave_count:]
        del stacks[row][column][leave_count:]
        stacks[next_row][next_column].extend(reversed(moving_slimes))
        for _, moving_slime_id in moving_slimes:
            slime_positions_by_id[moving_slime_id] = (next_row, next_column)
        _send_home(stacks, nest_colors, slime_positions_by_id, row, column)
        _send_home(stacks, nest_colors, slime_positions_by_id, next_row, next_column)

    def best_friend_route(row: int, column: int, color: int):
        current_stack = stacks[row][column]
        moving_count = _top_same_color_count(current_stack, color)
        if moving_count >= MAX_HEIGHT:
            return None, None

        distance_to_nest = distances_by_color[color][row][column]
        best_saving = 0
        best_friend_id = None
        best_distances = None
        for _, _, friend_id in slime_records[color]:
            friend_position = slime_positions_by_id[friend_id]
            if friend_position is None or friend_position == (row, column):
                continue

            friend_row, friend_column = friend_position
            if len(stacks[friend_row][friend_column]) + moving_count > MAX_HEIGHT:
                continue
            distances = distance_map_to(friend_position)
            distance_to_friend = distances[row][column]
            saving = distance_to_nest - distance_to_friend
            if saving > best_saving:
                best_saving = saving
                best_friend_id = friend_id
                best_distances = distances
        return best_friend_id, best_distances

    def farthest_tower_position(color: int):
        positions = set()
        for _, _, friend_id in slime_records[color]:
            friend_position = slime_positions_by_id[friend_id]
            if friend_position is not None:
                positions.add(friend_position)
        candidates = [
            position
            for position in positions
            if stacks[position[0]][position[1]]
            and stacks[position[0]][position[1]][-1][0] == color
        ]
        if not candidates:
            return None
        return max(
            candidates,
            key=lambda position: distances_by_color[color][position[0]][position[1]],
        )

    for color in range(color_count):
        while True:
            position = farthest_tower_position(color)
            if position is None:
                break
            row, column = position
            target_slime_id = stacks[row][column][-1][1]
            friend_id, distances = best_friend_route(row, column, color)
            if friend_id is None:
                move_once(row, column, color, distances_by_color[color])
                continue

            while (
                slime_positions_by_id[target_slime_id] is not None
                and slime_positions_by_id[friend_id] is not None
                and slime_positions_by_id[target_slime_id]
                != slime_positions_by_id[friend_id]
            ):
                row, column = slime_positions_by_id[target_slime_id]
                move_once(row, column, color, distances)
    return operations


def _top_same_color_count(stack, color: int):
    count = 0
    for slime_color, _ in reversed(stack):
        if slime_color != color:
            break
        count += 1
    return count


def _next_direction(board, distances, row: int, column: int):
    for delta_row, delta_column, direction in DIRECTIONS:
        next_row = row + delta_row
        next_column = column + delta_column
        if not (0 <= next_row < len(board) and 0 <= next_column < len(board)):
            continue
        if distances[next_row][next_column] == distances[row][column] - 1:
            return delta_row, delta_column, direction
    raise RuntimeError("巣までの最短経路が見つかりません")


def _straight_jump_distance(
    board,
    distances,
    row: int,
    column: int,
    delta_row: int,
    delta_column: int,
    max_distance: int,
):
    """同じ方向へ最短距離が減り続ける範囲をまとめる。"""
    jump_distance = 1
    while jump_distance < max_distance:
        next_row = row + delta_row * (jump_distance + 1)
        next_column = column + delta_column * (jump_distance + 1)
        if not (0 <= next_row < len(board) and 0 <= next_column < len(board)):
            break
        if board[next_row][next_column] == "#":
            break
        if distances[next_row][next_column] != distances[row][column] - (
            jump_distance + 1
        ):
            break
        jump_distance += 1
    return jump_distance


def _send_home(stacks, nest_colors, slime_positions_by_id, row: int, column: int):
    nest_color = nest_colors[row][column]
    if nest_color is None:
        return
    while stacks[row][column] and stacks[row][column][-1][0] == nest_color:
        _, slime_id = stacks[row][column].pop()
        slime_positions_by_id[slime_id] = None


def solve(input_stream, output_stream):
    N, K = map(int, input_stream.readline().split())
    table_C = [input_stream.readline().strip() for _ in range(N)]
    operations = make_operations(table_C, K)
    output_stream.write(
        "".join(
            f"{row} {column} {leave_count} {direction} {distance}\n"
            for row, column, leave_count, direction, distance in operations
        )
    )


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
