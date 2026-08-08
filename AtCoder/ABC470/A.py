import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
for i in range(1, N + 1):
    out = i
    if i % 3 == 0:
        out = "Fizz"

    # 出力
    print(out)
