import io
import sys

_INPUT = """\
1
2
"""
sys.stdin = io.StringIO(_INPUT)

# D_1:N=1の場合を考慮しておらず、２行出力していた。
#############ここから下をコピペ#############


# 関数
def get_time(idx_right, idx_left):
    return (list_X[idx_right] - list_X[idx_left]) // 2


# 入力
N = int(input())
list_X = list(map(int, input().split()))

# 処理
max_time = get_time(-1, 0)

# k=1の時
print(max_time)

# k=2~N-1の時
for k in range(1, N - 1):

    # 先に左に動いたとき
    left_first_left_time = get_time(k, k - 1)
    left_first_right_time = left_first_left_time + get_time(k + 1, k)

    left_left_total_time = left_first_left_time + get_time(k - 1, 0)
    left_right_total_time = left_first_right_time + get_time(-1, k + 1)

    left_min_time = max(left_left_total_time, left_right_total_time)

    # 先に右に動いたとき
    right_first_right_time = get_time(k + 1, k)
    right_first_left_time = right_first_right_time + get_time(k, k - 1)

    right_right_total_time = right_first_right_time + get_time(-1, k + 1)
    right_left_total_time = right_first_left_time + get_time(k - 1, 0)

    right_min_time = max(right_right_total_time, right_left_total_time)

    # 最終的な最小値
    out = min(left_min_time, right_min_time)

    # 出力
    print(out)


# k=Nの時
if N >= 2:
    print(max_time)
