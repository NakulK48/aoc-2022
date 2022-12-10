from pathlib import Path

input_lines = Path("problem_10.txt").read_text().strip().split("\n")

KEY_CYCLES = (20, 60, 100, 140, 180, 220)

def get_cycle_register_values():
    # 0-indexed!
    cycle_register_values = []
    value = 1
    for line in input_lines:
        if line.startswith("addx "):
            cycle_register_values.append(value)
            cycle_register_values.append(value)
            to_add = int(line.replace("addx ", ""))
            value += to_add
        else:
            cycle_register_values.append(value)
    return cycle_register_values


def part_a():
    cycle_register_values = get_cycle_register_values()
    return sum(
        cycle * cycle_register_values[cycle - 1]
        for cycle in KEY_CYCLES
    )

print(part_a())


NUM_ROWS = 6
NUM_COLS = 40

def part_b():
    pixels = [[" " for _ in range(NUM_COLS)] for __ in range(NUM_ROWS)]
    cycle_register_values = get_cycle_register_values()
    for row_num, row in enumerate(pixels):
        for col_num in range(len(row)):
            cycle = (row_num * NUM_COLS) + col_num
            cycle_value = cycle_register_values[cycle]
            if cycle_value - 1 <= col_num <= cycle_value + 1:
                pixels[row_num][col_num] = "X"
    for row in pixels:
        print(" ".join(row))

part_b()
