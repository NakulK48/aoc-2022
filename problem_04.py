from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path


input_text = Path("problem_04.txt").read_text().strip()
lines = input_text.split("\n")


@dataclass
class Interval:
    start: int
    end: int

    @staticmethod
    def from_string(raw: str) -> "Interval":
        raw_start, raw_end = raw.split("-")
        return Interval(int(raw_start), int(raw_end))

    def contains(self, other: "Interval") -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "Interval") -> bool:
        return (
            (other.start <= self.end <= other.end)
            or (other.start <= self.start <= other.end)
            or self.contains(other)
            or other.contains(self)
        )


def get_intervals() -> Generator[tuple[Interval, Interval], None, None]:
    for line in lines:
        raw1, raw2 = line.split(",")
        yield (Interval.from_string(raw1), Interval.from_string(raw2))


def part_a():
    return sum(1 for int1, int2 in get_intervals() if int1.contains(int2) or int2.contains(int1))


print(part_a())


def part_b():
    return sum(1 for int1, int2 in get_intervals() if int1.overlaps(int2))


print(part_b())
