from aoc_input import read_lines

def run_commands(commands: list[str], size: int = 100) -> int:
    """
    Return password, where password is how many times the dial is left pointing at 0 after a rotation.
    """
    pos = 50 
    password = 0

    for cmd in commands:
        cmd = cmd.strip()
        if not cmd:
            continue

        direction = cmd[0]
        amount = int(cmd[1:])

        step = amount if direction == "R" else -amount

        pos = (pos + step) % size

        if pos == 0:
            password += 1

    return password


if __name__ == "__main__":
    commands = read_lines(1)
    password = run_commands(commands)
    print(
        "Number of times the dial is left pointing at 0 (password):",
        password,
    )