import io
import sys

_INPUT = """\
1
x

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
S = input()

# 処理
count_o = 0
count_x = 0
max_count_diff = 0
list_count_o = []
list_count_x = []
list_count_diff = []
list_count_max_diff = []
for i in range(N):
    if S[i] == "o":
        count_o += 1
    list_count_o.append(count_o)


for i in range(N):
    first_o = list_count_o[i]

    tmp_left = 0
    tmp_right = i
    tmp_count_o = first_o
    # 残っているoの個数分だけoの個数を探索する処理を繰り返す
    while tmp_count_o > 0:
        tmp_left = tmp_right + 1
        tmp_right = min(tmp_right + tmp_count_o, N - 1)
        tmp_count_o = list_count_o[tmp_right] - list_count_o[tmp_left - 1]

    out = tmp_right + 1
    # 出力
    print(out)
