import io
import sys

_INPUT = """\
BANANA

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = ""
for s in S:
    if s == "A":
        out += "A"
    else:
        out += "."

# 出力
print(out)
