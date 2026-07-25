import io
import sys

_INPUT = """\
10
7 3 9 8 10 3 1 5 5 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
out = 0
for i in range(1, N - 1):
    if list_A[i - 1] < list_A[i] and list_A[i] > list_A[i + 1]:
        out += 1

# 出力
print(out)
