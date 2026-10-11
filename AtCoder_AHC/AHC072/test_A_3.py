import io
import unittest

from A_3 import make_operations, solve
from run_A_3 import run


class 同色一括移動テスト(unittest.TestCase):
    def test_重なった同色スライムをまとめて巣まで運ぶ(self):
        board = ["aa.A", "....", "....", "...."]

        operations = make_operations(board, 1)

        self.assertEqual(
            operations,
            [
                (0, 0, 0, "R", 1),
                (0, 1, 0, "R", 1),
                (0, 2, 0, "R", 1),
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

    def test_提出形式でまとめた操作を出力する(self):
        input_stream = io.StringIO("4 1\naa.A\n....\n....\n....\n")
        output_stream = io.StringIO()
        solve(input_stream, output_stream)
        self.assertEqual(
            output_stream.getvalue(),
            "0 0 0 R 1\n0 1 0 R 1\n0 2 0 R 1\n",
        )

    def test_コピペ入力からA3を実行できる(self):
        output_stream = io.StringIO()
        run("4 1\naa.A\n....\n....\n....\n", output_stream)
        self.assertEqual(
            output_stream.getvalue(),
            "0 0 0 R 1\n0 1 0 R 1\n0 2 0 R 1\n",
        )


if __name__ == "__main__":
    unittest.main()
