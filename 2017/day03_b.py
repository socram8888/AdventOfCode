#!/usr/bin/env python3

# --- Part Two ---

# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

# So, the first few squares' values are chosen as follows:

# Square 1 starts with the value 1.
# Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
# Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
# Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
# What is the first value written that is larger than your puzzle input?

import sys

class Direction:
	def __init__(self, name, steps):
		self.name = name
		self.steps = steps
		
	def increment(self, pos):
		return (pos[0] + self.steps[0], pos[1] + self.steps[1])

MATRIX_SIDE = 15
DIRECTIONS = [
	Direction("East",  (+1, 0)),
	Direction("North", (0, -1)),
	Direction("West",  (-1, 0)),
	Direction("South", (0, +1))
]

for target in sys.stdin:
	target = int(target)

	pos = (MATRIX_SIDE // 2, ) * 2
	matrix = [[0] * MATRIX_SIDE for x in range(MATRIX_SIDE)]
	matrix[pos[1]][pos[0]] = cellsum = 1

	direction = 0
	direction_steps = 1
	turns_until_increase = 2
	steps_per_direction = 1

	while cellsum < target:
		print('%s %i %s %i %i %i' % (repr(pos), cellsum, DIRECTIONS[direction].name, direction_steps, turns_until_increase, steps_per_direction))
		pos = DIRECTIONS[direction].increment(pos)
		direction_steps -= 1
		if direction_steps == 0:
			turns_until_increase -= 1
			if turns_until_increase == 0:
				steps_per_direction += 1
				turns_until_increase = 2

			direction_steps = steps_per_direction
			direction = (direction + 1) % 4

		cellsum = 0
		for y_rel in [-1, 0, 1]:
			for x_rel in [-1, 0, 1]:
				cellsum += matrix[pos[1] + y_rel][pos[0] + x_rel]
						
		matrix[pos[1]][pos[0]] = cellsum

	print('%s %i %s %i %i %i' % (repr(pos), cellsum, DIRECTIONS[direction].name, direction_steps, turns_until_increase, steps_per_direction))
