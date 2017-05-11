"""
    Adam Garcia
    Fati Chen
    Melissa Mekaoui : 21612501
    Pascal Zaragoza : 20130039
"""
import os.path
import re
import sys
import treetaggerwrapper

"""
Fonction qui supprime tous les mots des commentaires qui ne font pas partie
des categories grammaticales qu'on juge importantes.
@param : fichier contenant les commentaires
@return: void

    categ grammaticales importantes :
        adjectifs    -> TAGS -> JJ , JJR , JJS
        verbes       -> TAGS -> VV , VVD , VVG, VVN
        adverbes     -> TAGS -> RB , RBR , RBS
        interjections-> TAGS -> UH

"""


def Tagger(dataset):
# ------------Ouverture des fichiers-----------------------------------#
    D = open(dataset, 'r')
    Tag = open("DataTAG.txt", 'w')

# ------------Liste des tags a prendre en concideration-----------------#
    ListeTags = ["JJ", "JJR", "JJS", "VV", "VVD", "VVG", "VVN", "RBR", "RBS", "UH", "RB"]

# ------------Config du wrapper------------------------------------------#
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGDIR='./TreeTagger', TAGINENC='utf-8', TAGOUTENC='utf-8')

# ------------Analyse:----------------------------------------------------#
# Pour chaque ligne du dataset ,treetagger analyse le commentaire
# et renvoie les mots importants dans le fichier DataTAG

    for line in D:
        line = re.sub('http:\/\/[0-9a-zA-Z-_\.]*(\.[a-z]{0,9}\/?)?', "website ", line) #supression des url
        line = re.sub("[^a-zA-Z0-9 '-]", " ",line)              # suppression de tous les carracteres speciaux (sauf :',- et l'espace)
        tags = tagger.TagText(line.decode(encoding="utf-8"))    # "taggage" de chaque mot du commentaire
        for words in tags:                                      #recuperations des mots qui possedent les tags de ListTags
            w = words.split("\t")

            if w[1] in ListeTags:
                Tag.write(w[0] + " ")
        Tag.write("\n")



if __name__ == '__main__':
    print("hey\n")
    if len(sys.argv) != 2:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # dataset.csv
        exit(1)

    print("Starting...")
    Tagger(sys.argv[1])  # dataset.csv
    print("End.")
