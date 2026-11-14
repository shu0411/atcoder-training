import io
import sys

_INPUT = """\
30
24 22 18 20 14 22 14 14 26 14 26 26 20 22 24 18 22 22 14 24 18 14 14 24 22 18 18 26 14 20

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
dict_A_count = {}
out = 1
before_A = -1
for i, A in enumerate(list_A):
    if A == before_A:
        if A not in dict_A_count:
            dict_A_count[A] = 0
        dict_A_count[A] += 1
        continue

    if A in dict_A_count:
        out += i - dict_A_count[A]
    else:
        out += i

    if A not in dict_A_count:
        dict_A_count[A] = 0
    dict_A_count[A] += 1

    before_A = A

# 出力
print(out)
