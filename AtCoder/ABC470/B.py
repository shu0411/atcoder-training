import io
import sys

_INPUT = """\
9
4 2 3 3 4 1 2 7 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_C = list(map(int, input().split()))

# 処理
dict_C = {}
for C in list_C:
    if C not in dict_C:
        dict_C[C] = 0
    dict_C[C] += 1

max_cnt_C = max(list(dict_C.values()))
out = N - max_cnt_C

# 出力
print(out)
