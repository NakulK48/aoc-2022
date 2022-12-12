from dataclasses import dataclass
from pathlib import Path
from typing import Callable
import yaml

import numexpr


@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    test: Callable[[int], bool]
    true_target: int
    false_target: int
    num_inspected: int = 0


input_text = Path("problem_11.txt").read_text()
loaded = yaml.safe_load(input_text)

MONKEYS: list[Monkey] = []


for entry in loaded.values():
    items = [int(x) for x in entry["Starting items"].split(", ")]
    divisor = int((entry["Test"].replace("divisible by ", "")))
    operation = entry["Operation"].replace("new = ", "")
    MONKEYS.append(
        Monkey(
            items=items,
            operation=lambda x, op=operation: numexpr.evaluate(op.replace("old", str(x))),
            test=lambda x, divisor=divisor: not (x % divisor),
            true_target=int(entry["If true"].replace("throw to monkey ", "")),
            false_target=int(entry["If false"].replace("throw to monkey ", "")),
        )
    )


def part_a():
    for _ in range(20):
        for monkey in MONKEYS:
            for worry in monkey.items:
                monkey.num_inspected += 1
                new_worry = monkey.operation(worry) // 3
                if monkey.test(new_worry):
                    MONKEYS[monkey.true_target].items.append(new_worry)
                else:
                    MONKEYS[monkey.false_target].items.append(new_worry)
            monkey.items = []

    for monkey in MONKEYS:
        print(monkey.num_inspected)

    sorted_monkeys = sorted(MONKEYS, key=lambda x: x.num_inspected)
    return sorted_monkeys[-1].num_inspected * sorted_monkeys[-2].num_inspected


print(part_a())
