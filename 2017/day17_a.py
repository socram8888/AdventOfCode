#!/usr/bin/env python3

import sys

ITERATIONS = 2018

for line in sys.stdin:
	step = int(line)

	status = [0]
	pos = 0
	for num in range(1, ITERATIONS):
		pos = (step + pos + 1) % len(status)
		status = status[:pos+1] + [num] + status[pos+1:]

	print(status)
	print('Value after 2017: %d' % status[(pos+2) % len(status)])
