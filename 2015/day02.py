#!/usr/bin/env python3

import sys

area = 0
ribbon = 0

for line in sys.stdin:
	# Cuboid size
	a, b, c = sorted([int(x) for x in line.strip().split('x')])
	faces = (a * b, b * c, a * c)

	# Add area plus slack
	area += 2 * sum(faces) + faces[0]

	# Add ribbon
	ribbon += 2 * a + 2 * b + a * b * c

print('Area: %d' % area)
print('Ribbon: %d' % ribbon)
