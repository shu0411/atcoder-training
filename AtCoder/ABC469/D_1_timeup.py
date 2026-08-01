import io
import sys

_INPUT = """\
5 5
1 2
3 4
1 3
2 3
2 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

dict_win_count = {i: 0 for i in range(1, N + 1)}
dict_list_win_match = {i: [] for i in range(1, N + 1)}
list_list_AB = []
for i in range(M):
    A, B = map(int, input().split())
    list_list_AB.append([A, B])
    dict_win_count[A] += 1
    dict_list_win_match[A].append(i)
    dict_win_count[B] += 1
    dict_list_win_match[B].append(i)

# 処理
out = 0

list_key_value = list(dict_win_count.items())
list_key_value.sort(key=lambda x: x[1], reverse=True)

key_value_rank_1 = list_key_value[0]
key_value_rank_2 = list_key_value[1]

if key_value_rank_1[1] == M:
    # 全勝がいた場合、全勝が2人ならその2人のどちらかとその人以外。1人ならその人とその人以外。
    if key_value_rank_2[1] == M:
        out = (N - 1) * 2
    else:
        out = N - 1
elif key_value_rank_1[1] < M // 2:
    # 勝ちが一番多い人の勝ち数が試合数の半分以下の場合、条件を満たす組み合わせは起きない。
    out = -1
else:
    key_value_rank_3 = list_key_value[2]
    key_value_rank_4 = list_key_value[3]

    if key_value_rank_4[1] == key_value_rank_1[1]:
        pass

# 出力
print(out)
