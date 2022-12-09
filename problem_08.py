from dataclasses import dataclass
from pathlib import Path

input_text = Path("problem_08.txt").read_text().strip()
input_grid = [[int(x) for x in line] for line in input_text.split("\n")]


@dataclass(frozen=True)
class Tree:
    row: int
    col: int
    height: int


def visible_from_start(trees: list[Tree]):
    largest_so_far = -1
    visible = set()
    for tree in trees:
        if tree.height > largest_so_far:
            largest_so_far = tree.height
            visible.add((tree.row, tree.col))
    return visible


def part_a():
    visible = set()
    for row_num, row in enumerate(input_grid):
        row_trees = [Tree(row_num, col_num, height) for col_num, height in enumerate(row)]
        visible |= visible_from_start(row_trees)
        visible |= visible_from_start(row_trees[::-1])
    for col_num in range(len(input_grid[0])):
        col_trees = [
            Tree(
                row_num,
                col_num,
                input_grid[row_num][col_num],
            )
            for row_num in range(len(input_grid))
        ]
        visible |= visible_from_start(col_trees)
        visible |= visible_from_start(col_trees[::-1])
    return len(visible)


print(part_a())


def count_visible_trees(tree_heights: list[int], start_height: int):
    num_visible = 0  # noqa: SIM113
    for tree_height in tree_heights:
        num_visible += 1
        if tree_height >= start_height:
            break
    return num_visible


def part_b():
    max_score = 0
    for row_num in range(len(input_grid)):
        for col_num in range(len(input_grid[0])):
            height = input_grid[row_num][col_num]
            left_heights = input_grid[row_num][:col_num][::-1]
            right_heights = input_grid[row_num][col_num+1:]
            up_heights = [row[col_num] for row in input_grid[:row_num]][::-1]
            down_heights = [row[col_num] for row in input_grid[row_num+1:]]
            current_score = 1
            for heights in (left_heights, right_heights, up_heights, down_heights):
                current_score *= count_visible_trees(heights, height)
            max_score = max(max_score, current_score)
    return max_score


print(part_b())
