# This script will take E-coli.txt generated and will categorize the data according to the protein code (eg. 1kf6)
# author: cyb3rh4wk, bugcracker, Unknown
# python: v2.7 and v3
# before running the script check the filepath. Windows: "path\to\file"; Unix: "/path/to/file"
import urllib2
import sys
import os
import re
import subprocess
import helpers as hlp


def pdbToDSSP(pdbSource, pdbSearchCode):
	# This function can also be done using biopython library more efficiently
	# This method creates a subprocess which will use dssp.exe to convert pdb file to dssp
	# In Unix, Wine is required to run Windows executables
	command = './dssp.exe ' + pdbSource + ' -o ' + 'protiens/' + pdbSearchCode + '/' + pdbSearchCode + '.dssp'
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	p.wait()

def main():
	keyCodes = hlp.getProtienCodes('E.Coli.txt')
	hlp.makeDirStructure(keyCodes)
	for keyCode in keyCodes:
		pdbSearchCode = keyCode[1:5]
		print pdbSearchCode
		url = 'http://www.rcsb.org/pdb/files/' + pdbSearchCode + '.pdb'	# REST API for fetching pdb files
		pdbPath = 'protiens/' + pdbSearchCode + '/' + pdbSearchCode + '.pdb'
		# pdb file for respective protein is fetched only if it doean't exist
		if not os.path.exists(pdbPath):
			response = urllib2.urlopen(url)
			pdbData = response.read()
			pdbFile = open(pdbPath, 'w')
			pdbFile.write(pdbData)
			pdbFile.close()
		dsspPath = 'protiens/' + pdbSearchCode + '/' + pdbSearchCode + '.dssp'
		if os.path.exists(pdbPath) and not os.path.exists(dsspPath):
			pdbToDSSP(pdbPath, pdbSearchCode)	# Converting the pdb file to dssp

if __name__ == '__main__':
	main()