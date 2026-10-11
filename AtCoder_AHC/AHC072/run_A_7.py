import io
import sys

from A_7 import solve

# 手元で試したい入力を、この文字列へそのままコピペする。
INPUT = """\
14 9
..h...h#b.be.#
#....#...#.G.#
#C......#.A...
##e.g.....D.g.
.#ed...#.he...
e#..I..#.#F#.i
.....##...i#.#
f#.e...###...E
....#i.#e....#
.....##.....H.
a.b.f#.e#..f.d
#...gB......#.
i..###..#.##.#
#...ec#.#....#

"""


def run(input_text: str, output_stream):
    solve(io.StringIO(input_text), output_stream)


if __name__ == "__main__":
    run(INPUT, sys.stdout)
