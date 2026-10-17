import io
import sys

_INPUT = """\
5 8
takahashi
aoki
sato
kato
kano
aoki
takanashi
sano
atcoder
chokudai
kato
aoki
yato

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
dict_S = {input(): 0 for _ in range(N)}


def check_one_diff(check_S, check_T):
    if len(check_S) != len(check_T):
        return False

    check_diff_count = 0
    for i in range(len(check_S)):
        if check_S[i] != check_T[i]:
            check_diff_count += 1

    return check_diff_count == 1


# 処理
for i in range(M):
    T = input()

    if T in dict_S:
        dict_S[T] += 1
        continue

    target_S = ""
    for tmp_S in dict_S.keys():
        if check_one_diff(tmp_S, T):
            if target_S != "":
                break
            else:
                target_S = tmp_S
    else:
        if target_S != "":
            dict_S[target_S] += 1

# 出力
for cnt in dict_S.values():
    print(cnt)
