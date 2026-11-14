import io
import sys

_INPUT = """\
5 -2 3
3 -1 -4 -1 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, L, R = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
list_cum_sum_A = [0]
now_sum_A = 0
for A in list_A:
    now_sum_A += A
    list_cum_sum_A.append(now_sum_A)
