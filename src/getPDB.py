import urllib2
import sys
import os
import re
import subprocess

def makeDirStructure(keyCodes):
	root = 'proteins/'
	if not os.path.exists(root):
		os.mkdir(root, 0777)
	for keyCode in keyCodes:
		protienPath = root + keyCode[1:5]
		if not os.path.exists(protienPath):
			os.mkdir(protienPath, 0777)

def getProtienCodes(protienFile):
	keyCodes = []
	pFile = open(protienFile, 'r')
	for line in pFile:
		if re.match('>(.*)', line):
			keyCodes.append(line.split(' ')[0].split('>')[1])
	return keyCodes

def pdbToDSSP(pdbSource, pdbSearchCode):
	# p = PDBParser()
	# structure = p.get_structure(pdbSearchCode, pdbSource)
	# model = structure[0]
	# dssp_dict = dssp_dict_from_pdb_file(pdbSource, DSSP='dssp')
	# dssp = DSSP(model, pdbSource)
	# print list(dssp)
	# print str(dssp_dict)
	command = 'dssp.exe ' + pdbSource + ' -o ' + 'proteins/' + pdbSearchCode + '/' + pdbSearchCode + '.dssp'
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	p.wait()

def main():
	keyCodes = getProtienCodes('E.Coli.txt')
	makeDirStructure(keyCodes)
	for keyCode in keyCodes:
		pdbSearchCode = keyCode[1:5]
		print pdbSearchCode
		url = 'http://www.rcsb.org/pdb/files/' + pdbSearchCode + '.pdb'
		pdbPath = 'proteins/' + pdbSearchCode + '/' + pdbSearchCode + '.pdb'
		if not os.path.exists(pdbPath):
			response = urllib2.urlopen(url)
			pdbData = response.read()
			pdbFile = open(pdbPath, 'w')
			pdbFile.write(pdbData)
			pdbFile.close()
		dsspPath = 'proteins/' + pdbSearchCode + '/' + pdbSearchCode + '.dssp'
		if os.path.exists(pdbPath) and not os.path.exists(dsspPath):
			pdbToDSSP(pdbPath, pdbSearchCode)

if __name__ == '__main__':
	main()
