#!/usr/bin/env python3

# --- Part Two ---

# Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

# Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

# How many steps does it now take to reach the exit?

import sys

memory = [int(line) for line in sys.stdin]
pc = 0
steps = 0

while pc >= 0 and pc < len(memory):
	old_pc = pc
	pc += memory[pc]

	memory[old_pc] += (1 if memory[old_pc] < 3 else -1)
	steps += 1

print(steps)
