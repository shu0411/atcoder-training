import io
import sys

_INPUT = """\
5 4
3 5 2 4 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_K = list(map(int, input().split()))

# 処理
list_card = [i for i in range(1, N + 1)]

for K in list_K:
    tmp_list_card = list_card.copy()
    for i in range(K):
        tmp_list_card[i] = list_card[K - i - 1] * (-1)
    list_card = tmp_list_card.copy()

# 出力
for out in list_card:
    print(out)
