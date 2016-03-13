import os
import mergeConflictResolver

RSC = BLANK #really special character

openFile = lambda filePath, way: open(filePath, mode="rt", encoding="UTF-8") \	# if this doesn't work try assigning default value to way in begining,, else try `*way@`
				if way is None else open(NEW, mode=way, encoding="UTF-8")
closeFiles = lambda *fileHandleList: _.close() for _ in fileHandleList

def diff_files(OLD, NEW):	# ?? implement char by char | line by line    comparision mode
	diff = dict()	# dict to store charcaterwise diffs
	old, new = openFile(OLD), openFile(NEW)
	for _ in range(max(sizeof(new), sizeof(old))):	# ensure loop runs enough to cover the larges file
		o = old.read(1)	# reads 1 char and not 1 byte
		n = new.read(1)
		# data structure ====>   [delete, insert] @ that position
		if o is n and o+n not "":	# characters match and neither is NULL; no problems, move on
			continue
		else:
			if n is "":	# new file has ended
				diff(_) = [o, None]	# !! ctor, i.e. {posn: [delete, insert]}.. note that _ here is index so enum() isn't needed
				diff(_)[0]+= o.read();	break	# speed hack
			elif o is "":	# old file has ended
				diff(_) = [None, n]
				diff(_)[1]+= n.read();	break	# speed hack
			else:
				diff(_) = [o, n]
	closeFiles(old, new)
	return diff

def merge(OLD, NEW, OUTPUT=None):
	if OUTPUT is None:	# implies resolve in terminal;;; final "conflict resolved" merge should overwrite new
		path = os.tempDir+timestamp+".txt"
		result = openFile(path, "wt")
	else:	# implies conflict resolution should happen in GUI
		result = openFile(OUTPUT, "wt")
	diff = diff_files(OLD, NEW)
	old, new = openFile(OLD), openFile(NEW)
	for _ in range(min(sizeof(new), sizeof(old))):
		o = old.read(1)	# reads 1 char and not 1 byte
		n = new.read(1)
		if o is n:
			result.write(o) # writing n is also okay
		else:
			result.write(RSC)
	result.write(RSC*file_size_difference)
	closeFiles(result, old, new)
	if OUTPUT is None:
		mergeConflictResolver.cli(path, diff)
	else:
		mergeConflictResolver.gui(OUTPUT, diff)
	return



r"""		file character mapper=== {a: [2, 4, 16...], b: [1, 9, 34...]??}
pos = 0
while True:
	char = fh.read(1)
	if char is "":	break
	pos+= 1
	try:
		charPosMapDict[char].append(pos)
	except KeyError:
		charPosMapDict[char] = [pos]	# ctor
"""
r"""old, new = list(), list()"""
r"""
 ------------------------------------------------------------
inter = list()	# create an array of empty elements
inter.append(None) for _ in range(max(sizeof(new), sizeof(old))

for i in inter:	# scan char by char in each file
	o = old.read(1)	# reads 1 char and not 1 byte
	n = new.read(1)
	# d.s. ====   [delete, insert] @ that position
	if n is "":
		i = [o, None]
		i[0]+= o.read();	break	# speed hack
	elif o is "":
		i = [None, n]
		i[1]+= n.read();	break	# speed hack
	elif o is n:
		continue
	else:
		i = [o, n]

diff = dict()
for i, val in enumerate(inter):
	if type(val) is None:
		continue
	else:
		diff(i) = val	# ctor, i.e. {posn: [delete, insert]}
 ------------------------------------------------------------
"""
r"""
i = int()	# will be needed outside the loop

for i, char in enumerate(old):
	try:
		c = diff(i)
	except:
		continue
	new[i] = c[1]	# if c[1] is None IMPLIES delete/skip ???????????????
for _ in range(i, sizeof(new)):
	new[i] = diff[i][1]	# for rest of the file
"""

r"""
def applyDiff(OLD, NEW, diff):
	old = open(OLD, mode="rt", encoding="UTF-8")
	new = open(NEW, mode="?t", encoding="UTF-8")
	for _ in range(sizeof(old)):	# cuz old + diff = new
		try:
			c = diff(_)
		except KeyError:
			continue
		new.seek(_)
		new.write(c[1])	# it should be overwritten not inserted
	old.close();	new.close();
	return
"""