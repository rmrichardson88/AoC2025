from __future__ import annotations
import os
from pathlib import Path
import requests

def fetch_input(day: int, year: int = 2025, refresh: bool = False) -> str:
    """
    Fetch AoC input for the given day.

    - Uses local cache in inputs/dayXX.txt by default.
    - If refresh=True, refetches from the website.
    """
    cache_dir = Path("inputs")
    cache_dir.mkdir(exist_ok=True)
    cache_file = cache_dir / f"day{day:02d}.txt"

    if cache_file.exists() and not refresh:
        return cache_file.read_text().rstrip("\n")

    session = os.environ.get("AOC_SESSION")
    if not session:
        raise RuntimeError(
            "Environment variable AOC_SESSION is not set. "
            "Set it to your Advent of Code session cookie value."
        )

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    resp = requests.get(url, cookies={"session": session})
    resp.raise_for_status()

    text = resp.text.rstrip("\n")
    cache_file.write_text(text)
    return text


def read_lines(day: int, year: int = 2025, refresh: bool = False) -> list[str]:
    """Convenience: returns input as a list of lines."""
    return fetch_input(day, year=year, refresh=refresh).splitlines()


if __name__ == "__main__":
    lines = read_lines(1)
    print(f"Got {len(lines)} lines")
    print("First few:", lines[:5])
