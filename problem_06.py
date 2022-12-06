from pathlib import Path


input_text = Path("problem_06.txt").read_text().strip()


def get_index(buffer_length: int):
    for start_index in range(len(input_text) - buffer_length):
        sequence = input_text[start_index : start_index + buffer_length]
        if len(set(sequence)) == buffer_length:
            return start_index + buffer_length


def part_a():
    return get_index(4)


print(part_a())


def part_b():
    return get_index(14)


print(part_b())
