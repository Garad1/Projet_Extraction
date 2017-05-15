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



def analyseTTG(dataset, posW, negW):
    liste_not=["not","don't","haven't","doesn't","wasn't","isn't","weren't","hasn't","won't","wouldn't","hadn't","can't","didn't","n't"]
    D = open(dataset, 'r')
    Out = open("RatioOutTest.txt", 'a')

    pos = 0
    neg = 0

    for line in D:
        words = line.split(' ')
        for i in range(0,len(words)):
            if(i>=2):
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

        Out.write(str(int(truediv(pos,(pos+neg))*100))+", "+str(int(truediv(neg,(pos+neg))*100))+"\n")


    return 1

def moyenne(data):
    Out = open(data, 'r')
    moypos=0
    moyneg=0
    moypos2 = 0
    moyneg2 = 0
    i=0
    for line in Out:
        words = line.split(' ')
        i += 1
        if i<5000:
            moypos+= int(words[0])
            moyneg += int(words[1])

        else:
            moypos2 += int(words[0])
            moyneg2 += int(words[1])

    print ("moyene positive pour les neg :"+ str(moypos/5000))
    print ("moyene negative pour les neg :" + str(moyneg / 5000))

    print ("moyene positive pour les pos:" + str(moypos2 / 5000))
    print ("moyene negative pour les pos :" + str(moyneg2 / 5000))

def parse():
    file=open("RatioOut.txt","r")
    file2 = open("Ratio2Out.txt", "w")
    for line in file:
        lines=line.split(' ')
        for l in lines:
            if len(l)>2:
                file2.write(l[:2]+"\n"+l[-2:]+", ")
            else:
                file2.write(l+" ")





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

