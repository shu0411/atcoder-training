import io
import sys

_INPUT = """\
10 16
102228 448944 131224 326172 500169 670309 976672 579051 974511 773940

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, V = map(int, input().split())
list_W = list(map(int, input().split()))

# 処理
max_w = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_value = i + j + k + 3
            sum_w = list_W[i] + list_W[j] + list_W[k]
            if sum_value <= V:
                max_w = max(max_w, sum_w)

# 出力
print(max_w)
