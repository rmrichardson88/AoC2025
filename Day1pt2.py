from aoc_input import read_lines


def run_commands_part2(commands: list[str], size: int = 100) -> int:
    """
    Execute the commands on a circular dial and count how many times the dial
    passes 0.
    """
    pos = 50
    password = 0

    for cmd in commands:
        cmd = cmd.strip()
        if not cmd:
            continue

        direction = cmd[0]
        amount = int(cmd[1:])

        step = 1 if direction == "R" else -1

        for _ in range(amount):
            pos = (pos + step) % size
            if pos == 0:
                password += 1

    return password


if __name__ == "__main__":
    commands = read_lines(1)
    password = run_commands_part2(commands)
    print("Number of commands run:", len(commands))
    print("Total rollovers (password):", password)
