import sys


def solve(input_stream, output_stream):
    input = input_stream.readline

    # 入力
    N = int(input())
    S = input().strip()
    A, B, C = map(int, input().split())
    list_D = input().split()
    list_E = list(map(int, input().split()))
    table_F = [input().strip() for _ in range(N)]

    # 処理
    out = N

    # 出力
    print(out, file=output_stream)


if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
