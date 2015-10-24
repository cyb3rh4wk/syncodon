#!/usr/bin/env python


## Originally written by Alankrit Gupta and modifications are done by Raviprasad Aduri

## Use this script to extract a list of protein sequences from an organism from SCOP database

## command to run the program at the terminal:
## python extract_sequences-rpa.py input-file > output.txt 


## note the python script and the sequence file should be present in the same directory
## the output.txt will be created when you run the script 



import sys								##library for reading the file
import re 								##library for using 
from sys import argv					## way of reading the file
# script, infile = sys.argv				## reading the arguments from the terminal

## reading the file with read only permission
infile = open("astral-scopedom-seqres-gd-sel-gs-bib-40-2.04.fa", "r")		

check = 0

for line in infile:										## loop to read lines from file
	
	while check == 1 and not re.match(">(.*)", line):
		print line
		line = infile.next()
	while check == 1:
		check = 0
		print ''
		print '---------------------------------------------------------------------------------------'

	##  check condition to match pattern ; if true then continue
	if re.match("(.*)Escherichia coli(.*)", line):		
		# if ((re.match("(.*){Escherichia coli K-12 (.*)", line))or (re.match("(.*){Escherichia coli o6 (.*)", line)) or (re.match("(.*){Escherichia coli O157:H7(.*)", line))):
		#	continue

		# if ((re.match("(.*) 469008(.*)",line)) or (re.match("(.*) 668369(.*)",line)) or (re.match("(.*) 199310(.*)",line))):
		#	continue

		# if ((re.match("(.*) 405955(.*)",line)) or (re.match("(.*) 316407(.*)",line)) or (re.match("(.*) 511145(.*)",line))):
		#	continue

		# if ((re.match("(.*) 511693(.*)",line)) ):
		#	continue

		# if ((re.match("(.*) 714962(.*)",line)) or (re.match("(.*) 217992(.*)",line)) or (re.match("(.*) 9606(.*)",line))):
		#	continue

		print line

		check = 1