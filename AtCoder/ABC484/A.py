import io
import sys

_INPUT = """\
8 8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
B, R = map(int, input().split())

# 処理
out = (30 - B) * (30 - R)

# 出力
print(out)
