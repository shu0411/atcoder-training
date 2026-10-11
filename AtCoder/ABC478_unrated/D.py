import io
import sys

_INPUT = """\
30 20
3 22 11
8 30 10
12 14 7
2 17 4
1 19 12
7 30 15
11 23 2
14 25 17
9 12 7
10 16 7
16 18 19
1 11 14
11 15 4
1 21 6
4 8 10
23 24 11
8 27 10
1 19 12
23 23 16
13 24 12

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())

dict_X_list_LR = {}
# 処理
for _ in range(Q):
    L, R, X = map(int, input().split())
    if X not in dict_X_list_LR:
        dict_X_list_LR[X] = []
    dict_X_list_LR[X].append((L, R))

list_imos = [0] * (N + 1)
for list_LR in dict_X_list_LR.values():
    list_LR.sort()
    now_R = -1
    for L, R in list_LR:
        if now_R < L:
            list_imos[L - 1] += 1
            if now_R != -1:
                list_imos[now_R] -= 1
            now_R = R
        elif L <= now_R and now_R <= R:
            now_R = R
    else:
        list_imos[now_R] -= 1

now_cnt = 0
list_out = []
for now_imos in list_imos:
    now_cnt += now_imos
    list_out.append(now_cnt)

# 出力
print(*list_out[:-1])
