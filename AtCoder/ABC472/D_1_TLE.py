import io
import sys

_INPUT = """\
3 3 1
#..
..#
..#

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
from scipy.spatial import KDTree

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
if len(list_safety_point) > 0:
    tree = KDTree(list_safety_point)

    for y in range(H):
        for x in range(W):
            if table_S[y][x] == "#":
                continue

            d, idx = tree.query([x,y], k=1)
            nearest_safety_point = list_safety_point[idx]
            manhattan_dist = abs(nearest_safety_point[0] - x) + abs(nearest_safety_point[1] - y)
            if manhattan_dist <= K:
                out += 1

# 出力
print(out)
