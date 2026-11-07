import io
import sys

_INPUT = """\
59

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
out = N // 2 + (N % 2)

# 出力
print(out)
