#!/Users/kevin/opt/anaconda3/envs/advent-of-code/bin/python
import argparse
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import sys
from typing import List


def make_url(year: str, day: str) -> str:
    return f"https://adventofcode.com/20{year}/day/{day}"


def get_day_label(url: str) -> str:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching URL {url}: {e}") from e

    soup = BeautifulSoup(resp.content, "html.parser")
    h2 = soup.find("h2")
    if not h2:
        raise ValueError("Could not find <h2> on page for day label.")
    text = h2.get_text(strip=True)
    if "--- Day" not in text:
        raise ValueError(f"Unexpected day label format: {text!r}")
    return text  # e.g. '--- Day 3: Title ---'


def load_template() -> List[str]:
    utils_path = Path("~/Sandboxes/advent-of-code/utils").expanduser()
    template_path = utils_path / "template.ipynb"
    return template_path.read_text(encoding="utf-8")


def edit_template(template: str, day_label: str, url: str, day: str) -> str:
    template = template.replace("{{DAY_LABEL}}", f"{day_label}")
    template = template.replace("{{URL}}", url)
    template = template.replace("{{DAY}}", day.zfill(2))
    return template


def write_notebook_file(year: str, day: str, edited_template: str) -> None:
    notebook_dir = Path(f"~/Sandboxes/advent-of-code/20{year}/notebooks").expanduser()
    notebook_dir.mkdir(parents=True, exist_ok=True)
    filename = f"day-{day.zfill(2)}.ipynb"
    notebook_path = notebook_dir / filename

    if notebook_path.exists():
        raise FileExistsError(f"Notebook already exists: {notebook_path}")

    notebook_path.write_text(edited_template, encoding="utf-8")


def main(year: str, day: str) -> None:
    url = make_url(year, day)
    day_label = get_day_label(url)
    template_lines = load_template()
    edited_template = edit_template(template_lines, day_label, url, day)
    write_notebook_file(year, day, edited_template)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create AoC notebook from template.")
    parser.add_argument("year", help="last two digits of the AoC year, e.g., '16' for 2016")
    parser.add_argument("day", help="day of the AoC challenge, e.g., '3'")
    args = parser.parse_args()

    try:
        main(args.year, args.day)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
