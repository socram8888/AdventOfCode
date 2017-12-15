#!/usr/bin/env python3

import sys
import hashlib

while True:
	prefix = input('Prefix: ').strip()
	zeros = int(input('Zeros: '))
	num = 0

	while True:
		inp = '%s%d' % (prefix, num)
		inp = inp.encode('ascii')

		md = hashlib.md5()
		md.update(inp)
		md = md.hexdigest()

		if md[:zeros] == "0" * zeros:
			break
		else:
			num += 1

	print('Num: %d' % num)