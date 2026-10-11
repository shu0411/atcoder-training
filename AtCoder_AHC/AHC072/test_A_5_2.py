import io
import unittest

from A_5_2 import make_operations, solve
from run_A_5_2 import run


class 塔の高さ制限テスト(unittest.TestCase):
    def test_九匹目と合流する前に手前のスライムを帰巣させる(self):
        board = ["Aaaaaaaaaa.."] + ["............"] * 11

        operations = make_operations(board, 1)

        self.assertEqual(len(operations), 10)
        self.assertEqual(
            operations[-3:],
            [
                (0, 1, 0, "L", 1),
                (0, 2, 0, "L", 1),
                (0, 1, 0, "L", 1),
            ],
        )

    def test_八匹までは一つの塔として運ぶ(self):
        board = ["Aaaaaaaaa..."] + ["............"] * 11
        operations = make_operations(board, 1)
        self.assertEqual(len(operations), 8)

    def test_提出形式で高さ制限を守った操作を出力する(self):
        input_text = "12 1\nAaaaaaaaaa..\n" + "............\n" * 11
        output_stream = io.StringIO()
        solve(io.StringIO(input_text), output_stream)
        self.assertEqual(len(output_stream.getvalue().splitlines()), 10)

    def test_コピペ入力からA5_2を実行できる(self):
        input_text = "12 1\nAaaaaaaaaa..\n" + "............\n" * 11
        output_stream = io.StringIO()
        run(input_text, output_stream)
        self.assertEqual(len(output_stream.getvalue().splitlines()), 10)


if __name__ == "__main__":
    unittest.main()

