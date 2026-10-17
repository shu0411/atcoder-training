import io
import sys

_INPUT = """\
4 3
1 10 100 1000
3 6
6 10
8 8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import bisect

# 入力
N, Q = map(int, input().split())
list_A = list(map(int, input().split()))

# row = i回目に数列Bに追加した数を1行とみなす

# 各行の末尾が数列Bの前から何個目か
list_row_total_columns = [0]
total_columns = 0
for i in range(1, N + 1):
    total_columns += i
    list_row_total_columns.append(total_columns)

# 各行の合計（Aの累積和としても使える）
list_row_sum = [0]
row_sum = 0
for A in list_A:
    row_sum += A
    list_row_sum.append(row_sum)

# 各行の合計の累積和（LとRの間の行の合計算出に使用）
list_row_culmulative_sum = []
culmulative_sum = 0
for sum in list_row_sum:
    culmulative_sum += sum
    list_row_culmulative_sum.append(culmulative_sum)


def find_row_col(num):
    row = bisect.bisect_left(list_row_total_columns, num)
    col = num - list_row_total_columns[row - 1]
    return row, col


# 処理
for _ in range(Q):
    L, R = map(int, input().split())
    L_row, L_col = find_row_col(L)
    R_row, R_col = find_row_col(R)
    # print("L:" + str(L_row) + "," + str(L_col))
    # print("R:" + str(R_row) + "," + str(R_col))

    out = 0
    if L_row == R_row:
        out = list_row_sum[R_col] - list_row_sum[L_col - 1]
    else:
        # Lの行の合計
        out += list_row_sum[L_row] - list_row_sum[L_col - 1]
        # Rの行の合計
        out += list_row_sum[R_col]
        # 間の行の合計
        out += list_row_culmulative_sum[R_row - 1] - list_row_culmulative_sum[L_row]

    # 出力
    print(out)
