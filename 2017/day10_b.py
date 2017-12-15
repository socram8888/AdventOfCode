#!/usr/bin/env python3

import sys
from knothash import knothash

print(knothash(sys.stdin.buffer.read()).hex())
