import io
import sys

_INPUT = """\
atcoder

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
len_S = len(S)
out = len_S * 2 - 1
for i in range(len_S - 1):
    max_len = min(i, len_S - i - 1)
    exists_diff = False
    for j in range(max_len):
        if S[i - j] != S[i + j]:
            if exists_diff:
                break
            else:
                exists_diff = True
        out += 1

    max_len = min(i, len_S - i - 2)
    exists_diff = False
    if S[i] != S[i + 1]:
        exists_diff = True
    for j in range(max_len):
        if S[i - j] != S[i + j + 1]:
            if exists_diff:
                break
            else:
                exists_diff = True
        out += 1

# 出力
print(out)
