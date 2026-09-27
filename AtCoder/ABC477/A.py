import io
import sys

_INPUT = """\
Y
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
c = input()

# 処理
out = ""
if c == "B":
    out = "Y"
elif c == "Y":
    out = "R"
else:
    out = "B"

# 出力
print(out)
