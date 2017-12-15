#!/usr/bin/env python3

import sys
import re
from collections import defaultdict

COMPARISONS = {
	'==': lambda a, b: a == b,
	'!=': lambda a, b: a != b,
	'<' : lambda a, b: a <  b,
	'>' : lambda a, b: a >  b,
	'<=': lambda a, b: a <= b,
	'>=': lambda a, b: a >= b
}

memory = defaultdict(lambda: 0)
maxever = 0

for line in sys.stdin:
	match = re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) (==|!=|<|>|<=|>=) (-?\d+)', line)
	if not match:
		print('Nonmatching: ' + line)
		continue

	ifreg = match.group(4)
	ifop = COMPARISONS[match.group(5)]
	ifval = int(match.group(6))

	if ifop(memory[ifreg], ifval):
		linereg = match.group(1)
		lineval = int(match.group(3))
		if match.group(2) == 'dec':
			lineval = -lineval

		memory[linereg] += lineval
		maxever = max(maxever, memory[linereg])

maxitem = max(memory.items(), key=lambda x: x[1])
print('Max value: ' + repr(maxitem))
print('Max ever: %i' % maxever)
