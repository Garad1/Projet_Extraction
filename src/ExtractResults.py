"""
    Adam Garcia
    Fati Chen
    Melissa Mekaoui : 21612501
    Pascal Zaragoza : 20130039
"""
import os.path
import sys
from operator import truediv

"""
fonction qui extrait la classe des commentaires
du datatest fourni par le classifieur, pour une meilleure vue
des resultats

@param  : input_path : fichier cree par weka
          output_path : un fichier de sortie quelconque
@return : void
"""

def extract(input_path, output_path):
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')

    input_file.readline()

    for line in input_file:
        line = line.split(",")

        if len(line) > 2:
            line = line[len(line) - 3].split(':')[1]
            output_file.write(line + "\n")

"""
fonction qui calcule le taux de classification correct

@param: output_path de la fonction precedente
@return: void
"""
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

    print("Il y a "+str( truediv(justepos,4000))+" commentaires corrects")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # resultats du classifieur SMO (sous weka)
        exit(1)

    print("Starting...")
    extract(sys.argv[1], sys.argv[2])
    verif_result(sys.argv[2])
    print("End.")

