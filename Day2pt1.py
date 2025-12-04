from aoc_input import read_lines

def parse_ranges(lines: list[str]) -> list[int]:
    all_ids: list[int] = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        for part in parts:
            part = part.strip()
            if not part:
                continue

            start_str, end_str = part.split("-", 1)
            start = int(start_str)
            end = int(end_str)

            all_ids.extend(range(start, end + 1))

    return all_ids


def id_repeats(product_id: int) -> bool:
    s = str(product_id)

    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


def sum_invalid_ids(ids: list[int]) -> int:
    total = 0

    for product_id in ids:
        if id_repeats(product_id):
            total += product_id

    return total



if __name__ == "__main__":
    ranges = read_lines(2)
    ids = parse_ranges(ranges)
    invalid_sum = sum_invalid_ids(ids)
    print(ranges, "\nTotal invalid ids:", invalid_sum)