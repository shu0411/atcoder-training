import io
import sys

_INPUT = """\
10 15
1 8
2 m
1 3
1 10
2 q
1 6
1 10
2 d
1 1
2 z
1 9
2 f
1 4
1 7
2 k

"""
sys.stdin = io.StringIO(_INPUT)

# ほとんどは変わるはず。
# 変わらない時（タイルが置かれている間）だけ記録しておけばよさそう。
# タイルが置かれたとき、置いたidxと、その直前のクエリ2の色を記録
# タイルを除くとき→その後に2があれば問題なし。なければ除く前に記録してた色が答え。
# タイルが置いてあるidxと色のリスト、タイルを除いた直後のidxと色のリストを持つ。タイルをのぞいたらlistを移動。色を塗ったら除いたリストを空に
#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())

# 処理
last_color = "a"
dict_idx_color_covered = {}  # タイルを置いた時点のidxと色
dict_idx_color_uncovered = {}  # タイルを除いた直後のidxと色
for _ in range(Q):
    list_query = input().split()
    if list_query[0] == "1":
        X = int(list_query[1])
        if X in dict_idx_color_covered:
            dict_idx_color_uncovered[X] = dict_idx_color_covered[X]
            del dict_idx_color_covered[X]
        elif X in dict_idx_color_uncovered:
            dict_idx_color_covered[X] = dict_idx_color_uncovered[X]
            del dict_idx_color_uncovered[X]
        else:
            dict_idx_color_covered[X] = last_color
    else:
        C = list_query[1]
        last_color = C
        dict_idx_color_uncovered = {}
# 出力
list_out = []
for i in range(1, N + 1):
    if i in dict_idx_color_covered:
        list_out.append(dict_idx_color_covered[i])
    elif i in dict_idx_color_uncovered:
        list_out.append(dict_idx_color_uncovered[i])
    else:
        list_out.append(last_color)

out = "".join(list_out)
print(out)
