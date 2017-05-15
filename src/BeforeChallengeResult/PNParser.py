"""
    Adam Garcia : 20133168
    Fati Chen   : 20121110
    Melissa Mekaoui : 21612501
    Pascal Zaragoza : 20130039
"""
import sys
import os.path
from operator import truediv

"""
Fonction qui determine si un mot est positif
ou non en utilisant un dictionnaire
de mots a connotations positives
@param: le dictionnaire : posW
        le mot: word
@return:boolean
"""
def positif(posW ,word):
    PW= open(posW ,'r')

    for line in PW:
        if word == line.strip():
            return True
        
    return False

"""
Fonction qui determine si un mot est negatif
ou non en utilisant un dictionnaire
de mots a connotations negatives
@param: le dictionnaire : negW
        le mot: word
@:return:boolean
"""
def negatif(negW,word):
    NW= open(negW,'r')
    for line in NW:
        if word == line.strip():
            return True
        
    return False
"""
Fonction qui va analyser chaque mot de chaque commentaire
et qui determinera si le commentaire est positif ou negatif
selon le nombre de mots positifs et negatifs
@param: les commentaires : dataset
        dico des mots positifs : posW
        dico des mots negatifs : negW
@return: void
"""
def analyse(dataset,posW,negW):
# ------------Ouverture des fichiers-----------------#
    D= open(dataset,'r')
    Out= open("poids.txt",'w')

# ------------Variables -----------------------------#
    pos=0
    neg=0

# ------------Analyse -------------------------------#
    for line in D:
        words =line.split(' ')
        for w in words:
            if positif(posW,w):
                pos=pos+1
            elif negatif(negW, w):
                neg=neg+1
        if pos>neg+2:
            Out.write("positive\n")
        elif neg>pos+2:
            Out.write("negative\n")
        else:
            Out.write("neutral\n")
        pos=0
        neg=0





if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # dataset
        exit(1)
    elif not os.path.isfile(sys.argv[2]):
        print("Erreur: fichier ", sys.argv[2], "introuvable")  # positif words
        exit(1)
    elif not os.path.isfile(sys.argv[3]):
        print("Erreur: fichier ", sys.argv[3], "introuvable")  # negatif words
        exit(1)

    print("Starting...")
    analyse(sys.argv[1], sys.argv[2], sys.argv[3])
    print("End")

