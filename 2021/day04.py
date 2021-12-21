#!/usr/bin/env python

from __future__ import annotations

from typing import NamedTuple

class Board(NamedTuple):
	left: set[int]
	ints: list[int]

	@property
	def has_won(self) -> bool:
		for i in range(5):
			for j in range(5):
				if self.ints[i * 5 + j] in self.left:
					break
			else:
				return True

			for j in range(5):
				if self.ints[i + 5 * j] in self.left:
					break
			else:
				return True
		return False

	@classmethod
	def parse(cls, board: str) -> Board:
		ints = [int(s) for s in board.split()]
		left = set(ints)
		return cls(left, ints)


# read input
with open('./inputs/day04.txt') as filehandle:
	INPUT_S = filehandle.read()

first, *rest = INPUT_S.split('\n\n')
boards = [Board.parse(board) for board in rest]
ints = [int(s) for s in first.split(',')]

def part1_get_number() -> int:
	for number in ints:
		for board in boards:
			board.left.discard(number)

		for board in boards:
			if board.has_won:
				return sum(board.left) * number

	raise AssertionError('unreachable')


def part2_get_number() -> int:
	last_winner = -1
	seen = set()
	for number in ints:
		for board in boards:
			board.left.discard(number)

		for i, board in enumerate(boards):
			if i not in seen and board.has_won:
				last_winner = sum(board.left) * number
				seen.add(i)

	return last_winner

print(part1_get_number())
print(part2_get_number())