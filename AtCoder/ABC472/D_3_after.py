import io
import sys

_INPUT = """\
5 7 2
..#....
..#....
.......
...#...
...#...

"""
sys.stdin = io.StringIO(_INPUT)

# 本番中、安全な地点を見つけ、そこにK回以下でたどり着ける点を探ればいいことはわかった。
# BFSを使うという発想にたどり着けなかった
#############ここから下をコピペ#############
from collections import deque

# 入力
H, W, K = map(int, input().split())
table_S = [input() for _ in range(H)]

# 処理
list_bomb_exists_x = [False] * W
list_bomb_exists_y = [False] * H
for y, row_S in enumerate(table_S):
    for x, S in enumerate(list(row_S)):
        if S == "#":
            list_bomb_exists_x[x] = True
            list_bomb_exists_y[y] = True

list_safety_point = []
for y in range(H):
    for x in range(W):
        if not list_bomb_exists_x[x] and not list_bomb_exists_y[y]:
            list_safety_point.append((x, y))

out = 0
q = deque()
if len(list_safety_point) > 0:
    for safety_point in list_safety_point:
        q.append((safety_point[0], safety_point[1], 0))

    visited = [[False] * W for _ in range(H)]
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y, move_times = q.popleft()
        if (
            0 <= x
            and x < W
            and 0 <= y
            and y < H
            and not visited[y][x]
            and table_S[y][x] == "."
            and move_times <= K
        ):
            visited[y][x] = True
            out += 1

            for move_x, move_y in move:
                after_move_x = x + move_x
                after_move_y = y + move_y
                q.append((after_move_x, after_move_y, move_times + 1))

# 出力
print(out)
