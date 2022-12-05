from collections import defaultdict, deque
from pathlib import Path
import re
from typing import Generator

input_text = Path("problem_05.txt").read_text()
diagram_text, moves_text = input_text.split("\n\n")
moves_text = moves_text.strip()

REGEX = re.compile("move (\d+) from (\d) to (\d)")


def parse_diagram():
    stacks = defaultdict(deque)
    diagram_lines = diagram_text.split("\n")[:-1][::-1]
    # No final space on the last column
    num_cols = (len(diagram_lines[0]) + 1) // 4

    for line in diagram_lines:
        for col_index in range(num_cols):
            letter = line[(col_index * 4) + 1]
            if letter != " ":
                stacks[col_index + 1].append(letter)

    return stacks


def get_moves() -> Generator[tuple[int, int, int], None, None]:
    for move in moves_text.split("\n"):
        parsed = REGEX.fullmatch(move)
        amount, start, end = [int(x) for x in parsed.group(1, 2, 3)]
    yield (amount, start, end)


def part_a():
    stacks = parse_diagram()
    for amount, start, end in get_moves():
        for _ in range(amount):
            letter = stacks[start].pop()
            stacks[end].append(letter)

    return "".join(stack[-1] for stack in stacks.values())


print(part_a())


def part_b():
    stacks = parse_diagram()
    for amount, start, end in get_moves():
        staging = deque()
        for _ in range(amount):
            letter = stacks[start].pop()
            staging.append(letter)
        while staging:
            stacks[end].append(staging.pop())

    return "".join(stack[-1] for stack in stacks.values())


print(part_b())
