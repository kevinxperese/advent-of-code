#!/Users/kevin/opt/anaconda3/envs/advent-of-code/bin/python
import argparse
import sys
import get_input
import make_nb


parser = argparse.ArgumentParser(description="Set up AoC notebook and download input data.")
parser.add_argument("year", help="last two digits of the AoC year, e.g., '16' for 2016")
parser.add_argument("day", help="day of the AoC challenge, e.g., '3'")
args = parser.parse_args()

try:
    get_input.main(args.year, args.day)
    make_nb.main(args.year, args.day)
except Exception as e:
    print(f"Unexpected error: {e}", file=sys.stderr)
    sys.exit(1)
