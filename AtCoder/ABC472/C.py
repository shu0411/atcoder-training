import io
import sys

_INPUT = """\
10 3 1368290936
216519459 804733999 297250023 775422599 287963235 999315644 354987425 974810607 653940822 117157941

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N,M,K = map(int,input().split())
list_A = list(map(int,input().split()))

# 処理
cumulative_sum_list_A = [0] * (N * 2)

out = ""
for i,A in enumerate(list_A):
    idx_sum = i + N
    if cumulative_sum_list_A[idx_sum - 1] - cumulative_sum_list_A[idx_sum - M] + A <= K:
        out = "Yes"
        cumulative_sum_list_A[idx_sum] = cumulative_sum_list_A[idx_sum - 1] + A
    else:
        out = "No"
        cumulative_sum_list_A[idx_sum] = cumulative_sum_list_A[idx_sum - 1]

    # 出力
    print(out)
