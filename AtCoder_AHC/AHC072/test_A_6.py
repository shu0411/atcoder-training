import io
import unittest

from A_6 import make_operations, solve
from run_A_6 import run


class 仲間経由選択テスト(unittest.TestCase):
    def test_直接帰巣より有利な仲間を経由して合流する(self):
        board = ["A..a", "..a.", "....", "...."]

        operations = make_operations(board, 1)

        self.assertEqual(
            operations,
            [
                (0, 3, 0, "D", 1),
                (1, 3, 0, "L", 1),
                (1, 2, 0, "U", 1),
                (0, 2, 0, "L", 1),
                (0, 1, 0, "L", 1),
            ],
        )

    def test_九匹目との合流前に手前のスライムを帰巣させる(self):
        board = ["Aaaaaaaaaa.."] + ["............"] * 11
        operations = make_operations(board, 1)
        self.assertEqual(len(operations), 10)

    def test_提出形式で仲間を経由した操作を出力する(self):
        input_stream = io.StringIO("4 1\nA..a\n..a.\n....\n....\n")
        output_stream = io.StringIO()
        solve(input_stream, output_stream)
        self.assertEqual(len(output_stream.getvalue().splitlines()), 5)

    def test_コピペ入力からA6を実行できる(self):
        output_stream = io.StringIO()
        run("4 1\nA..a\n..a.\n....\n....\n", output_stream)
        self.assertEqual(len(output_stream.getvalue().splitlines()), 5)


if __name__ == "__main__":
    unittest.main()
