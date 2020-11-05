import argparse
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board_grid", type=int, help="layout pixel")
    ap.add_argument("--unit_grid", type=int, help="rectangle pixel")
    ap.add_argument("--unit_n", type=int, help="number of rectangles")
    ap.add_argument("--positions", nargs="+", type=int, help="number of rectangles")
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
    assert (
        board_grid % unit_grid == 0
    ), "The board_graid cannot be devided by unit_grid!"
    positions = args["positions"]
    assert (min(positions) >= 1) and (
        max(positions) <= (board_grid / unit_grid) ** 2
    ), "The positions are out of scope!"
    outdir = args["outdir"]
    file_name = args["file_name"]
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    file_1 = open(outdir + file_name + ".mat", "w")
    file_1.close()
    file_2 = open(outdir + file_name + ".jpg", "w")
    file_2.close()
    return None


if __name__ == "__main__":
    main()
