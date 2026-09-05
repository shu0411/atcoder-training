import io
import sys

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
X = int(input())

# 処理
Y = X // 25
Z = X % 25

list_tmp_out = ["C"] * (24 - Y) + ["A"] * Z + ["C"] + ["A"] * (25 - Z) + ["C"] * Y

out = "R".join(list_tmp_out)

# 出力
print(out)
