import io
import sys

_INPUT = """\
8
xxoxxoxx

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
S = "x" + input() + "x"

# 処理
out = 0
for i in range(1, N + 1):
    if S[i - 1] == "x" and S[i] == "x" and S[i + 1] == "x":
        out += 1

# 出力
print(out)
