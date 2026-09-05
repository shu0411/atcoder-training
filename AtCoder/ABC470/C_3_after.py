import io
import sys

_INPUT = """\
3 8
1 2
1 3
1 1
1 2
1 1
2
1 3
1 1

"""
sys.stdin = io.StringIO(_INPUT)

# 反省：
# XORの差分更新という発想は正しかった。
# 旧実装は個数0のキーも残して毎回走査し、最悪O(Q^2)になっていた。
# また、全体減算を遅延管理する際、0で打ち止めになる処理を考慮できていなかった。
# 正の要素だけを走査すると、1回の処理で総和が必ず1減る。
# 減らせる総量はクエリ1による加算回数以下なので、全体でO(N+Q)。
# 二重ループという形だけで判断せず、内側の処理の総回数を評価する。
#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())

# 処理
list_A = [0] * N
set_idx_A = set()
now_xor = 0
for i in range(Q):
    list_query = list(map(int, input().split()))

    if list_query[0] == 1:
        x = list_query[1] - 1

        now_val = list_A[x]
        next_val = list_A[x] + 1
        list_A[x] = next_val

        # 現在の値から前の数を引いて、新しい数を足す
        now_xor ^= now_val ^ next_val
        set_idx_A.add(x)

    else:
        now_xor = 0
        new_set_idx_A = set()
        for key in set_idx_A:
            next_val = list_A[key] - 1
            list_A[key] = next_val
            if next_val > 0:
                now_xor ^= next_val
                new_set_idx_A.add(key)

        set_idx_A = new_set_idx_A

    # 出力
    print(now_xor)
