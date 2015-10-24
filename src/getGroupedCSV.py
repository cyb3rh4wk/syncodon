import re
import os
import sys
import csv
import helpers as hlp

def getResidueNum(line):
	return line.split(',')[0]

def getAminoAcids(line):
	return line.split(',')[1]

def getStructures(line):
	return line.split(',')[2]

def getCodons(line):
	return line.split(',')[3].split('\r')[0]

def getGroupedCSV(residueNum, aminoAcid, structure, groupCount, keyCode):
	aminoAcidSeq = []
	structureSeq = []
	codonSeq = []
	for i in range(0,len(residueNum)):
		if ( (i + groupCount - 1) <= len(residueNum) - 1 ):
			tempResidue = ''
			tempAA = ''
			tempStruct = ''
			tempCodon = ''
			for j in range(0, groupCount):
				tempAA = tempAA + aminoAcid[i + j]
				tempStruct = tempStruct + structure[i + j]
				tempCodon = tempCodon + ' | ' + codon[i + j]
			aminoAcidSeq.append(tempAA)
			structureSeq.append(tempStruct)
			codonSeq.append(tempCodon)
	# CSVFile = csv.writer(open('protiens/' + keyCode + '/' + keyCode + '_' + str(groupCount) + '_GROUP' + '.csv', 'wb'))
	# CSVFile = csv.writer(open('test_GROUP.csv', 'wb'))
	# CSVFile.writerow(['Amino Acids', 'Structures', 'Codons'])
	print aminoAcidSeq[i], structureSeq[i], codonSeq[i]

	# for i in range(0, len(aminoAcidSeq)):
	# 	CSVFile.writerow([aminoAcidSeq[i], structureSeq[i], codonSeq[i]])
	sys.exit(0)


def main():
	residueClass = raw_input("Please enter the Residue class: (Eg. A,B,C.....) ")
	residueClass = residueClass.upper()
	groupCount = int(raw_input("Please enter the grouping constant: "))
	# print residueClass
	# print groupCount
	keyCodes = hlp.getProtienCodes("E.Coli.txt")
	keyCodes = hlp.cleanProtienCodes(keyCodes)
	keyCodes = list(set(keyCodes))
	for keyCode in keyCodes:
		targetFile = 'protiens/' + keyCode + '/' + keyCode + '_' + residueClass + '.csv'
		if os.path.exists(targetFile):
			infile = open(targetFile, 'r')
			infile.next()

			residueNum = []
			aminoAcid = []
			structure = []
			codons = []
			for line in infile:
				# print line
				residueNum.append(getResidueNum(line))
				aminoAcid.append(getAminoAcids(line))
				structure.append(getStructures(line))
				codons.append(getCodons(line))
			print keyCode, len(residueNum)
			getGroupedCSV(residueNum, aminoAcid, structure, codons, groupCount, keyCode)


if __name__ == '__main__':
	main()