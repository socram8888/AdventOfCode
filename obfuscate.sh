#!/bin/bash -e

# ROT47 """encryption"""
# This isn't supposed to make reading these files impossible
# It's just to avoid others getting spoiled if you accidentally open a task you've still not solved

tmpfile=$(mktemp)

find $1 -type f -print0 | while read -d '' -r file; do
	tr '\!-~' 'P-~\!-O' <"$file" >"$tmpfile"
	mv "$tmpfile" "$file"
done
