#!/usr/bin/env python3

import sys

for line in sys.stdin:
	x = y = 0
	visited = set([(0, 0)])

	for char in line:
		if char == '^':
			y += 1
		elif char == 'v':
			y -= 1
		elif char == '<':
			x -= 1
		elif char == '>':
			x += 1

		visited.add((x, y))

	print('Houses: %d' % len(visited))
