#!/usr/bin/env python3

import sys

for stream in sys.stdin:
	score = 0
	depth = 0
	is_garbage = False
	is_skipped = False
	offset = 0
	garbage_chars = 0

	for char in stream.strip():
		print('S:%d D:%d G:%d S:%d C:%s' % (score, depth, int(is_garbage), int(is_skipped), char))
		if is_skipped:
			is_skipped = False
		elif char == '!':
			is_skipped = True
		elif is_garbage:
			if char == '>':
				is_garbage = False
			else:
				garbage_chars += 1
		elif char == '{':
			depth += 1
		elif char == '}':
			score += depth
			depth -= 1
		elif char == '<':
			is_garbage = True
		elif char == ',':
			pass
		else:
			raise Exception('Unexpected character "%s" at offset %d' % (char, offset))

		offset += 1

	print('Score: %i' % score)
	print('Garbage chars: %i' % garbage_chars)
