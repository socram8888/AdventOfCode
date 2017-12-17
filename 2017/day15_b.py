#!/usr/bin/env python3

status_a = int(input('Generator A start value: '))
status_b = int(input('Generator B start value: '))

matching = 0
for iteration in range(5 * 1000 * 1000):
	if iteration % (1000 * 1000) == 0:
		print(iteration)

	status_a = (status_a * 16807) % 2147483647
	while (status_a & 3) != 0:
		#print('Fail A: %d' % status_a)
		status_a = (status_a * 16807) % 2147483647

	status_b = (status_b * 48271) % 2147483647
	while (status_b & 7) != 0:
		#print('Fail B: %d' % status_b)
		status_b = (status_b * 48271) % 2147483647

	#print("%d %d" % (status_a, status_b))
	if (status_a & 0xFFFF) == (status_b & 0xFFFF):
		matching += 1

print('Matching: %d' % matching)
