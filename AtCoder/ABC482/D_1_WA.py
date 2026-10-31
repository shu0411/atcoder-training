import io
import sys

_INPUT = """\
9
140322306 171833796 356303608 595703832 701965684 798563428 857902324 933683272 971602066

"""
sys.stdin = io.StringIO(_INPUT)

# 前提：２転換の距離は、同じ方向に進んでいたら変わらない。向かい合って進んでいたら1秒間に-2

# k=1,Nのとき→反対側の端との距離の半分が答え
# k=2~N-1のとき
# 始点の両隣をどちらから感染させるかで変わる。
# 始点の隣が感染するまで：
# 両隣は始点に向かって動く。始点は、片方に向かって動き、隣を感染させたら反対を感染させる。
# 始点の隣が感染してから：
# 始点の隣が感染するまでは、両隣が始点に向かって動くため、両隣と端点の距離は変わらなかった。
# 始点の隣が感染してからは、その点とそちら側の端の点との距離の半分が所要時間。
# 左右それぞれの端が感染するまでにかかる時間を比べて多いほうが、答えの候補となる。
# 始点が最初に左に動いた時と右に動いた時を比べ、小さいほうが答えとなる。
#############ここから下をコピペ#############


# 関数
def get_time(idx_right, idx_left):
    return (list_X[idx_right] - list_X[idx_left]) // 2


# 入力
N = int(input())
list_X = list(map(int, input().split()))

# 処理
max_time = get_time(-1, 0)

# k=1の時
print(max_time)

# k=2~N-1の時
for k in range(1, N - 1):

    # 先に左に動いたとき
    left_first_left_time = get_time(k, k - 1)
    left_first_right_time = left_first_left_time + get_time(k + 1, k)

    left_left_total_time = left_first_left_time + get_time(k - 1, 0)
    left_right_total_time = left_first_right_time + get_time(-1, k + 1)

    left_min_time = max(left_left_total_time, left_right_total_time)

    # 先に右に動いたとき
    right_first_right_time = get_time(k + 1, k)
    right_first_left_time = right_first_right_time + get_time(k, k - 1)

    right_right_total_time = right_first_right_time + get_time(-1, k + 1)
    right_left_total_time = right_first_left_time + get_time(k - 1, 0)

    right_min_time = max(right_right_total_time, right_left_total_time)

    # 最終的な最小値
    out = min(left_min_time, right_min_time)

    # 出力
    print(out)


# k=Nの時
print(max_time)
