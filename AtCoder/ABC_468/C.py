import io
import sys

_INPUT = """\
3
1 3 2
3 1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import math

# 入力
N = int(input())
list_P = list(map(int, input().split()))
list_Q = list(map(int, input().split()))

out = 0
set_used_idx = set()


# list_Pでその桁がその数字の時のその桁以下の合計数の計算
def calc_P_under_digit(idx, tmp_out, set_used_idx):
    if idx == N - 1:
        return tmp_out

    now_digit_num = list_P[idx]
    used_larger_num_cnt = len(
        list(filter(lambda x: x > now_digit_num, list(set_used_idx)))
    )
    larger_num_cnt = N - now_digit_num - used_larger_num_cnt
    right_digit = N - idx - 1
    tmp_out += larger_num_cnt * math.factorial(right_digit)
    set_used_idx.add(now_digit_num)
    tmp_out = calc_P_under_digit(idx + 1, tmp_out, set_used_idx)
    return tmp_out


# list_Qでその桁がその数字の時のその桁以下の合計数の計算
def calc_Q_under_digit(idx, tmp_out, set_used_idx):
    if idx == N - 1:
        return tmp_out

    now_digit_num = list_Q[idx]
    used_smaller_num_cnt = len(
        list(filter(lambda x: x < now_digit_num, list(set_used_idx)))
    )
    smaller_num_cnt = now_digit_num - 1 - used_smaller_num_cnt
    right_digit = N - idx - 1
    tmp_out += smaller_num_cnt * math.factorial(right_digit)
    set_used_idx.add(now_digit_num)
    tmp_out = calc_Q_under_digit(idx + 1, tmp_out, set_used_idx)
    return tmp_out


# 同じ数字より下の桁の計算
def calc_under_same_num(idx, out, set_used_idx):
    # PとQの間の数がある場合、その桁がその間の数であるものはすべて対象
    diff = list_Q[idx] - list_P[idx] - 1
    right_digit = N - idx - 1
    out += diff * math.factorial(right_digit)

    # idx桁目がlist_P[idx]で範囲内の数の合計
    out += calc_P_under_digit(idx + 1, 0, set_used_idx.union({list_P[idx]}))
    # idx桁目がlist_Q[idx]で範囲内の数の合計
    out += calc_Q_under_digit(idx + 1, 0, set_used_idx.union({list_Q[idx]}))

    return out


# その桁が同じ数字かどうかの判定
def valid_digit(idx, out, set_used_idx):
    if list_P[idx] > list_Q[idx]:
        return 0
    if list_P[idx] == list_Q[idx]:
        if idx == N - 1:
            return 0
        else:
            set_used_idx.add(list_P[idx])
            return valid_digit(idx + 1, out, set_used_idx)
    else:
        return calc_under_same_num(idx, out, set_used_idx)


# 処理
out = valid_digit(0, out, set_used_idx)

# 出力
print(out)
