import sys
import os
import helpers
import urllib2
from Bio.Blast import NCBIWWW

def getCodon(keyCode, fastaCode, gi):
	# record = SeqIO.read("test.fasta", format="fasta")
	# result_handle = NCBIWWW.qblast("tblastn", "nt", record.format("fasta"))
	print "Starting.............. " + fastaCode
	result_handle = NCBIWWW.qblast("tblastn", "nt", gi)
	print fastaCode + " BLAST done!"
	codonFileName = 'protiens/' + keyCode + '/' + fastaCode + ".xml"
	to_file = open(codonFileName, "w")
	to_file.write(result_handle.read())
	print fastaCode + ' XML created!'
	#close files
	to_file.close()
	result_handle.close()

def main():
	fastaCodes = helpers.getProtienCodesForFasta('E.Coli.txt')
	GIFile = open('GI.txt', 'a+')
	for fastaCode in fastaCodes:
		keyCode = fastaCode[0:4].lower()
		fastaURL = 'http://www.ncbi.nlm.nih.gov/protein/' + fastaCode + '?report=gilist&log$=seqview&format=text'
		print fastaURL
		codonFileName = 'protiens/' + keyCode + '/' + fastaCode + ".xml"
		if not os.path.exists(codonFileName):
			fastaRequest = urllib2.Request(fastaURL, None, headers={'User-Agent' : 'Mozilla/5.0'})
			fastaResponse = urllib2.urlopen(fastaRequest)
			GI = fastaResponse.read().split('<pre>')[1].split('</pre>')[0]
			print GI
			getCodon(keyCode, fastaCode, GI)
			GIFile.write(GI)

	GIFile.close()

def driver():
	print helpers.getProtienCodesForFasta('E.Coli.txt')


if __name__ == '__main__':
	 main()