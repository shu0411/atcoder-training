import io
import sys

_INPUT = """\
5
-2 3 -2 4 -5

"""
sys.stdin = io.StringIO(_INPUT)

# 前から順に、その移動をする前の最大最小を記録
# 最終的にたどり着く位置と、何も入れ替えなかった時の座標数を記録
# 後ろから順に、そこで入れ替えた時の最大、最小を求める→入れ替えた時の座標数を求め、max座標数を更新
#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
max_pos = 0
min_pos = 0
now_pos = 0
list_before_max_pos = [0]
list_before_min_pos = [0]
for A in list_A:
    now_pos += A
    max_pos = max(max_pos, now_pos)
    min_pos = min(min_pos, now_pos)
    list_before_max_pos.append(max_pos)
    list_before_min_pos.append(min_pos)

final_pos = now_pos
final_score = max_pos - min_pos + 1

now_max_pos = final_pos
now_min_pos = final_pos
for i in range(N - 1, -1, -1):
    A = list_A[i]

    if A > 0:
        potential_min_pos = now_min_pos + A * (-2)
        tmp_score = list_before_max_pos[i] - min(min_pos, potential_min_pos) + 1
    else:
        potential_max_pos = now_max_pos + A * (-2)
        tmp_score = max(max_pos, potential_max_pos) - list_before_min_pos[i] + 1

    final_score = max(final_score, tmp_score)

    now_pos -= A
    now_max_pos = max(now_max_pos, now_pos)
    now_min_pos = min(now_min_pos, now_pos)

print(final_score)
