import io
import sys

_INPUT = """\
5 3
1 3 4 2 5
5 2 4 3 7
2 5
5 6
1 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import heapq

# 入力
N, Q = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 処理
dict_u = {i: [] for i in range(1, N + 2)}
for i, A in enumerate(list_A):
    dict_u[i + 1].append((((i + 1) % N + 1), A))
    dict_u[(i + 1) % N + 1].append((i + 1, A))
for i, B in enumerate(list_B):
    dict_u[i + 1].append((N + 1, B))
    dict_u[N + 1].append((i + 1, B))

# N+1からN+1以外への最短
list_cost_node_from_n1 = [float("inf")] * (N + 2)
list_visited = [False] * (N + 2)

heap_node = []
heapq.heappush(heap_node, [0, N + 1])
while len(heap_node) > 0:
    now_cost, now_point = heapq.heappop(heap_node)
    if list_visited[now_point]:
        continue

    list_visited[now_point] = True
    list_cost_node_from_n1[now_point] = now_cost

    for next_point, next_cost in dict_u[now_point]:
        if list_visited[next_point]:
            continue

        heapq.heappush(heap_node, (now_cost + next_cost, next_point))

list_cost_turn_right = [float("inf")] * (N * 2 + 1)
list_cost_turn_right[1] = 0
for i in range(1, N * 2):
    list_cost_turn_right[i + 1] = list_cost_turn_right[i] + list_B[i]
list_cost_turn_left = [float("inf")] * (N * 2 + 1)

for _ in range(Q):

    # 出力
    # print(out)
    pass
