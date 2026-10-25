import io
import sys

_INPUT = """\
2 1 1 2
2 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import heapq

# 入力
N, M, S, T = map(int, input().split())

list_AB = [tuple(map(int, input().split())) for _ in range(M)]
list_AB.sort()

# 処理
dict_edge = {n: [] for n in range(1, N + 1)}
before_A = -1
for A, B in list_AB:
    cost = 1 if A == before_A else 0
    dict_edge[A].append((cost, B))
    before_A = A

dict_visited_cost = {n: -1 for n in range(1, N + 1)}

queue_cost_node = [(0, S)]
heapq.heapify(queue_cost_node)

while len(queue_cost_node) >= 1 and dict_visited_cost[T] == -1:
    now_cost, now_node = heapq.heappop(queue_cost_node)
    if dict_visited_cost[now_node] == -1:
        dict_visited_cost[now_node] = now_cost
        for add_cost, new_node in dict_edge[now_node]:
            if dict_visited_cost[new_node] == -1:
                heapq.heappush(
                    queue_cost_node, (dict_visited_cost[now_node] + add_cost, new_node)
                )

# 出力
print(dict_visited_cost[T])
