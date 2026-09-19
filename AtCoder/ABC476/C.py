import io
import sys

_INPUT = """\
10
11 9 1 3 17 19 10 19 17 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
list_best_3 = sorted(list_A[:3], reverse=True)
print(list_best_3[-1])
for k in range(3, N):
    tmp_list_best_3 = list_best_3.copy()
    tmp_list_best_3.append(list_A[k])
    tmp_list_best_3.sort(reverse=True)
    list_best_3 = tmp_list_best_3[:3].copy()

    # 出力
    print(list_best_3[-1])
