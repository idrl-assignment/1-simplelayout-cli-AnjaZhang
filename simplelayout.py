import argparse
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board_grid", type=int, help="layout pixel")
    ap.add_argument("--unit_grid", type=int, help="rectangle pixel")
    ap.add_argument("--unit_n", type=int, help="number of rectangles")
    ap.add_argument(
        "--positions", nargs="+", type=int, help="the positions of rectangles"
    )
    ap.add_argument(
        "-o",
        "--outdir",
        type=str,
        default="example_dir/",
        help="rectangle point order number",
    )
    ap.add_argument(
        "--file_name", type=str, default="example", help="the saved file name"
    )
    args = vars(ap.parse_args())
    board_grid = args["board_grid"]
    unit_grid = args["unit_grid"]
    # 要求`board_grid` 能整除 `unit_grid`
    assert (
        board_grid % unit_grid == 0
    ), "The board_graid cannot be devided by unit_grid!"
    unit_n = args["unit_n"]
    positions = args["positions"]
    # 要求`positions` 数量与 `unit_n` 一致
    assert len(positions) == unit_n, "The position number must equal to unit_n!"
    # 要求组件位置为从1开始的整数，上限为 `(board_grid/unit_grid)^2`
    assert (min(positions) >= 1) and (
        max(positions) <= (board_grid / unit_grid) ** 2
    ), "The positions are out of scope!"
    outdir = args["outdir"]
    file_name = args["file_name"]
    # 判断给定路径是否存在，不存在则创建
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    # 生成文件
    file_1 = open(outdir + file_name + ".mat", "w")
    file_1.close()
    file_2 = open(outdir + file_name + ".jpg", "w")
    file_2.close()
    return None


if __name__ == "__main__":
    main()
