import io
import unittest

from A_2 import make_operations, solve
from run_A_2 import run


class 同方向移動まとめテスト(unittest.TestCase):
    def test_塔の上から同じ方向へ進む移動をまとめる(self):
        board = ["aa.A", "....", "....", "...."]

        operations = make_operations(board, 1)

        self.assertEqual(
            operations,
            [
                (0, 0, 0, "R", 1),
                (0, 1, 1, "R", 2),
                (0, 1, 0, "R", 1),
                (0, 2, 0, "R", 1),
            ],
        )

    def test_一匹だけのときは飛距離一のままにする(self):
        board = ["a..A", "....", "....", "...."]
        operations = make_operations(board, 1)
        self.assertEqual(
            operations,
            [
                (0, 0, 0, "R", 1),
                (0, 1, 0, "R", 1),
                (0, 2, 0, "R", 1),
            ],
        )

    def test_提出形式でまとめた操作を出力する(self):
        input_stream = io.StringIO("4 1\naa.A\n....\n....\n....\n")
        output_stream = io.StringIO()
        solve(input_stream, output_stream)
        self.assertEqual(
            output_stream.getvalue(),
            "0 0 0 R 1\n0 1 1 R 2\n0 1 0 R 1\n0 2 0 R 1\n",
        )

    def test_コピペ入力からA2を実行できる(self):
        output_stream = io.StringIO()
        run("4 1\naa.A\n....\n....\n....\n", output_stream)
        self.assertEqual(
            output_stream.getvalue(),
            "0 0 0 R 1\n0 1 1 R 2\n0 1 0 R 1\n0 2 0 R 1\n",
        )


if __name__ == "__main__":
    unittest.main()
