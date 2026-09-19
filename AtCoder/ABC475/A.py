import io
import sys

_INPUT = """\
oo

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = "o".join(S)

# 出力
print(out)
