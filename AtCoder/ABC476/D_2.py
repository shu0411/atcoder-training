import io
import sys

_INPUT = """\
2 3 10
50 6
22 30
20 12 24

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M, K = map(int, input().split())
X, Y = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 処理
list_A.sort()
list_B.sort()

# ドリンクを買える最大量を特定
max_count_B = M
tmp_count_Y = 0
for i in range(M):
    B = list_B[i]
    if K * (Y - tmp_count_Y) >= B:
        tmp_count_Y += B // K
        if B % K != 0:
            tmp_count_Y += 1
    else:
        max_count_B = i
        break

# Yを1枚ずつ減らして、Aの個数を決め、maxを見つける

# Bを買えるだけ買ったとき
left_money = X + K * Y - sum(list_B[:max_count_B])
tmp_count_A = N
tmp_count_B = max_count_B
tmp_A_money = 0
for j in range(N):
    if tmp_A_money + list_A[j] > left_money:
        tmp_count_A = j
        break

    tmp_A_money += list_A[j]
max_count_AB = tmp_count_A + tmp_count_B

for i in range(max_count_B - 1, -1, -1):
    left_money += list_B[i]
    tmp_count_B -= 1
    for j in range(tmp_count_A, N):
        if tmp_A_money + list_A[j] > left_money:
            tmp_count_A = j
            break

        tmp_A_money += list_A[j]
    else:
        tmp_count_A = N

    max_count_AB = max(max_count_AB, tmp_count_A + tmp_count_B)

# 出力
print(max_count_AB)
