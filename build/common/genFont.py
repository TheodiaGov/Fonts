#!/usr/bin/env python
# coding=utf-8
## Copyright © from the date of the last git commit to this file in this git branch,
## by all persons with git blame to this file in this git branch, per the terms of
## the GNU AGPL 3.0 with the additional allowances of the GNU LGPL 3.0.
# Baby's first Python script

## Imports
import fontforge
import sys

## Helptext
def help():
	print("genFont.py")
	print("Copyright (C) 2018 by Miles B Huff per GNU LAGPL3")
	print()
	print("This program expects three variables:")
	print("- An action (either 'gen' or 'rip)")
	print("- An input file")
	print("- An output file")
	print()
	print("Actions:")
	print("- gen:  Expects an input .sfd file and an output font file.")
	print("- rip:  Expects an input font file and an output .sfd file.")

## Main
try:
	## Check for parameters
	if len(sys.argv) < 4:
		sys.stderr.write('Invalid parameters.\n')
		help()
		sys.exit(1)

	## Open the font
	font = fontforge.open(sys.argv[2])

	## Save the font as an .sfd
	if sys.argv[1] == 'rip':
		font.save(sys.argv[3])

	## Generate a font of the specified format, or a TTF font if bitmapped.
	elif sys.argv[1] == 'gen':
		font.generate(sys.argv[3], bitmap_type='ttf', flags=('apple', 'opentype', 'PfEd-background', 'PfEd-colors', 'round', 'TeX-table'), bitmap_resolution=-1) #'PfEd-guidelines'

	## If the first argument is invalid, exit with an error and message.
	else:
		sys.stderr.write('Invalid action.\n')
		sys.exit(2)

	## Close the font for reading
	font.close()

except:
	## If there were any errors, print what they are and quit with an error code.
	raise
	sys.exit(3)

## If there were no errors, quit successfully.
sys.exit(0)
