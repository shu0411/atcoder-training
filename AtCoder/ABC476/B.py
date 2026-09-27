import io
import sys

_INPUT = """\
5
yiwiy
*****

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
S = input()
T = input()

# 処理
out = "Yes"
for i in range(N):
    if T[i] != "*" and S[i] != T[i]:
        out = "No"
        break

# 出力
print(out)
