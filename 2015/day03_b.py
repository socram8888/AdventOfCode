#!/usr/bin/env python3

import sys

def do_step(pos, char):
	x, y = pos

	if char == '^':
		y += 1
	elif char == 'v':
		y -= 1
	elif char == '<':
		x -= 1
	elif char == '>':
		x += 1

	return x, y

for line in sys.stdin:
	santa = robo = (0, 0)
	is_robo = False
	visited = set([santa])

	for char in line:
		if is_robo:
			robo = do_step(robo, char)
			visited.add(robo)
		else:
			santa = do_step(santa, char)
			visited.add(santa)

		is_robo = not is_robo

	print('Houses: %d' % len(visited))
