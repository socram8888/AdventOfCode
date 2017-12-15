#!/usr/bin/env python3

# --- Part Two ---

# For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

# For example:

    # abcde fghij is a valid passphrase.
    # abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    # a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    # iiii oiii ooii oooi oooo is valid.
    # oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

# Under this new system policy, how many passphrases are valid?

import sys

valid = 0
for passphrase in sys.stdin:
	words = [''.join(sorted(word)) for word in passphrase.split()]

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
