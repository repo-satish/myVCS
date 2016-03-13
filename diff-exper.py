"""
	2 file diff utility written in python
		add? ability to mention encoding in shell"
"""

import os, sys
from collections import namedtuple



try:
	fileA = sys.argv[1]
	fileB = sys.argv[2]
except IndexError:
	print("\tUsage:\n`diff file1 file2`\n")
	input()
	sys.exit(1)

opeN = lambda fn: open(fn, mode="rt", encoding="UTF-8")

with opeN(fileA), opeN(fileB) as a, b:
	diff(a, b)