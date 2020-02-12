# This is a very simple program that simply removes a certain line of characters from a text file
# It was written for accesability reasons as certain character strings can cause problems with screen readers
# Written by Adam Pohl

import sys

# Get name of file to edit
fileName = sys.argv[1]
# Get fileName without file extension
data = fileName.split(".")
# Prepare output name by appending "out.py" to end of filename
out = data[0] + "out.py"
# Create two files, one for input and one for output
fin = open(fileName, "rt")
fout = open(out, "wt")
# Go through file and replace all long comment lines with nothing
for line in fin:
    fout.write(line.replace('# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -', ''))

fin.close()
fout.close()