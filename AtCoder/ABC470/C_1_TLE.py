import io
import sys

_INPUT = """\
3 8
1 2
1 3
1 1
1 2
1 1
2
1 3
1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())

# 処理
dict_A = {}
for i in range(Q):
    list_query = list(map(int, input().split()))

    if list_query[0] == 1:
        x = list_query[1]
        if x not in dict_A:
            dict_A[x] = 0
        dict_A[x] += 1

    else:
        tmp_dict_A = {}
        for key, value in dict_A.items():
            if value != 1:
                tmp_dict_A[key] = value - 1
        dict_A = tmp_dict_A.copy()

    list_A_count = list(dict_A.values())
    out = 0
    for A_count in list_A_count:
        out ^= A_count

    # 出力
    print(out)
