import io
import sys

_INPUT = """\
4 17
1 100
1 100
1 100
1 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, W = map(int, input().split())
table_AB = [list(map(int, input().split())) for _ in range(N)]

# 処理
max_A = 0
for i in range(2**N):
    tmp_sum_A = 0
    tmp_sum_B = 0
    binary_i = bin(i)[2:].zfill(N)
    for j, flag in enumerate(list(binary_i)):
        if flag == "1":
            A, B = table_AB[j]
            if tmp_sum_B + B > W:
                break

            tmp_sum_A += A
            tmp_sum_B += B

    max_A = max(max_A, tmp_sum_A)

# 出力
print(max_A)
