import io
import sys

_INPUT = """\
2
abc
1 2 3
a b c
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
Q = int(input())
S = input()
A, B, C = map(int, input().split())
list_D = input().split()
list_E = list(map(int, input().split()))

# 処理
for _ in range(Q):
    L, R = map(int, input().split())
    list_F = list(map(int, input().split()))
    out = R

    # 出力
    print(out)
