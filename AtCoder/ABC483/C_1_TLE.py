import io
import sys

_INPUT = """\
5 6
1 3
1 3
2 1
2 1
3 4
4 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

# 処理
dict_A = {}
dict_A_B = {}
for _ in range(M):
    A, B = map(int, input().split())
    if A not in dict_A:
        dict_A[A] = 0
        dict_A_B[A] = {}
    dict_A[A] += 1
    if B not in dict_A_B[A]:
        dict_A_B[A][B] = 0
    dict_A_B[A][B] += 1

for i in range(1, N + 1):
    dict_final = dict_A.copy()
    dict_final[i] = 0

    # 辞退者の振り替え
    if i in dict_A_B:
        for B, cnt in dict_A_B[i].items():
            if B not in dict_final:
                dict_final[B] = 0
            dict_final[B] += cnt

    out = 0
    max_cnt = 0
    for target, cnt in dict_final.items():
        if max_cnt < cnt:
            out = target
            max_cnt = cnt

    # 出力
    print(out)
