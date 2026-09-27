import io
import sys

_INPUT = """\
3
abcd
aaaaaaaaa
1 2
1 1
1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
Q = int(input())
S = input()
T = input()

# 事前処理
tmp_count = 0
list_count = [0]
len_S = len(S)
len_T = len(T)
for i in range(len_S - len_T + 1):
    if S[i : i + len_T] == T:
        tmp_count += 1
    list_count.append(tmp_count)

# query処理
for _ in range(Q):
    L, R = map(int, input().split())
    out = "No"
    if len_S >= len_T:
        target_idx_L = min(max(L - 1, 0), len_S - len_T + 1)
        target_idx_R = max(min(R - len_T + 1, len_S - len_T + 1), 0)
        if list_count[target_idx_R] - list_count[target_idx_L] > 0:
            out = "Yes"

    # 出力
    print(out)
