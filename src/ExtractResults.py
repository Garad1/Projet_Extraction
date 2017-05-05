import os.path
import sys
from operator import truediv

def verif_result(input):
    input_file = open(input, 'r')
    justepos=0
    i=0
    for line in input_file:
        i+=1
        if i<=2000:
            if  int(line)==-1:
                justepos+=1
        else:
            if  int(line)==1:
                justepos+=1

    print("Il y a "+str( truediv(justepos,4000))+" commen correctes")

def extract(input_path, output_path):
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    input_file.readline()

    for line in input_file:
        line = line.split(",")

        if len(line) > 2:
            line = line[len(line) - 3].split(':')[1]
            print(line)
            output_file.write(line + "\n")

    return 1


def main():
    if len(sys.argv) != 3:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # dataset
        exit(1)

    print("Debut analyse")
    extract(sys.argv[1], sys.argv[2])
    print("fin analyse")


if __name__ == '__main__':
   verif_result(sys.argv[2])
