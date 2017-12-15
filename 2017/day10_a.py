#!/usr/bin/env python3

import sys

HASH_LEN = 256

for line in sys.stdin:
	lengths = [int(x) for x in line.strip().split(",")]
	
	knots = list(range(HASH_LEN))
	skip = 0
	offset = 0
	for length in lengths:
		print('Len: %d' % length)
		for i in range(length // 2):
			pos_a = (offset + i) % HASH_LEN
			pos_b = (offset + length - i - 1) % HASH_LEN
			print('Swap %d <-> %d' % (pos_a, pos_b))

			# Swap them
			knots[pos_a], knots[pos_b] = knots[pos_b], knots[pos_a]

		offset = (offset + length + skip) % HASH_LEN
		skip = (skip + 1) % HASH_LEN

		print('Status: %s' % repr(knots))

	print('Final: %s' % repr(knots))
