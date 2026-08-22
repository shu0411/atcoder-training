import io
import sys

_INPUT = """\
4
5 2 3 8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_L = list(map(int,input().split()))

# 処理
sum_L = sum(list_L)

tmp_sum_L = 0
for L in list_L:
    before_tmp_sum_L = tmp_sum_L
    tmp_sum_L += L
    if tmp_sum_L >= sum_L / 2:
        if tmp_sum_L - sum_L/2 >=  sum_L/2 - before_tmp_sum_L:
            out = (sum_L - before_tmp_sum_L) - before_tmp_sum_L
        else:
            out = tmp_sum_L - (sum_L - tmp_sum_L)

        break

# 出力
print(out)
