import sys
import os.path

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
    main(sys.argv[1])