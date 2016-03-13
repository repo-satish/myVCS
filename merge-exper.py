RSC = BLANK #really special character

def merge(old, new, output=None):
	if output is None:	# implies final "conflict resolved" merge should overwrite new
		# code
	else:
		result = open(output, "wt", encoding="UTF-8")
	diff = dict()
	x = lambda arg: result.write(RSC) if arg is None else result.write(arg)
	for _ in range(max(sizeof(new), sizeof(old))):
		o = old.read(1)	# reads 1 char and not 1 byte
		n = new.read(1)
		# d.s. ====   [delete, insert] @ that position
		if o is n and o+n not "":
			x(o) # x(n) is also okay
			continue # speedy
		else:
			if n is "":	# new file has ended
				diff(_) = [o, None]	# ctor, i.e. {posn: [delete, insert]}.. note that _ here is index so enum() isn't needed
			elif o is "":	# old file has ended
				diff(_) = [None, n]
			else:
				diff(_) = [o, n]
			x()
	result.close()
	return diff

def resolveMerge(conflictFile, diff): # for safety from file and diff mismatch, this fn should never be called explicitly
	if len(diff) is 0:
		print("diff data structure not found")
	elif cFhandel.count(RSC) not len(diff):
		print("data structure mismatch")
	else
		os.start(conflictFile+"resolve.html") # js writes the final result to disk
	return









r"""
i = int()	# will be needed outside the loop

for i, char in old:
	try:
		c = diff(i)
	except KeyError:
		continue
	new.seek(i)
	new.write(c[1])	# it should be overwritten not inserted

for _ in range(i, sizeof(new))
"""