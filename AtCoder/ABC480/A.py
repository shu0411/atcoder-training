import io
import sys

_INPUT = """\
BD
CA

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S1 = input()
S2 = input()

# 処理
out = "Yes"
if (
    S1[0] == "A"
    and S2[1] == "D"
    or S1[1] == "A"
    and S2[0] == "D"
    or S2[0] == "A"
    and S1[1] == "D"
    or S2[1] == "A"
    and S1[0] == "D"
):
    out = "No"


# 出力
print(out)
