from pathlib import Path

input_text = Path("problem_01.txt").read_text().strip()

def get_elf_nums():
    elf_texts = input_text.split("\n\n")
    return (
        sum(int(x) for x in elf_text.split("\n"))
        for elf_text in elf_texts
    )


def part_a():
    return max(get_elf_nums())


print(part_a())

def part_b():
    sorted_elf_nums = sorted(list(get_elf_nums()))
    return sum(sorted_elf_nums[-3:])

print(part_b())
