#!/usr/bin/env python3

# --- Part Two ---

# Now, you need to pass through the firewall without being caught - easier said than done.

# You can't control the speed of the packet, but you can delay it any number of picoseconds. For each picosecond you delay the packet before beginning your trip, all security scanners move one step. You're not in the firewall during this time; you don't enter layer 0 until you stop delaying the packet.

# In the example above, if you delay 10 picoseconds (picoseconds 0 - 9), you won't get caught:

# State after delaying:
 # 0   1   2   3   4   5   6
# [ ] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
                # [ ]     [ ]

# Picosecond 10:
 # 0   1   2   3   4   5   6
# ( ) [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
                # [ ]     [ ]

 # 0   1   2   3   4   5   6
# ( ) [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
                # [ ]     [ ]


# Picosecond 11:
 # 0   1   2   3   4   5   6
# [ ] ( ) ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
                # [ ]     [ ]

 # 0   1   2   3   4   5   6
# [S] (S) ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
                # [ ]     [ ]


# Picosecond 12:
 # 0   1   2   3   4   5   6
# [S] [S] (.) ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
                # [ ]     [ ]

 # 0   1   2   3   4   5   6
# [ ] [ ] (.) ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
                # [ ]     [ ]


# Picosecond 13:
 # 0   1   2   3   4   5   6
# [ ] [ ] ... (.) [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
                # [ ]     [ ]

 # 0   1   2   3   4   5   6
# [ ] [S] ... (.) [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
                # [ ]     [ ]


# Picosecond 14:
 # 0   1   2   3   4   5   6
# [ ] [S] ... ... ( ) ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
                # [ ]     [ ]

 # 0   1   2   3   4   5   6
# [ ] [ ] ... ... ( ) ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
                # [S]     [S]


# Picosecond 15:
 # 0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] (.) [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
                # [S]     [S]

 # 0   1   2   3   4   5   6
# [S] [S] ... ... [ ] (.) [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
                # [ ]     [ ]


# Picosecond 16:
 # 0   1   2   3   4   5   6
# [S] [S] ... ... [ ] ... ( )
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
                # [ ]     [ ]

 # 0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... ( )
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
                # [ ]     [ ]

# Because all smaller delays would get you caught, the fewest number of picoseconds you would need to delay to get through safely is 10.

# What is the fewest number of picoseconds that you need to delay the packet to pass through the firewall without being caught?

import sys
import re
from itertools import count

# From https://stackoverflow.com/a/1857860
class SparseList(list):
	def __setitem__(self, index, value):
		missing = index - len(self) + 1
		if missing > 0:
			self.extend([None] * missing)
		list.__setitem__(self, index, value)

	def __getitem__(self, index):
		try:
			return list.__getitem__(self, index)
		except IndexError:
			return None

scanners = SparseList()

for line in sys.stdin:
	match = re.match(r'(\d+)\s*:\s*(\d+)', line)

	pos = int(match.group(1))
	depth = int(match.group(2))

	scanners[pos] = depth

def collides(delay):
	for tick, depth in zip(count(delay), scanners):
		if depth is None:
			continue

		if tick % (2 * depth - 2) == 0:
			return True

	return False

delay = 0
while collides(delay):
	delay += 1

print('Delay: %d' % delay)
