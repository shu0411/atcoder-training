import io
import sys

_INPUT = """\
30 25
1 2 2 22 14 10 14 10 18 5 15 8 17 22 10 17 11 25 13 16 9 19 26 7 11 12 23 3 30 30

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理

list_B = sorted(list_A)

cnt_match = 0
for i in range(N):
    if list_A[i] == list_B[i]:
        cnt_match += 1
    else:
        break

for i in range(N - 1, -1, -1):
    if list_A[i] == list_B[i]:
        cnt_match += 1
    else:
        break

out = "No"
if cnt_match >= N - K:
    out = "Yes"

# 出力
print(out)
