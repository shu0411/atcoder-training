import io
import sys

_INPUT = """\
5 7
5 6 2 9
3 1 3 8
1 2
2 1
2 4
3 2
3 5
4 3
5 2

"""
sys.stdin = io.StringIO(_INPUT)

# 左に移動： min(始点のL, 始点のR + 自分より右にあるLの値の最小)
# 右に移動： min(始点のR, 始点のL + 自分より左にあるRの値の最小)
#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_L = (
    [float("inf")] + [float("inf")] + list(map(int, input().split())) + [float("inf")]
)
list_R = (
    [float("inf")] + list(map(int, input().split())) + [float("inf")] + [float("inf")]
)

list_min_L = [float("inf")] * (N + 2)  # 自分より右にあるLの値の最小
for i in range(N, 1, -1):
    list_min_L[i] = min(list_min_L[i + 1], list_L[i + 1])

list_min_R = [float("inf")] * (N + 2)  # 自分より左にあるRの値の最小
for i in range(1, N + 1):
    list_min_R[i] = min(list_min_R[i - 1], list_R[i - 1])


# 処理
for _ in range(Q):
    s, t = map(int, input().split())
    if s > t:
        out = min(list_L[s], list_R[s] + list_min_L[s])
    else:
        out = min(list_R[s], list_L[s] + list_min_R[s])

    # 出力
    print(out)
