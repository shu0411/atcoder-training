import io
import unittest

from A_1 import find_slimes_and_nests, make_operations, solve
from run_A_1 import run


class 基本方針テスト(unittest.TestCase):
    def test_色ごとにスライムと巣の座標を記録する(self):
        board = ["a.A", ".b.", "B.a"]
        slimes, nests = find_slimes_and_nests(board, 2)
        self.assertEqual(slimes, [[(0, 0), (2, 2)], [(1, 1)]])
        self.assertEqual(nests, [(0, 2), (2, 0)])

    def test_各スライムを色順かつ最短経路で1マスずつ運ぶ(self):
        board = ["a.A", ".#.", "b.B"]
        operations = make_operations(board, 2)
        self.assertEqual(
            operations,
            [
                (0, 0, 0, "R", 1),
                (0, 1, 0, "R", 1),
                (2, 0, 0, "R", 1),
                (2, 1, 0, "R", 1),
            ],
        )

    def test_提出形式で操作だけを出力する(self):
        input_stream = io.StringIO("3 2\na.A\n.#.\nb.B\n")
        output_stream = io.StringIO()
        solve(input_stream, output_stream)
        self.assertEqual(
            output_stream.getvalue(),
            "0 0 0 R 1\n0 1 0 R 1\n2 0 0 R 1\n2 1 0 R 1\n",
        )

    def test_コピペした入力から同じ解法を実行できる(self):
        output_stream = io.StringIO()
        run("3 2\na.A\n.#.\nb.B\n", output_stream)
        self.assertEqual(
            output_stream.getvalue(),
            "0 0 0 R 1\n0 1 0 R 1\n2 0 0 R 1\n2 1 0 R 1\n",
        )


if __name__ == "__main__":
    unittest.main()
