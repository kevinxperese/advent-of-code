#!/Users/kevin/opt/anaconda3/envs/advent-of-code/bin/python
"""Get input data for given year/day of Advent of Code puzzle."""
import argparse
from pathlib import Path
import requests


def main(year: str, day: str) -> None:
    # load session cookie
    COOKIE_PATH = "~/Sandboxes/advent-of-code/utils/session_cookie.txt"
    with open(Path(COOKIE_PATH).expanduser()) as f:
        cookie = f.read().strip()

    # get input data
    url = f"https://adventofcode.com/20{year}/day/{day}/input"
    cookie_dict = {"session" : cookie}
    response = requests.get(url, cookies=cookie_dict)
    input_data = response.text

    # write out input data
    input_dir = f"~/Sandboxes/advent-of-code/20{year}/inputs"
    filename = f"day-{str(day).zfill(2)}.txt"
    input_path = Path(input_dir, filename).expanduser()
    input_path.parent.mkdir(parents=True, exist_ok=True)
    with input_path.open("w") as f:
        f.write(input_data.rstrip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Advent of Code input.")
    parser.add_argument("year", help="last two digits of the AoC year, e.g., '16' for 2016")
    parser.add_argument("day", help="day of the AoC challenge, e.g., '3'")
    args = parser.parse_args()

    main(args.year, args.day)