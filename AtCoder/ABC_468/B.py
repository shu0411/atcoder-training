import io
import sys

_INPUT = """\
21 2
....G...GG.....G.....

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
M, D = map(int, input().split())
S = input()


# 処理
list_looked = [False] * M

for i in range(M):
    looked_area = S[max(0, i - D) : min(i + D + 1, M)]
    for s in looked_area:
        if s == "G":
            list_looked[i] = True
            break

out = list_looked.count(False)

# 出力
print(out)
