#!/usr/bin/env python3

# --- Day 4: High-Entropy Passphrases ---

# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

    # aa bb cc dd ee is valid.
    # aa bb cc dd aa is not valid - the word aa appears more than once.
    # aa bb cc dd aaa is valid - aa and aaa count as different words.

# The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

import sys

valid = 0
for passphrase in sys.stdin:
	words = passphrase.split()

	if len(words) == 0:
		continue

	words.sort()
	last = words[0]
	for word in words[1:]:
		if word == last:
			break
		last = word
	else:
		valid += 1

print(valid)
