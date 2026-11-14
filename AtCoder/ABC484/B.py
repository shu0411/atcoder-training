import io
import sys

_INPUT = """\
3
7 9 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
K = int(input())
list_A = list(map(int, input().split()))

# 処理
min_val = 9
has_nine = False

for A in list_A:
    if A == 9:
        has_nine = True
    min_val = min(A, min_val)

out = -1
if has_nine:
    out = min_val

# 出力
print(out)
