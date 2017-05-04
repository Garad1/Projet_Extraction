import sys
import os.path

def PNarff(fich):
    print ("hello")
    Avis = open(fich, 'r')
    A = open("NewCommentaires.arff", 'w')
    PN=open("Ratio2Out.txt","r")

    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@ATTRIBUTE ratio pos numeric\n")
    A.write("@ATTRIBUTE ratio neg numeric\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")
    i = 0

    for pn in PN:
        i = i + 1
        if i < 5000:
            line = "\"%s\",%s,-1\n" % (Avis.readline().replace("\n", "").replace("\"", "'"),pn[:len(pn)-1])
            A.write(line)

        else:
            line = "\"%s\",%s,1\n" % (Avis.readline().replace("\n", "").replace("\"", "'"),pn[:len(pn)-1])
            A.write(line)

def main(fich):
    print ("hello")
    Avis = open(fich, 'r')
    A = open("Commentaires.arff", 'w')
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")
    i = 0

    while (i < 5000):
        line = "\"%s\",-1\n" % Avis.readline().replace("\n", "").replace("\"","'")
        A.write(line)
        i = i + 1
    while (i < 10000):
        line = "\"%s\",1\n" % Avis.readline().replace("\n", "").replace("\"", "'")
        A.write(line)
        i = i + 1

    return 1


if __name__ == '__main__':
    print("hey")
    PNarff("NewDataTAG.txt")