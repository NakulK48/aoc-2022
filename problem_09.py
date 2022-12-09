from dataclasses import dataclass
from pathlib import Path


def parse_line(line: str):
    direction, distance_str = line.split()
    return (direction, int(distance_str))


input_text = Path("problem_09.txt").read_text().strip()
input_pairs = [parse_line(line) for line in input_text.split("\n")]


@dataclass(frozen=True)
class Position:
    x: int
    y: int


def get_new_tail_pos(head_pos: Position, tail_pos: Position):
    x_diff = head_pos.x - tail_pos.x
    y_diff = head_pos.y - tail_pos.y

    if x_diff < -1 or (x_diff == -1 and abs(y_diff) > 1):
        new_x = tail_pos.x - 1
    elif x_diff > 1 or (x_diff == 1 and abs(y_diff) > 1):
        new_x = tail_pos.x + 1
    else:
        new_x = tail_pos.x

    if y_diff < -1 or (y_diff == -1 and abs(x_diff) > 1):
        new_y = tail_pos.y - 1
    elif y_diff > 1 or (y_diff == 1 and abs(x_diff) > 1):
        new_y = tail_pos.y + 1
    else:
        new_y = tail_pos.y

    return Position(new_x, new_y)


def part_a():
    tail_visited = set()
    head_pos = Position(0, 0)
    tail_pos = Position(0, 0)
    for (direction, distance) in input_pairs:
        for _ in range(distance):
            if direction == "R":
                head_pos = Position(head_pos.x + 1, head_pos.y)
            elif direction == "L":
                head_pos = Position(head_pos.x - 1, head_pos.y)
            elif direction == "U":
                head_pos = Position(head_pos.x, head_pos.y + 1)
            elif direction == "D":
                head_pos = Position(head_pos.x, head_pos.y - 1)
            else:
                raise ValueError(f"Invalid direction {direction}")
            tail_pos = get_new_tail_pos(head_pos, tail_pos)
            tail_visited.add(tail_pos)
    return len(tail_visited)


print(part_a())


def part_b():
    tail_visited = set()
    positions = [Position(0, 0) for _ in range(10)]
    for (direction, distance) in input_pairs:
        for _ in range(distance):
            head_pos = positions[0]
            if direction == "R":
                head_pos = Position(head_pos.x + 1, head_pos.y)
            elif direction == "L":
                head_pos = Position(head_pos.x - 1, head_pos.y)
            elif direction == "U":
                head_pos = Position(head_pos.x, head_pos.y + 1)
            elif direction == "D":
                head_pos = Position(head_pos.x, head_pos.y - 1)
            else:
                raise ValueError(f"Invalid direction {direction}")
            positions[0] = head_pos
            for i in range(1, len(positions)):
                positions[i] = get_new_tail_pos(positions[i - 1], positions[i])
            tail_visited.add(positions[-1])
    return len(tail_visited)


print(part_b())
