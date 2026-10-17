import io
import sys

_INPUT = """\
5 9
6 4
9 1
2 1
4 3
5 4
4
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, W = map(int, input().split())


# 処理
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(N):
    A, B = map(int, input().split())
    for w in range(W + 1):
        if w >= B:
            dp[i + 1][w] = max(dp[i][w], dp[i][w - B] + A)
        else:
            dp[i + 1][w] = dp[i][w]

# 出力
print(dp[N][W])
