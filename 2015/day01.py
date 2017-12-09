#!/usr/bin/env python3

import sys

for line in sys.stdin:
	depth = 0
	offset = 0
	basement_offset = -1

	for char in line:
		if char == '(':
			depth += 1
		elif char == ')':
			depth -= 1

		offset += 1
		if depth < 0 and basement_offset < 0:
			basement_offset = offset

	print('Depth: %d' % depth)
	print('Basement: %d' % basement_offset)
