import sys
import os
import re

def makeDirStructure(keyCodes):
	root = 'protiens/'
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

def getProtienCodesForFasta(protienFile):
	keyCodes = []
	pFile = open(protienFile, 'r')
	for line in pFile:
		if re.match('>(.*)', line):
			tempCompleteCode = line.split(' ')[0].split('>')[1].upper()
			tempFinal = tempCompleteCode[1:5] + '_' + tempCompleteCode[5]
			keyCodes.append(tempFinal)
	return keyCodes

def cleanProtienCodes(keyCodes):
	newKeyCodes = []
	for keyCode in keyCodes:
		newKeyCodes.append(keyCode[1:5])
	return newKeyCodes

def purgeFiles(dir, ext):
	filelist = [ f for f in os.listdir(dir) if f.endswith(ext) ]
	for f in filelist:
		if os.path.exists(dir + f):
			os.remove(dir + f)