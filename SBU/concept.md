# Simple Source-code Back-up in Python
Aim-- a simple_to_understand, gradually_building_in_concept_stages; polite_to_new, indispensabe_to_veteran; smaller_yet_faster_than_gitHG; switchable_CVCS_DVCS_mode version contorl system that has intutive(dropdead_gorgeous_GUI, sensible_CLI_commands), pluginAble architecture ofcourse (esp. directly to text-editors) secure [multithreading & use a lang faster tha C-- Erlang Haskell FORTRAN]

## Challenging the Arcane Insane
repository is project
commit is backup
 is fetch
branch is experiment, buildUpon

## Features
gorgeous tab completion
**fetch this part/portion of abc.xyz file from last 3 revisions** and by "this part/portion" I mean a block .. it can be of whileLoop, forLoop, etc. or even main(){...} itself. hence in
	CLI - provide an option to reference blocks of code in a file in format `TLB-frstIndntPosn-scndIndntPosn...` e.g. `main-1-6-1` i.e. in this file in `main` TopLevelBlock -> in it go to 1st block in first_indent -> in it go to 6th block of second_indent -> in it go to first block of third_indent (this implies codeBeautifier is in-built but if a user doesn't want auto-code-beautification then report user that the cannot use this specific feature in CLI mode & must switch to GUI mode)
	GUI - just select (to highlight) the portion of code you want to see previous version of, right click, see prev. versions.
now it may happen that changing a part of code without taking whole file into consideration will cause broken code e.g. you retrieve a call to `os.getcwd()` from `main-1-6-1_ver11` but in current version you have removed the `import os` part in first few lines and as a result there will be a NameError. So -- SBU tries to do backtracing for you & generates a report like "pleas make sure/remember that:\n- to import abc, def & ghi\n- to define function xyz...." (implies understanding of languages is required) optionally you can ask it to backtrace throughout the project i.e.

## Abstract Stuff
	- when offline, i.e. space is an issue processing is limited, store entire files of project at regular intervals (say ever 50th commit so when building 51st stage, instead of applying 51 diffPatchSets to base repo you just have to apply 1 diffPatchSet to 50th commit), the interval is (by default) dictated by processing power of user.  
	On the server however, where space is a bigger issue and processing is done by **specialized** ASICs - store everything as diffPatchSet.
	- it is possible to apply diffPatchSet, make it possible to remove/undo/peelOff diffPatchSet
	- ask peole why branch? if it turns out that `branch == experiment` then rename branch to experiment and auto-assign tags like `experiment-feature`, `experiment-debug`, `experiment-optimization`, etc. based on user's choice and give it color code. When mid_user wants to branch_off_n_start_their_own_project call it buildUpon

## Commands in SSB
### Command - `ssb init`
`.ignore` file, if more than one merge them
make a `.ssb` folder it contains
	- store-leve-compressed-zipped backup of entire project along with message, name of zip file is project name followed by timestamp
	- so ideally `.ssb` should only contain several `[filenames].zip` take these and Ultra_PPMd_7zip them with optional AES-256, delete all the zip files
	- now there is no need of `.ssb` directory - everthing will lie in a hidden `project-name.ssb` file which is actually a 7z

### Command - `ssb status`

### Command - `ssb log`

### Command - `ssb addtostagingarea`
	WTF

### Command - `ssb diff`

### Command - `ssb commit -m`
	to zip the entire project along with an extra message.txt file (remember - this txt file should be easily available)

### Command - `ssb fetch sha2/commitNum_?branchName/partOfCommitMsgs`

### Command - `branch`

### Command - `merge`




NoSQLdb.username.projectname.trunk_or_branch.aStage = {
	"ObjectID":			// is it necessary
	"SHA1":
	"timestamp":
	"commitMsg":
	"aStageORdiffPatchSet_UltraPPMd.7z.bin":

	"TAGs":
	"branchMsg":		// why this branch was created? the text in this field is always automatically added to begining of commitMsg, this field is optional in trunk otherwise compulsary
}
