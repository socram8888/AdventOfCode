#!/usr/bin/env python3

import sys

for line in sys.stdin:
	moves = line.strip().split(',')
	x = y = 0
	most_far = 0

	for move in moves:
		if move == 'n':
			y += 1
		elif move == 's':
			y -= 1
		else:
			offset = x & 1
			if move[0] == 'n':
				y += offset
			elif move[0] == 's':
				y -= 1 - offset
			else:
				raise Exception('Invalid direction: %s' % repr(move))

			if move[1] == 'w':
				x -= 1
			elif move[1] == 'e':
				x += 1
			else:
				raise Exception('Invalid direction: %s' % repr(move))

		steps = x + max(y - x // 2, 0)
		most_far = max(steps, most_far)

	print('Final position X: %d, Y: %d' % (x, y))
	print('Steps required: %d' % steps)
	print('Most far: %d' % most_far)
