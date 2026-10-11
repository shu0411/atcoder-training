import io
import sys

from A_2 import solve


# 手元で試したい入力を、この文字列へそのままコピペする。
INPUT = """\
12 4
............
...c.##.....
.A..c##.....
...c#.##....
c..##.###B..
aa.#...##.b.
..##C..###..
.a#.d#..##.b
a##d.##b.##.
d...####b...
...######...
.d.......D..
"""


def run(input_text: str, output_stream):
    solve(io.StringIO(input_text), output_stream)


if __name__ == "__main__":
    run(INPUT, sys.stdout)
