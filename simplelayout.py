import argparse
import os
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--board_grid", type=int, default=100, help="layout pixel")
ap.add_argument("--unit_grid", type=int, default=10, help="rectangle pixel")
ap.add_argument("--unit_n", type=int, default=5, help="number of rectangles")
ap.add_argument("--positions", nargs='+', type=int, default=1, help="number of rectangles")
ap.add_argument("-o", "--outdir", type=str, default='example_dir/', help="rectangle point order number")
ap.add_argument("--file_name", type=str, default='example', help="the saved file name")
args = vars(ap.parse_args())


def main():
    board_grid = args['board_grid']
    unit_grid = args['unit_grid']
    assert board_grid % unit_grid == 0, "The board_graid cannot be devide by unit_grid!"
    unit_n = args['unit_n']
    positions = args['positions']
    assert (min(positions) >= 1) & (max(positions) <= (board_grid/unit_grid)**2), "The positions are out of scope!"
    outdir = args['outdir']
    file_name = args['file_name']
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    file_1 = open(outdir + file_name + '.mat', 'w')
    file_1.close()
    file_2 = open(outdir + file_name + '.jpg', 'w')
    file_2.close()
    return None


if __name__ == "__main__":
    main()
