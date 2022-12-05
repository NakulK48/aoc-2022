from pathlib import Path

input_text = Path("problem_03.txt").read_text().strip()

def get_priority(shared: str) -> int:
    if shared.isupper():
        return (ord(shared) - ord("A")) + 27
    else:
        return (ord(shared) - ord("a")) + 1

def part_a():
    score = 0
    for line in input_text.split("\n"):
        halfway = len(line) // 2
        first = set(line[:halfway])
        second = set(line[halfway:])
        [shared] = list(first & second)
        score += get_priority(shared)
    return score

print(part_a())

def part_b():
    lines = input_text.split("\n")
    score = 0
    for index in range(0, len(lines), 3):
        (first, second, third) = lines[index:index+3]
        [shared] = list(set(first) & set(second) & set(third))
        score += get_priority(shared)
    return score

print(part_b())
