import io
import sys

_INPUT = """\
3
4
4 5 6 7
5
1 4 4 4 5
3
2 3 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    N = int(input())
    list_A = list(map(int, input().split()))

    out = 0

    tmp_A = list_A[-1]
    if tmp_A < list_A[0]:
        out = -1
    else:
        for i in range(N - 2, 0, -1):
            if list_A[i] > tmp_A:
                out += list_A[i] - tmp_A
            else:
                tmp_A = list_A[i]

        if tmp_A < list_A[0]:
            out = -1

    # 出力
    print(out)
