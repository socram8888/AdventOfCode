#!/usr/bin/env python3

# I love knots so much, this had to have its own file

def knothash(lengths):
	lengths = lengths + bytes([17, 31, 73, 47, 23])

	sparse = list(range(256))
	offset = 0
	skip = 0
	for iteration in range(64):
		for length in lengths:
			for pos in range(length // 2):
				pos_a = (offset + pos) % 256
				pos_b = (offset + length - pos - 1) % 256

				# Swap them
				sparse[pos_a], sparse[pos_b] = sparse[pos_b], sparse[pos_a]

			offset = (offset + length + skip) % 256
			skip = (skip + 1) % 256

	knots = bytearray(16)
	for pos in range(256):
		knots[pos // 16] ^= sparse[pos]

	return knots
