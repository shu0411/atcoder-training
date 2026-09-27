import io
import sys

_INPUT = """\
6 3 18
9 9 1 2 1
"""
sys.stdin = io.StringIO(_INPUT)

# まずは左右に行けるだけ行く。（上限を超えないor端に到達）
# 多く行けた方を採用し、その時の移動距離を記録。
# 残りの分を反対側＊2でどれだけ行けるか。
#############ここから下をコピペ#############

# 入力
N, S, L = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
# 最終的に左に進むルート（左片道＋右往復）
tmp_left_dist = 0
tmp_left_count = 1
tmp_left_l = 0
tmp_left_r = N - 2
for i in range(S - 2, -1, -1):
    if tmp_left_dist + list_A[i] > L:
        tmp_left_l = i + 1
        break

    tmp_left_count += 1
    tmp_left_dist += list_A[i]

tmp_i = -1
for i in range(S - 1, N - 1):
    if tmp_left_dist + list_A[i] * 2 > L:
        tmp_left_r = i - 1
        break

    tmp_left_count += 1
    tmp_left_dist += list_A[i] * 2

# 端の調整（右2個*2増やして左1個減らしてもLを超えない場合、その方がcountが大きくなる）
while S != tmp_left_l and tmp_left_r <= N - 4:
    if (
        tmp_left_dist
        - list_A[tmp_left_l]
        + (list_A[tmp_left_r + 1] + list_A[tmp_left_r + 2]) * 2
        > L
    ):
        break

    tmp_left_count += 1
    tmp_left_dist -= list_A[tmp_left_l]
    tmp_left_dist += (list_A[tmp_left_r + 1] + list_A[tmp_left_r + 2]) * 2
    tmp_left_l += 1
    tmp_left_r += 2


# 最終的に右に進むルート（右片道＋左往復）
tmp_right_dist = 0
tmp_right_count = 1
tmp_right_l = 0
tmp_right_r = N - 2
for i in range(S - 1, N - 1):
    if tmp_right_dist + list_A[i] > L:
        tmp_right_r = i - 1
        break

    tmp_right_count += 1
    tmp_right_dist += list_A[i]

for i in range(S - 2, -1, -1):
    if tmp_right_dist + list_A[i] * 2 > L:
        tmp_right_l = i + 1
        break

    tmp_right_count += 1
    tmp_right_dist += list_A[i] * 2

# 端の調整（左2個*2増やして右1個減らしてもLを超えない場合、その方がcountが大きくなる）
while S != tmp_right_r and tmp_right_l >= 2:
    if (
        tmp_right_dist
        - list_A[tmp_right_r]
        + (list_A[tmp_right_l - 1] + list_A[tmp_right_l - 2]) * 2
        > L
    ):
        break

    tmp_right_count += 1
    tmp_right_dist -= list_A[tmp_right_r]
    tmp_right_dist += (list_A[tmp_right_l - 1] + list_A[tmp_right_l - 2]) * 2
    tmp_right_r -= 1
    tmp_right_l -= 2

out = max(tmp_left_count, tmp_right_count)

# 出力
print(out)
