import io
import sys

_INPUT = """\
motor

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############


# 入力
S = input()

# 処理
# おなじ文字の判定
dict_s_idx = {}
for i, s in enumerate(list(S)):
    if s not in dict_s_idx:
        dict_s_idx[s] = []
    dict_s_idx[s].append(i)


# 関数：素数判定
def trial_odd_sqrt(n: int):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 2
    return True


# 関数：条件を満たす数か判定
def add_num(
    list_num: list[str],
    tmp_num: str,
    dict_s_idx: dict,
    count_digits: int,
    used_digit: list[int],
):
    if len(tmp_num) == count_digits:
        list_num.append(tmp_num)
        return

    for i in range(10):
        if i in used_digit:
            continue

        if len(dict_s_idx[S[len(tmp_num)]]) == 1:
            tmp_num += str(i)
            used_digit.append(i)
            add_num(list_num, tmp_num, dict_s_idx, count_digits, used_digit)


list_num = []

for i in range(1, 10):
    str_num = str(i)
    add_num(list_num, str_num, dict_s_idx, len(S), [i])

print(list_num)

# while True:


# # 出力
# print(out)
