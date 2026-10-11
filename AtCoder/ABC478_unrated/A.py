import io
import sys

_INPUT = """\
12 3456

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

# 処理
quotient = M // N
remainder = M % N

# 出力
for _ in range(remainder):
    print(quotient + 1)
for _ in range(N - remainder):
    print(quotient)
