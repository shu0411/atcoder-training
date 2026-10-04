import io
import sys

from A_1 import solve


# 手元で試したい入力を、この文字列へそのままコピペする。
INPUT = """\
2
abc
1 2 3
a b c
1 2 3
"""


def run(input_text: str, output_stream):
    solve(io.StringIO(input_text), output_stream)


if __name__ == "__main__":
    run(INPUT, sys.stdout)
