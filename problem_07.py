from collections import defaultdict
from pathlib import Path

input_lines = Path("problem_07.txt").read_text().strip().split("\n")


def get_directory_sizes():
    line_index = 0
    folder = []
    directory_sizes = defaultdict(int)
    while line_index < len(input_lines):
        line = input_lines[line_index]
        if line == "$ cd ..":
            folder.pop()
            line_index += 1
            continue
        if line.startswith("$ cd"):
            folder.append(line.replace("$ cd ", ""))
            line_index += 1
            continue
        if line == "$ ls":
            line_index += 1
            while (
                line_index < len(input_lines) and not
                (line := input_lines[line_index]).startswith("$")
            ):
                if not line.startswith("dir"):  
                    file_size = int(line.split()[0])
                    for folder_index in range(len(folder)):
                        directory_sizes[tuple(folder[:folder_index+1])] += file_size
                line_index += 1
        else:
            raise ValueError(f"Unexpected line {line}")

    return directory_sizes


def part_a():
    return sum(size for size in get_directory_sizes().values() if size <= 100_000)


print(part_a())

DISK_SIZE = 70_000_000
REQUIRED_FREE = 30_000_000


def part_b():
    directory_sizes = get_directory_sizes()
    currently_free = DISK_SIZE - directory_sizes[("/",)]
    target = REQUIRED_FREE - currently_free
    return min(size for size in directory_sizes.values() if size >= target)


print(part_b())
