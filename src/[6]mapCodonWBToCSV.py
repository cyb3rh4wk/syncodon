import csv
import re
import urllib2
import os
import sys
import csv
import glob
import helpers

def matchCodons( aa1 , codon1 ):
	try:
		CodonSeq = open('AA_CODONS.csv','r')
		reader = csv.reader(CodonSeq)
   		for row in reader:
   			if(row[0] == aa1):
   				k=1
   				while(k<7):
   					if(row[k] == codon1):
   						CodonSeq.close()
   						return True
   					k+=1	
   				CodonSeq.close()	
   				return False	 				  						
	finally:
		l=0

keyCodes = helpers.getProtienCodesForFasta('E.Coli.txt')

for keyCode in keyCodes:
	tempKeyCode = keyCode[0:4].lower()
	filename1 = 'protiens/' + tempKeyCode + '/' + tempKeyCode + '_*_AA_CODONS.txt'

	filenames = glob.glob(filename1)
	
	for filename in filenames:
		print filename
		CODON = open(filename, 'r')
		AA = CODON.readline()
		CS = next(CODON)
		CS = CS.upper()


		i=0
		#print CS
		start=0
		# print len( CS )
		match=0
		# print len( CS )
		while(i < len(CS)-14 ):

			cod = CS[i] + CS[i+1] + CS[i+2]
			cod1 = CS[i+3] + CS[i+4] + CS[i+5]
			cod2 = CS[i+6] + CS[i+7] + CS[i+8]
			cod3 = CS[i+9] + CS[i+10] + CS[i+11]
			cod4 = CS[i+12] + CS[i+13] + CS[i+14]
			j=0
		
			#print cod + " \t " + cod1 + " \t " + cod2 + " \n" 

			while(j < len(AA) ) :
				aa = AA[j]
				s = matchCodons(aa,cod)
				if (s):
					aa1 = AA[j+1]
					s1 = matchCodons(aa1,cod1)
					if(s1):
						aa2 = AA[j+2]
						s2 = matchCodons(aa2,cod2)
						if(s2):
							aa3 = AA[j+3]
							s3 = matchCodons(aa3,cod3)
							if(s3):
								aa4 = AA[j+4]
								s4 = matchCodons(aa4,cod4)
								if(s4):
									start=j
									match = 1
									break
								else:
									j+=1
							else:
								j+=1
						else:
							j+=1
					else:
						j+=1
				else:
					j+=1
			if(match == 1) :
				break
			i = i+1


		if(match == 1):
			csvsrc = 'protiens/' + tempKeyCode + '/' + tempKeyCode + "_" + filename[19] + ".csv"
			csvtarget = 'protiens/' + tempKeyCode + '/' + tempKeyCode + "_" + filename[19] + "_With_Codons.csv"
			src = open (csvsrc,'r')
			reader = csv.reader(src)
			target = open (csvtarget,'wb')
			writer = csv.writer(target)
			p=0
			key=0
			#writer.writerow(["Residue No.","Amino Acid","Structure","Codon"]) 
			for row in reader:
				if(start == 1111):
					if (p==0):
						Codon = "Codon"
						writer.writerow([row[0],row[1],row[2],Codon])
					else:
						Codon = "000"
						writer.writerow([row[0],row[1],row[2],Codon])
				else:
					if (p==0):
						Codon = "Codon"
						writer.writerow([row[0],row[1],row[2],Codon])
				
					elif( (p <= start ) or ( p > (start + (len(CS)-i)/3 ) ) ):
						Codon = "000"
						writer.writerow([row[0],row[1],row[2],Codon])
					else:
						if(key<(len(CS))-3):
							Codon = CS[key+i]+CS[key+i+1]+CS[key+i+2]
							key +=3
						else:
							Codon = "000"

						writer.writerow([row[0],row[1],row[2],Codon])
				p +=1


		CODON.close()
		#CodonSeq.close()
