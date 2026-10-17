import io
import sys

_INPUT = """\
9 37 480
12 123 132 213 231 312 321 500 1000

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K, T = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
list_A.sort()
count_push = 0
last_end_time = 0
for A in list_A:
    if A >= T:
        break

    if last_end_time < A:
        count_push += (A - last_end_time) // K
        if (A - last_end_time) % K != 0:
            count_push += 1

    last_end_time = A + K

if last_end_time < T:
    count_push += (T - last_end_time) // K
    if (T - last_end_time) % K != 0:
        count_push += 1

print(count_push)
