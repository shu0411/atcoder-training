import io
import sys

_INPUT = """\
99 50

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())

# 処理
out = N - K + 1

# 出力
print(out)
