import io
import sys

_INPUT = """\
7
joayo
joayo
joayo
joayo
joayo
joayo
joayo

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
Q = int(input())

# 処理
dict_name = {}
now_id = 0
for _ in range(Q):
    query = input()
    if query not in dict_name:
        now_id += 1
        dict_name[query] = now_id
        out = now_id
    else:
        out = dict_name[query]

    # 出力
    print(out)
