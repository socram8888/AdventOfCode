#!/usr/bin/env python3

import sys

ITERATIONS = 50000000

for line in sys.stdin:
	step = int(line)

	second_value = -1
	pos = 0
	for num in range(1, ITERATIONS):
		pos = (step + pos + 1) % num
		if pos == 0:
			second_value = num

	print('Value after 0: %d' % second_value)
