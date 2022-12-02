from pathlib import Path
from collections.abc import Generator

input_text = Path("problem_02.txt").read_text().strip()


class Move:
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def from_opp(letter: str) -> "Move":
        return Move(ord(letter) - ord("A"))

    @staticmethod
    def from_me(letter: str) -> "Move":
        return Move(ord(letter) - ord("X"))

    def own_score(self) -> int:
        return self.value + 1

    def score(self, other: "Move") -> int:
        # 1 higher means you win; 1 lower means you lose
        diff = (self.value - other.value) % 3
        return {0: 3, 1: 6, 2: 0}[diff]

    def get_move(self, strategy: str) -> "Move":
        new_moves = {"X": self.value - 1, "Y": self.value, "Z": self.value + 1}
        return Move(new_moves[strategy] % 3)


def input_pairs() -> Generator[tuple[str, str], None, None]:
    for line in input_text.split("\n"):
        yield line.split(" ")


def input_moves() -> Generator[tuple[str, str], None, None]:
    for (raw_opp, raw_my) in input_pairs():
        yield Move.from_opp(raw_opp), Move.from_me(raw_my)


def part_a():
    score = 0
    for opp_move, my_move in input_moves():
        score += my_move.own_score() + my_move.score(opp_move)
    return score


print(part_a())


def part_b():
    score = 0
    for opp_move_raw, strategy in input_pairs():
        opp_move = Move.from_opp(opp_move_raw)
        my_move = opp_move.get_move(strategy)
        score += my_move.own_score() + my_move.score(opp_move)
    return score


print(part_b())
