# AC
# 色順に各スライムを1匹ずつ、最短経路で1マスずつ巣へ運ぶ。
from collections import deque
import sys

DIRECTIONS = ((-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R"))
MAX_OPERATIONS = 100_000


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
    """各スライムを色順に、最短経路で1マスずつ巣へ運ぶ。"""
    slime_positions, nest_positions = find_slimes_and_nests(board, color_count)
    stacks = [[[] for _ in board] for _ in board]
    nest_colors = [[None for _ in board] for _ in board]

    for color, positions in enumerate(slime_positions):
        for row, column in positions:
            stacks[row][column].append(color)
    for color, position in enumerate(nest_positions):
        row, column = position
        nest_colors[row][column] = color

    operations = []
    for color in range(color_count):
        distances = distances_from(board, nest_positions[color])
        for row, column in slime_positions[color]:
            while distances[row][column] > 0:
                for delta_row, delta_column, direction in DIRECTIONS:
                    next_row = row + delta_row
                    next_column = column + delta_column
                    if not (
                        0 <= next_row < len(board) and 0 <= next_column < len(board)
                    ):
                        continue
                    if distances[next_row][next_column] == distances[row][column] - 1:
                        break

                height = len(stacks[row][column])
                if stacks[row][column][-1] != color:
                    raise RuntimeError("移動対象のスライムが塔の最上部にありません")
                operations.append((row, column, height - 1, direction, 1))
                if len(operations) > MAX_OPERATIONS:
                    raise RuntimeError("操作回数が100000回を超えました")

                moving_slime = stacks[row][column].pop()
                stacks[next_row][next_column].append(moving_slime)
                _send_home(stacks, nest_colors, row, column)
                _send_home(stacks, nest_colors, next_row, next_column)
                row, column = next_row, next_column
    return operations


def _send_home(stacks, nest_colors, row: int, column: int):
    nest_color = nest_colors[row][column]
    if nest_color is None:
        return
    while stacks[row][column] and stacks[row][column][-1] == nest_color:
        stacks[row][column].pop()


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
