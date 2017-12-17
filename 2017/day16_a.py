#!/usr/bin/env python3

import sys
import re

def do_operation(status, op):
	match = re.match(r'x(\d+)/(\d+)', op)
	if match is not None:
		a = int(match.group(1))
		b = int(match.group(2))

		(status[a], status[b]) = (status[b], status[a])
		return status

	match = re.match(r'p([a-p])/([a-p]+)', op)
	if match is not None:
		a = status.index(match.group(1))
		b = status.index(match.group(2))

		(status[a], status[b]) = (status[b], status[a])
		return status

	match = re.match(r's(\d+)', op)
	if match is not None:
		a = int(match.group(1))

		return status[-a:] + status[:-a]

	raise Exception('Unknown operation: %s' % repr(op))

for line in sys.stdin:
	status = list('abcdefghijklmnop')
	#status = list('abcde')

	for operation in line.strip().split(','):
		status = do_operation(status, operation)

	print('Status: %s' % ''.join(status))
