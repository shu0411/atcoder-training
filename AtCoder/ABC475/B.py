import io
import sys

_INPUT = """\
3
1000 1000 1000

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
dict_out = {1: 0, 10: 0, 100: 0}
for A in list_A:
    if A % 1000 != 0:
        count_1000 = A // 1000 + 1
        charge = count_1000 * 1000 - A
        dict_out[100] += charge // 100
        dict_out[10] += charge // 10 % 10
        dict_out[1] += charge % 10

# 出力
print(*dict_out.values())
