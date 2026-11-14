import io
import sys

_INPUT = """\
30
25 11 21 15 30 20 17 19 17 21 10 13 22 10 22 14 30 25 17 25 11 19 27 27 15 18 16 16 20 16
25 11 15 30 20 17 19 17 21 10 13 22 10 22 14 30 25 17 25 11 19 27 27 15 21 18 16 16 20 16

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 処理
result_A = True
is_changing_A = False
is_changed_A = False
changing_A_value = -1
for i in range(N):
    if not is_changing_A:
        if list_A[i] != list_B[i]:
            is_changing_A = True
            changing_A_value = list_A[i]
    elif not is_changed_A:
        if i == (N - 1) or list_A[i + 1] != list_B[i]:
            if list_B[i] == changing_A_value:
                is_changed_A = True
            else:
                result_A = False
                break
    else:
        if list_A[i] != list_B[i]:
            result_A = False
            break

if result_A and is_changing_A and not is_changed_A:
    result_A = False

result_B = True
is_changing_B = False
is_changed_B = False
changing_B_value = -1
for i in range(N):
    if not is_changing_B:
        if list_A[i] != list_B[i]:
            is_changing_B = True
            changing_B_value = list_B[i]
    elif not is_changed_B:
        if i == (N - 1) or list_A[i] != list_B[i + 1]:
            if list_A[i] == changing_B_value:
                is_changed_B = True
            else:
                result_B = False
                break
    else:
        if list_A[i] != list_B[i]:
            result_B = False
            break

if result_B and is_changing_B and not is_changed_B:
    result_B = False

out = "Yes"

if not result_A and not result_B:
    out = "No"

# 出力
print(out)
