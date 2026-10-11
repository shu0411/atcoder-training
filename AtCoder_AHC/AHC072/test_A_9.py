import io
import unittest

from A_9 import make_operations, solve
from run_A_9 import run


class 最遠塔再選択テスト(unittest.TestCase):
    def test_合流後は合流した塔を含めて最遠を選び直す(self):
        board = ["Aaaa", "....", "....", "...."]

        operations = make_operations(board, 1)

        self.assertEqual(
            operations,
            [
                (0, 3, 0, "L", 1),
                (0, 2, 0, "L", 1),
                (0, 1, 0, "L", 1),
            ],
        )

    def test_九匹目との合流前に手前のスライムを帰巣させる(self):
        board = ["Aaaaaaaaaa.."] + ["............"] * 11
        operations = make_operations(board, 1)
        self.assertEqual(len(operations), 10)

    def test_合流相手の現在位置から距離を毎回計算できる(self):
        board = [
            "A.....",
            "......",
            "..a..a",
            ".a....",
            "......",
            "......",
        ]
        operations = make_operations(board, 1)
        self.assertGreater(len(operations), 0)

    def test_提出形式で最遠塔を選び直す(self):
        input_text = "4 1\nAaaa\n....\n....\n....\n"
        output_stream = io.StringIO()
        solve(io.StringIO(input_text), output_stream)
        self.assertEqual(len(output_stream.getvalue().splitlines()), 3)

    def test_コピペ入力からA9を実行できる(self):
        input_text = "4 1\nAaaa\n....\n....\n....\n"
        output_stream = io.StringIO()
        run(input_text, output_stream)
        self.assertEqual(len(output_stream.getvalue().splitlines()), 3)


if __name__ == "__main__":
    unittest.main()

