import io
import sys

_INPUT = """\
7 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
A, B = map(int, input().split())

# 処理
out = len(str(A + B))

# 出力
print(out)
