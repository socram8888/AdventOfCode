#!/usr/bin/env python3

import sys
from math import sqrt, ceil

for address in sys.stdin:
	address = int(address)

	# This machine's memory is a matrix whose size is increased by one in each
	# direction (up, down, left and right) whenever it runs out of memory
	#
	# In iteration 0, we have only the center cell, so the matrix's size is 1x1
	# In iteration 1, the matrix size is 3x3. Iteration 2, 5x5. Iteration 3, 7x7...
	#
	# Thus, we can define the matrix size, or number of addresses, to be a=(2i+1)^2 for iteration i
	# Solving the above equation for "i", we get that i=(sqrt(a)-1)/2
	#
	# This means that an address "a" will appear in iteration i=ceil((sqrt(a)-1)/2)
	iteration = ceil((sqrt(address) - 1) / 2)

	# We'll substract the previous iteration matrix size, and substract it from the address,
	# converting the address to a 0-based offset from previous iteration size
	offset = address - (2 * iteration - 1) ** 2 - 1

	# Empirically, I've observed that the offset can now be divided in eight parts (from 1 to 8),
	# with even and odd parts having a different way of calculating the number of steps
	even = (offset // iteration) % 2 == 0

	# See day03.jpg for an explanation of these
	if even:
		steps = 2 * iteration - offset % iteration - 1
	else:
		steps = iteration + offset % iteration + 1

	print(steps)
