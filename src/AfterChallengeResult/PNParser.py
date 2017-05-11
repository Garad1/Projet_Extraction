"""
    Adam Garcia
    Fati Chen
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
@:return:boolean
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

def analyse(dataset, posW, negW):
# ------------Ouverture des fichiers-----------------#
    D = open(dataset, 'r')
    Out = open("RatioOut.txt", 'w')

# ------------   Variables----------------------------#
    pos = 0
    neg = 0

# ------------Liste des mots qui transforme un mot positif en nrgatif-----------------#
    liste_not = ["not", "don't", "haven't", "doesn't", "wasn't", "isn't", "weren't", "hasn't", "won't", "wouldn't",
                 "hadn't", "can't", "didn't", "n't"]

# ------------Analyse :-----------------#
# Pour chaque mot du commentaire on verifie s'il est positif ou negatif (dans le dico)
# et si un mot et positif on verifie egalement qu'il n'est pas precede d'une negation
    for line in D:
        words = line.split(' ')
        for i in range(0,len(words)):
            if(i>=2): # on verifie la negation qu'apres le 2eme mot du commentaire
                if positif(posW, words[i]):
                    if words[i-1] in liste_not or words[i-2] in liste_not:
                        neg=neg+1
                    else:
                        pos=pos+1
                if negatif(negW, words[i]):
                    if words[i - 1] not in liste_not and words[i - 2] not in liste_not:
                        neg = neg + 1
            else:
                if positif(posW, words[i]):
                    pos = pos + 1
                elif negatif(negW, words[i]):
                    neg = neg + 1
 # ------------Ecriture des pourcentages de mots positifs/negatifs sur le fichier de sortie-----------------#
        Out.write(str(int(truediv(pos,(pos+neg))*100))+", "+str(int(truediv(neg,(pos+neg))*100))+"\n")


    return 1






if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # result treetaggerparser (DataTAG)
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

