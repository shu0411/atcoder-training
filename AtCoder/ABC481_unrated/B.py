import io
import sys

_INPUT = """\
2 100
1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
out = 0
if list_A[0] == K:
    out += 1
for i in range(N - 1):
    if list_A[i] < K and list_A[i + 1] >= K:
        out += 1
    elif list_A[i] > K and list_A[i + 1] <= K:
        out += 1

# 出力
print(out)
