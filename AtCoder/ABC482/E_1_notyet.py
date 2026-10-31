import io
import sys

_INPUT = """\
5
1 2
2 3
2 4
4 5
2 1 3 1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
from collections import deque

# 入力
N = int(input())

dict_uv = {i: [] for i in range(1, N + 1)}
for _ in range(N):
    u, v = map(int, input().split())
    dict_uv[u].append(v)
    dict_uv[v].append(u)

list_C = [0] + list(map(int, input().split()))

# 処理
# 片方の端点の1つ
dist_from_first = [-1] * (N + 1)

queue_node = deque([(1, 0)])

while queue_node:
    node, dist = queue_node.pop()

    if dist_from_first[node] != -1:
        continue

    dist_from_first[node] = dist

    next_dist = dist + 1
    for next_node in dict_uv[node]:
        if dist_from_first[next_node] == -1:
            queue_node.append((next_node, next_dist))
