import sys
import os.path
import treetaggerwrapper
import  ConvertToArff

"""
    categ grammaticales importantes :
        (A revoir)
        adjectifs -> TAGS -> JJ , JJR , JJS
        verbes    -> TAGS -> VV , VVD , VVG, VVN
        adverbes  -> TAGS -> RB , RBR , RBS

    """

def Tagger(dataset) :
    #ouverture des fichiers
    D   = open(dataset, 'r')
    Tag = open("DataTAG.txt", 'w')

    #liste des tags a prendre en concideration
    ListeTags=["JJ","JJR","JJS","VV","VVD","VVG","VVN","RBR","RBS"]

    #cnfig du wrapper
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGDIR='./TreeTagger',TAGINENC='utf-8', TAGOUTENC='utf-8')

    #Analyse:
    #Pour chaque ligne du dataset ,
    #treetagger analyse le commentaire et renvoie les mots important dans le fichier DataTAG

    for line in D:
        line=line.replace("."," . ")
        tags = tagger.TagText(line.decode(encoding="utf-8"))
        for words in tags:
            w=words.split("\t")
            if(len(w)==1):
                print(w)
            if w[1] in ListeTags:
                Tag.write(w[0]+" ")
        Tag.write("\n")

    #Convertir le fichier en .arff

    #ConvertToArff.main("DataTAG.txt")
def main():
    print("hey\n")
    if len(sys.argv) != 2:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # dataset
        exit(1)

    print("Debut analyse")
    Tagger(sys.argv[1])
    print("fin analyse")
    print("\nBye")
if __name__ == '__main__':
    main()