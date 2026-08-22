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

#############ここから下をコピペ#############
from collections import deque

# 入力
H,W,K = map(int,input().split())
table_S = [input() for _ in range(H)]

# 処理
list_bomb_exists_x = [False] * W
list_bomb_exists_y = [False] * H
for y,row_S in enumerate(table_S):
    for x,S in enumerate(list(row_S)):
        if S == "#":
            list_bomb_exists_x[x] = True
            list_bomb_exists_y[y] = True

list_safety_point = []
for y in range(H):
    for x in range(W):
        if not list_bomb_exists_x[x] and not list_bomb_exists_y[y]:
            list_safety_point.append((x,y))


out = 0
q = deque()
if len(list_safety_point) > 0:
    for safety_point in list_safety_point:
        pass

# 出力
print(out)
