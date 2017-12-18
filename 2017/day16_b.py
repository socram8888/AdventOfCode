#!/usr/bin/env python3

import sys
import re

INITIAL_VALUE = list('abcdefghijklmnop')
ITERATIONS = 1000000000

EXCHANGE_REGEX = re.compile(r'x(\d+)/(\d+)')
PARTNER_REGEX = re.compile(r'p([a-p])/([a-p]+)')
SPLIT_REGEX = re.compile(r's(\d+)')

def do_operation(status, op):
	match = EXCHANGE_REGEX.match(op)
	if match is not None:
		a = int(match.group(1))
		b = int(match.group(2))

		(status[a], status[b]) = (status[b], status[a])
		return status

	match = PARTNER_REGEX.match(op)
	if match is not None:
		a = status.index(match.group(1))
		b = status.index(match.group(2))

		(status[a], status[b]) = (status[b], status[a])
		return status

	match = SPLIT_REGEX.match(op)
	if match is not None:
		a = int(match.group(1))

		return status[-a:] + status[:-a]

	raise Exception('Unknown operation: %s' % repr(op))

for line in sys.stdin:
	operations = line.strip().split(',')

	status = list(INITIAL_VALUE)
	for iteration in range(ITERATIONS):
		for operation in operations:
			status = do_operation(status, operation)

		if status == INITIAL_VALUE:
			print('Cycle size: %d' % iteration)

			for iteration in range(ITERATIONS % (iteration + 1)):
				for operation in operations:
					status = do_operation(status, operation)

			break

	print('Final status: %s' % ''.join(status))