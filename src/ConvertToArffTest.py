import sys
import os.path
import re
def main(fich):
    print ("hello")
    Avis = open(fich, 'r')
    A = open("tests.arff", 'w')
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")
    i = 0

    while (i < 4000):
        line=re.sub("[^a-zA-Z0-9 '-]"," ", Avis.readline())
        line = "\"%s\",?\n" % line.replace("\n", "")
        A.write(line)
        i = i + 1


    return 1

def PNarff(fich):
    print ("hello")
    Avis = open(fich, 'r')
    A = open("NewCommentairesTest.arff", 'w')
    PN=open("RatioOutTest.txt","r")

    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@ATTRIBUTE ratio pos numeric\n")
    A.write("@ATTRIBUTE ratio neg numeric\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")
    i = 0

    for pn in PN:
        i = i + 1
        if i < 4000:
            line = "\"%s\",%s,?\n" % (Avis.readline().replace("\n", "").replace("\"", "'"),pn[:len(pn)-1])
            A.write(line)


if __name__ == '__main__':
    print("hey")
    PNarff(sys.argv[1])