import sys
import re
import csv
import helpers as hlp
import os

def main():
	keyCodes = hlp.getProtienCodes('E.Coli.txt')


	for keyCode in keyCodes:
		pdbSearchCode = keyCode[1:5]
		pdbPath = 'protiens/' + pdbSearchCode + '/' + pdbSearchCode + '.pdb'
		dsspPath = 'protiens/' + pdbSearchCode + '/' + pdbSearchCode + '.dssp'	
		if not os.path.exists(dsspPath):
			print dsspPath + " doesn't exists \n"
			pass
		else :
			csvPath = 'protiens/' + pdbSearchCode + '/' + pdbSearchCode
			purgePath = 'protiens/' + pdbSearchCode + '/'
			hlp.purgeFiles(purgePath, ".csv")
			infile = open(dsspPath, "r")
			for line in infile:
				if(re.match(".*#.*",line)):
					#line = infile.next()
					# c = csv.writer(open(csvPath,"wb+"))
					# c.writerow(["Residue No.","Amino Acid","Structure"])
					for line in infile:
						suffix = re.split("\W+", line)[3] + '.csv'
						# print csvPath
						if not os.path.exists(csvPath + '_' + suffix):
							c = csv.writer(open(csvPath + '_' + suffix,"wb+"))
							c.writerow(["Residue No.", "Residue Class", "Amino Acid", "Structure"])
						splitLine = re.split("\W+",line)
						if( not (splitLine[3].isdigit() or splitLine[4].isdigit())):
							# print splitLine[2]+" "+splitLine[4]+" "+splitLine[5]	
							c.writerow([splitLine[2], splitLine[3], splitLine[4], splitLine[5]])
			infile.close()
	sys.exit(0)

if __name__ == '__main__':
	main()