import itertools
import csv
import helpers
import glob

fin={}
allCodons = []

allStructures = []
for structure in itertools.product('ABR', repeat=3):
    s2 = ''.join(structure)
    allStructures.append(s2)
      
for codons in itertools.product('ACGT', repeat=9):
    s1 = ''.join(codons)
    s1 = s1[0]+s1[1]+s1[2]+'|'+s1[3]+s1[4]+s1[5]+'|'+s1[6]+s1[7]+s1[8]
    allCodons.append(s1)
    for structure in allStructures:
        fin[(s1,structure)] = 0

def main():
    keycodes = helpers.getProtienCodesForFasta('E.Coli.txt')

    for keycode in keycodes:
        tempKeycode = keycode[0:4].lower()
        path = "protiens/"+tempKeycode+"/"+tempKeycode+"_*_GROUP.csv"
        filenames = glob.glob(path)
        for filename in filenames:
            infile = open(filename, 'r')
            reader = csv.reader(infile)

            d={}

            allCodons = []
            for codons in itertools.product('ACGT', repeat=9):
                s1 = ''.join(codons)
                s1 = s1[0]+s1[1]+s1[2]+'|'+s1[3]+s1[4]+s1[5]+'|'+s1[6]+s1[7]+s1[8]
                allCodons.append(s1)
                for structure in allStructures:
                	d[(s1,structure)] = 0


            count = 0
            for line in reader:
                if(count==0):
                     count+=1
                     continue
                if (line[2].rstrip(), line[1].rstrip()) in d:
                     d[(line[2].rstrip(), line[1].rstrip())] += 1
                     fin[(line[2].rstrip(), line[1].rstrip())] += 1
                     # print 'Incremented' + ' ' + line[2].rstrip() + ' ' + line[1].rstrip() + ' : ' + str(d[(line[2].rstrip(), line[1].rstrip())])

            listStructure = ['']
            for structure in allStructures:
                listStructure.append(structure)

            newfile = open('protiens/' + tempKeycode + '/' +'1kf6_'+filename[-13]+'_MATRIX.csv','w')
            matrixcsv = csv.writer(newfile)
            matrixcsv.writerow(listStructure)

            for codons in allCodons:
                listCodon=[]
                listCodon.append(codons)
                for structure in allStructures:
                	listCodon.append(d[(codons,structure)])
                    # print listCodon
                matrixcsv.writerow(listCodon)
            print filename


            listStructure = ['']
            for structure in allStructures:
                listStructure.append(structure)

            newfile = open('FINAL_MATRIX.csv','w')
            matrixcsv = csv.writer(newfile)
            matrixcsv.writerow(listStructure)

            for codons in allCodons:
                listCodon=[]
                listCodon.append(codons)
                for structure in allStructures:
                    listCodon.append(fin[(codons,structure)])
                    # print listCodon
                matrixcsv.writerow(listCodon)


if __name__ == '__main__':
     main()