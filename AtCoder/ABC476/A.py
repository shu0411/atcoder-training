import io
import sys

_INPUT = """\
chimpanzee

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = S
if S[-1] == "e":
    out += "r"
else:
    out += "er"

# 出力
print(out)
