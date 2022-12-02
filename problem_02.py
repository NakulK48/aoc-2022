from pathlib import Path

input_text = Path("problem_02.txt").read_text().strip()


def input_pairs():
    for line in input_text.split("\n"):
        yield line.split(" ")


SCORES = {"X": 1, "Y": 2, "Z": 3}
WIN_PAIRS = {("A", "Y"), ("B", "Z"), ("C", "X")}
DRAW_PAIRS = {("A", "X"), ("B", "Y"), ("C", "Z")}
LOSE_PAIRS = {("A", "Z"), ("B", "X"), ("C", "Y")}

SCORE_BY_PAIR = {
    **{win_pair: 6 for win_pair in WIN_PAIRS},
    **{draw_pair: 3 for draw_pair in DRAW_PAIRS},
    **{lose_pair: 0 for lose_pair in LOSE_PAIRS},
}


def part_a():
    score = 0
    for opp_move, my_move in input_pairs():
        score += SCORES[my_move] + SCORE_BY_PAIR[(opp_move, my_move)]
    return score


print(part_a())


SCORES_B = {"X": 0, "Y": 3, "Z": 6}
ROCK_PAIRS = {("A", "Y"), ("B", "X"), ("C", "Z")}
PAPER_PAIRS = {("A", "Z"), ("B", "Y"), ("C", "X")}
SCISSORS_PAIRS = {("A", "X"), ("B", "Z"), ("C", "Y")}

SCORE_BY_PAIR_B = {
    **{pair: 1 for pair in ROCK_PAIRS},
    **{pair: 2 for pair in PAPER_PAIRS},
    **{pair: 3 for pair in SCISSORS_PAIRS},
}


def part_b():
    score = 0
    for opp_move, my_move in input_pairs():
        score += SCORES_B[my_move] + SCORE_BY_PAIR_B[(opp_move, my_move)]
    return score


print(part_b())
