import io
import sys

_INPUT = """\
.

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

cnt = 0
for s in S:
    if s == "o":
        cnt += 1

# 処理
if cnt % 2 == 1:
    out = "odd"
else:
    out = "even"

# 出力
print(out)
