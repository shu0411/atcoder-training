import io
import sys

_INPUT = """\
120
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import math

# 入力
N = int(input())

max_diff = int(math.sqrt(N + 8)) - 3

# 処理
out = 0
for diff in range(1, max_diff + 1):
    now_product = 1 + diff
    now_column = 1 + diff
    now_count = 2
    while now_product * (now_column + diff) <= N:
        now_column += diff
        now_count += 1
        now_product *= now_column

    out += (now_count - 1) * (now_count - 2) // 2

print(out)
