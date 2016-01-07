import re
import urllib2
import os
import sys
import csv
import helpers
import glob

keyCodes = helpers.getProtienCodesForFasta('E.Coli.txt')

for keyCode in keyCodes:
	fileKeyCode = keyCode[0:4].lower()
	protienFileName = 'protiens/' + fileKeyCode + '/' + keyCode + '.xml'
	print protienFileName
	filenames = glob.glob(protienFileName)
	for filename in filenames:
#	xml_name = 'protiens/' + pdbSearchCode + '/' + pdbSearchCode + '.xml'
		infile = open(filename, "r")

		for line in infile:
		
			if re.match(".*<Hit_num>1</Hit_num>.*", line):
				line = infile.next()

				if re.match(".*<Hit_id>gi|.*</Hit_id>.*", line):
					start = line.find("gi|") + 3
					end = line.find("|",start)
					ans = line[start:end]
					break

		if (ans!=None):
			output1 = filename[0:len(filename)-5].lower() + filename[len(filename)-5] + "_AA_CODONS.txt"
			output2 = filename[0:len(filename)-5].lower() + filename[len(filename)-5] + ".csv"
			if not os.path.exists(output1):
				urlForCodons = 	"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?val=" + ans + "&db=nuccore&dopt=fasta&retmode=text"
				response = urllib2.urlopen(urlForCodons)
				f = open('CodonSequence.txt', 'w+') 
				f.write(response.read())
				f.close()
				
				print output2
				print output1
				out = open(output1, 'w')
				csvFile = csv.reader(open(output2,"r"))
				csvFile.next()
				for csvLine in csvFile:
					out.write(csvLine[1].strip("\n"))
				out.write("\n")

				f = open('CodonSequence.txt', 'r')
				for line in f:
					 if re.match(".*gi.*", line):
					 	 # out = open('out.txt', 'w')
						 for line in f:	
						 	out.write(line.strip("\n"))
				f.close()
				
				out.close()













			# urlForCodons = 	"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?val=" + ans + "&db=nuccore&dopt=fasta&retmode=text"
			# response = urllib2.urlopen(urlForCodons)
			# output = filename[0:len(filename)-4] + "_AA_CODONS.txt"
			# f = open('out', 'w') 
			# f.write(response.read())
			# f.close()

			# f = open('out', 'r')
			# for line in f:
			# 	if re.match(".*gi.*", line):
			# 	 	out = open(output, 'w')
			# 	 	for line in f:
			# 	 		out.write(line.strip("\n"))

			# out.close()		 	
			# f.close()
#	os.remove(f)	