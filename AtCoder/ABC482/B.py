import io
import sys

_INPUT = """\
.....
.....
.....
.....
.....

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
table_S = [input() for _ in range(5)]

# 処理
max_o_cnt = 0

# 横
for S in table_S:
    tmp_cnt = list(S).count("o")
    max_o_cnt = max(max_o_cnt, tmp_cnt)

# 縦
for i in range(5):
    tmp_cnt = 0
    for j in range(5):
        if table_S[j][i] == "o":
            tmp_cnt += 1

    max_o_cnt = max(max_o_cnt, tmp_cnt)

# 斜め（左上から）
tmp_cnt = 0
for i in range(5):
    if table_S[i][i] == "o":
        tmp_cnt += 1
max_o_cnt = max(max_o_cnt, tmp_cnt)

# 斜め（右上から）
tmp_cnt = 0
for i in range(5):
    if table_S[i][5 - i - 1] == "o":
        tmp_cnt += 1
max_o_cnt = max(max_o_cnt, tmp_cnt)

# 必要数
out = 5 - max_o_cnt

# 出力
print(out)
