import io
import sys

_INPUT = """\
8 3
4 77 20 26 9 26 22 40

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, D = map(int, input().split())
list_X = list(map(int, input().split()))

# 処理
list_out = []
for i, X in enumerate(list_X):
    for j, check_X in enumerate(list_X):
        if i != j and abs(X - check_X) < D:
            break
    else:
        list_out.append(i + 1)

# 出力
print(len(list_out))
print(*list_out)
