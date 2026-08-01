import io
import sys

_INPUT = """\
5 6
1 4
1 2
1 3
1 3
3 5
3 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

dict_win_count = {i: 0 for i in range(1, N + 1)}
dict_list_win_match = {i: set() for i in range(1, N + 1)}
list_list_AB = []
for i in range(M):
    A, B = map(int, input().split())
    list_list_AB.append([A, B])
    dict_win_count[A] += 1
    dict_list_win_match[A].add(i)
    dict_win_count[B] += 1
    dict_list_win_match[B].add(i)


# 関数
def is_match(a: int, b: int):
    set_a = dict_list_win_match[a]
    set_b = dict_list_win_match[b]
    union_set = set_a | set_b
    return len(union_set) == M


def count_pairs(target: list):
    tmp_count = 0
    for i in range(len(target)):
        for j in range(i + 1, len(target)):
            if is_match(target[i], target[j]):
                tmp_count += 1
    return tmp_count


def count_winner_pairs(winner: int):
    tmp_count = 0
    list_left_list_AB = []
    for i in range(M):
        if i not in dict_list_win_match[winner]:
            list_left_list_AB.append(list_list_AB[i])

    is_A = True
    is_B = True
    first_A = list_left_list_AB[0][0]
    first_B = list_left_list_AB[0][1]
    for list_AB in list_left_list_AB:
        if first_A not in list_AB:
            is_A = False
        if first_B not in list_AB:
            is_B = False

        if not is_A and not is_B:
            break
    if is_A:
        tmp_count += 1
    if is_B:
        tmp_count += 1
    return tmp_count


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
    out = 0
else:
    if N >= 4 and list_key_value[3][1] == key_value_rank_1[1]:
        out = count_pairs(
            [
                key_value_rank_1[0],
                key_value_rank_2[0],
                list_key_value[2][0],
                list_key_value[3][0],
            ]
        )
    elif N >= 3 and list_key_value[2][1] == key_value_rank_1[1]:
        out = count_pairs(
            [key_value_rank_1[0], key_value_rank_2[0], list_key_value[2][0]]
        )
    elif key_value_rank_2[1] == key_value_rank_1[1]:
        out = (
            count_winner_pairs(key_value_rank_1[0])
            + count_winner_pairs(key_value_rank_2[0])
            - count_pairs([key_value_rank_1[0], key_value_rank_2[0]])
        )
    else:
        out = count_winner_pairs(key_value_rank_1[0])

# 出力
print(out)
