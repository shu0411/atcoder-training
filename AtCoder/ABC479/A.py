import io
import sys

_INPUT = """\
9
100 40 30 50 20 90 100 80 60

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
out = 0
for i, A in enumerate(list_A):
    if i % 2 == 0:
        out += A

# 出力
print(out)
