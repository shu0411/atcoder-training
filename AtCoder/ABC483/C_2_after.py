import io
import sys

_INPUT = """\
5 13
1 3
1 3
1 3
2 1
2 1
2 1
3 1
3 2
3 4
3 5
4 1
4 1
4 3

"""
sys.stdin = io.StringIO(_INPUT)

# 全部足すのではなく、2番目に投票した人がいた候補者だけ足す
# →全部で投票者がN人なので、最悪でもN回（←この計算をM**2にしてしまったのが失敗原因）
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

max_1_id = -1
max_1_cnt = -1
max_2_id = -1
max_2_cnt = -1
list_A_score = sorted(list(dict_A.items()))
for A, cnt in list_A_score:
    if cnt > max_1_cnt:
        max_1_id, max_2_id = A, max_1_id
        max_1_cnt, max_2_cnt = cnt, max_1_cnt
    elif cnt == max_1_cnt and cnt > max_2_cnt:
        max_2_id = A
        max_2_cnt = cnt

for i in range(1, N + 1):
    dict_final = {}

    # 辞退者の振り替え
    if i in dict_A_B:
        for B, cnt in dict_A_B[i].items():
            if B not in dict_final:
                dict_final[B] = dict_A[B] if B in dict_A else 0
            dict_final[B] += cnt

    out = 0
    max_cnt = 0

    # 振り替え前のmax
    if i != max_1_id:
        out = max_1_id
        max_cnt = max_1_cnt
    else:
        out = max_2_id
        max_cnt = max_2_cnt

    for target, cnt in sorted(list(dict_final.items())):
        if max_cnt < cnt or max_cnt == cnt and target < out:
            out = target
            max_cnt = cnt

    # 出力
    print(out)
