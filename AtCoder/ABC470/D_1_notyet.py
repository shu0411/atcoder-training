import io
import sys

_INPUT = """\
5 5
2 1 3 5 4
1 2 4
2
1 2 3
1 3 4
2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_P = list(map(int, input().split()))

# 処理

for i in range(Q):
    list_query = list(map(int, input().split()))

    if list_query[0] == 1:
        _, x, y = list_query

    else:
        pass

    out = N

    # 出力
    print(out)
