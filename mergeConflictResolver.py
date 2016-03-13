import os

ERROR = "\n<script>alert('fatal error occured, diff file or source file corrupted.\nTerminating execution.)</script>)"
initString = r"""
<!doctype html><html><head><meta charset = "utf-8"><title>GUI Merge Resolver</title>
<script>highlight.js   see(envato's 25 syntax highlighters tried and tested)</script>
<script>
/*
create checkboxes (and sub-sup tags if css can't handle it as per SO)
on every element having class delete/insert and id. if checked then
commit changes to file.
*/
get xxx by class
add checkbox to span
-- loop to read the changes made
-- prompt user to save changes
</script>
<styles>
// make span text superscript +css
body {
	/* reduce width to about 80%, center align
		word-wrap disable with side scroll-bar enable
	*/
	align: 0 auto;
}
.insert {
	background-color: green;
	vertical-align: super;
	font-size: 0.83 em
}
.delete {
	background-color: red;
	vertical-align: sub;
	font-size: 0.83 em
}
</styles></head><body>
<h1>Merge Resolve: <span style="background-color:pink">%s</span></h1></br></hr>
<save n close button
<pre>\n<code>\n
"""
endString = r"""\n</code></pre></body></html>"""
deleter = r"""<span id=#%d class="delete">%s</span>"""
inserter= r"""<span id=#%d class="insert">%s</span>"""

def gui(conflictFile, diff): # for safety from file and diff mismatch, this fn should never be called explicitly# if len(diff) is 0:	print("diff data structure not found");	elif cFhandel.count(RSC) not len(diff):	print("data structure mismatch")
	gui = os.tempDir + os.path.basename(conflictFile) + "resolve.html"
	#	ensure all None in diff dict get replaced by empty strings
	src, dest = openFile(conflictFile), openFile(gui, "wt")
	dest.write(initString % os.path.basename(coflictFile))
	
	writeBuffer = str()
	for i, char in enumerate(src):
		if char is RSC:
			dest.write(writeBuffer);	writeBuffer = ""
			try:
				ds = diff[i]
			except KeyError:
				dest.write(ERROR)
				break	#raise
			if ds[0] is None:
				dest.write(inserter % (i, ds[1]))
			elif ds[1] is None:
				dest.write(deleter % (i, ds[0]))
			else:
				dest.write(deleter % (i, ds[0]))
				dest.write(inserter % (i, ds[1]))
		else:
			writeBuffer+= char
	
	dest.write(endString)
	closeFiles(src, dest)
	os.start(gui) # js can not write the final result to disk, hence wait ?threading? till file is closed
	return

def cli(conflictFile, diff):
	# o,n- choose old,new char;; n,p- view next or previous conflict
	try:
		import ncurses
	except:
		input("Avanced 'shell display control' libraries unavailable, try installing ncurses.")
		print("Initiating GUI merge conflict resolver . . .")
		gui(conflictFile, diff)
	# notepad.cc/pyGuiTui		1234
	# defaults to line wise resolving (may switch to char-wise at
	# any time) if u wanna keep both then one of them will be commented
	# inline or in line above(new) or below(old)
	return
