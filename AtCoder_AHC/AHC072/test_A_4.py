import io
import unittest

from A_4 import make_operations, solve
from run_A_4 import run


class 遠い順処理テスト(unittest.TestCase):
    def test_巣から遠いスライムを先に動かして近いスライムと合流する(self):
        board = ["Aaa.", "....", "....", "...."]

        operations = make_operations(board, 1)

        self.assertEqual(
            operations,
            [
                (0, 2, 0, "L", 1),
                (0, 1, 0, "L", 1),
            ],
        )

    def test_異色スライムは残して同色だけを移動する(self):
        board = ["ab.A", ".B..", "....", "...."]
        operations = make_operations(board, 2)
        self.assertEqual(
            operations,
            [
                (0, 0, 0, "R", 1),
                (0, 1, 1, "R", 2),
                (0, 1, 0, "D", 1),
            ],
        )

    def test_提出形式で遠いスライムから処理した操作を出力する(self):
        input_stream = io.StringIO("4 1\nAaa.\n....\n....\n....\n")
        output_stream = io.StringIO()
        solve(input_stream, output_stream)
        self.assertEqual(output_stream.getvalue(), "0 2 0 L 1\n0 1 0 L 1\n")

    def test_コピペ入力からA4を実行できる(self):
        output_stream = io.StringIO()
        run("4 1\nAaa.\n....\n....\n....\n", output_stream)
        self.assertEqual(output_stream.getvalue(), "0 2 0 L 1\n0 1 0 L 1\n")


if __name__ == "__main__":
    unittest.main()
