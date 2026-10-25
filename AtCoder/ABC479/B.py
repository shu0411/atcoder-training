import io
import sys

_INPUT = """\
20
RRRSRRRRSSRRRRSRRRRR

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
S = input()

# 処理
max_cnt = 0
tmp_cnt = 0
for s in S:
    if s == "R":
        tmp_cnt += 1
    else:
        max_cnt = max(max_cnt, tmp_cnt)
        tmp_cnt = 0
else:
    max_cnt = max(max_cnt, tmp_cnt)

# 出力
print(max_cnt)
