import argparse
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--board_grid", type=int, help="layout pixel")
    ap.add_argument("--unit_grid", type=int, help="rectangle pixel")
    ap.add_argument("--unit_n", type=int, help="number of rectangles")
    ap.add_argument(
        "--positions", nargs="+", type=int, help="positions of rectangles"
    )
    ap.add_argument(
        "-o",
        "--outdir",
        type=str,
        default="example_dir1/example_dir2",
        help="rectangle point order number",
    )
    ap.add_argument(
        "--file_name", type=str, default="example", help="saved file name"
    )
    args = vars(ap.parse_args())
    board_grid = args["board_grid"]
    unit_grid = args["unit_grid"]
    if board_grid % unit_grid != 0:
        print("board_grid must be devided by unit_grid!")
        exit(0)
    unit_n = args["unit_n"]
    positions = args["positions"]
    if len(positions) != unit_n:
        print("position number isnot equal to unit_n!")
        exit(0)
    upper_bound = (board_grid / unit_grid) ** 2
    if (min(positions) < 1) or (max(positions) > upper_bound):
        print("position must be in [1, (board_grid / unit_grid) ** 2]")
        exit(0)
    outdir = args["outdir"]
    file_name = args["file_name"]
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    file_1 = open(outdir + '/' + file_name + ".mat", "w")
    file_1.close()
    file_2 = open(outdir + '/' + file_name + ".jpg", "w")
    file_2.close()
    return None


if __name__ == "__main__":
    main()
