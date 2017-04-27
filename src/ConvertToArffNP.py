import sys
import os.path

def main(fichA,fichB):
    print ("hello")
    Avis = open(fichA, 'r')
    PNFile = open(fichB, 'r')
    A = open("Commentaires.arff", 'w')
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@ATTRIBUTE weight  { 'positive', 'negative', 'neutral'}\n")
    A.write("@attribute class {-1,1}\n")
    A.write("@data\n")
    i = 0

    while (i < 5000):
        line = "\""+Avis.readline().replace("\n", "").replace("\"","'")+"\","+PNFile.readline().replace("\n","")+",-1\n"
        A.write(line)
        i = i + 1
    while (i < 10000):
        line = "\"" + Avis.readline().replace("\n", "").replace("\"", "'") + "\"," + PNFile.readline().replace("\n",
                                                                                                             "") + ",1\n"

        A.write(line)
        i = i + 1

    return 1


if __name__ == '__main__':
    print("hey")
    main(sys.argv[1],sys.argv[2])