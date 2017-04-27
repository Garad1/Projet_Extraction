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


if __name__ == '__main__':
    print("hey")
    main(sys.argv[1])