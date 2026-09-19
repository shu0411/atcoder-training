import io
import sys

_INPUT = """\
6 7
3 6 5 2 4 1
4 5
2 3
3 5
4 6
3 4
1 6
3 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_P = list(map(int, input().split()))


# 処理
dict_P_idx = {i: -1 for i in range(1, N + 1)}
for i, P in enumerate(list_P):
    dict_P_idx[P] = i

for i in range(M):
    L, R = map(int, input().split())

    for tmp_min_P in range(1, N + i):
        idx = dict_P_idx[tmp_min_P]
        if idx >= L - 1 and idx <= R - 1:
            min_P = tmp_min_P
            min_idx = idx
            break

    for tmp_max_P in range(N, 0, -1):
        idx = dict_P_idx[tmp_max_P]
        if idx >= L - 1 and idx <= R - 1:
            max_P = tmp_max_P
            max_idx = idx
            break

    dict_P_idx[min_P] = max_idx
    dict_P_idx[max_P] = min_idx

list_out = [-1] * N
for P, idx in dict_P_idx.items():
    list_out[idx] = P

# 出力
print(*list_out)
