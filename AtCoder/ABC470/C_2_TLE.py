import io
import sys

_INPUT = """\
2 5
1 2
1 2
1 1
2
2

"""
sys.stdin = io.StringIO(_INPUT)

# 数字の個数を辞書で保持する形。
# クエリ1：愚直に現在のXORの結果から該当の数を除き（XORは同じ数をもう1回XORすると消える）、新しい数を加えている。→OK
# クエリ2：その時点のすべての数字が1以上化を確認して1を引いている。TLE
# →そもそも辞書で保持する形が今回の場合あまり高速ではなかった。
#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())

# 処理
dict_A = {}
dict_count_A = {}
count_query_2 = 0
now_xor = 0
for i in range(Q):
    list_query = list(map(int, input().split()))

    if list_query[0] == 1:
        x = list_query[1]
        if x not in dict_A:
            dict_A[x] = 0

        # 現在の値から引く
        now_xor ^= max(dict_A[x] - count_query_2, 0)

        if dict_A[x] != 0:
            dict_count_A[dict_A[x]] -= 1

        dict_A[x] += 1

        if dict_A[x] not in dict_count_A:
            dict_count_A[dict_A[x]] = 0
        dict_count_A[dict_A[x]] += 1

        # 新しい値を足す
        now_xor ^= max(dict_A[x] - count_query_2, 0)

    else:
        count_query_2 += 1

        now_xor = 0
        for key, value in dict_count_A.items():
            if value % 2 == 1:
                now_xor ^= max(key - count_query_2, 0)

    # 出力
    print(now_xor)
