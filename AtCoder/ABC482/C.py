import io
import sys

_INPUT = """\
17 23 12 12
14 8
2 19
17 3
7 11
2 4
10 19
7 8
1 23
14 11
2 23
17 19
7 2
1 2 7
2 9 20
1 3 6
2 8 8
1 11 17
2 1 23
1 1 1
2 20 22
1 7 14
2 3 11
1 15 17
2 19 23

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import bisect

# 入力
H, W, N, Q = map(int, input().split())

# 入力（駒）
dict_R = {}
dict_C = {}

for _ in range(N):
    R, C = map(int, input().split())
    if R not in dict_R:
        dict_R[R] = 0
    dict_R[R] += 1

    if C not in dict_C:
        dict_C[C] = 0
    dict_C[C] += 1


# 累積和処理
sorted_dict_R = sorted(dict_R.items(), key=lambda x: x[0])
dict_cumsum_R = {-1: 0}
total_cnt_R = 0
for R, cnt_R in sorted_dict_R:
    total_cnt_R += cnt_R
    dict_cumsum_R[R] = total_cnt_R
list_idx_dict_cumsum_R = list(dict_cumsum_R.keys())

sorted_dict_C = sorted(dict_C.items(), key=lambda x: x[0])
dict_cumsum_C = {-1: 0}
total_cnt_C = 0
for C, cnt_C in sorted_dict_C:
    total_cnt_C += cnt_C
    dict_cumsum_C[C] = total_cnt_C
list_idx_dict_cumsum_C = list(dict_cumsum_C.keys())

# クエリ
for _ in range(Q):
    # 入力（クエリ）
    query_id, start, end = list(map(int, input().split()))

    # 処理
    if query_id == 1:
        # R処理
        idx_start_R = bisect.bisect_left(list_idx_dict_cumsum_R, start) - 1
        idx_end_R = bisect.bisect_right(list_idx_dict_cumsum_R, end) - 1
        start_R = list_idx_dict_cumsum_R[idx_start_R]
        end_R = list_idx_dict_cumsum_R[idx_end_R]
        out = dict_cumsum_R[end_R] - dict_cumsum_R[start_R]
    else:
        # C処理
        idx_start_C = bisect.bisect_left(list_idx_dict_cumsum_C, start) - 1
        idx_end_C = bisect.bisect_right(list_idx_dict_cumsum_C, end) - 1
        start_C = list_idx_dict_cumsum_C[idx_start_C]
        end_C = list_idx_dict_cumsum_C[idx_end_C]
        out = dict_cumsum_C[end_C] - dict_cumsum_C[start_C]

    # 出力
    print(out)
