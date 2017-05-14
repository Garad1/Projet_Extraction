"""
    Adam Garcia : 20133168
    Fati Chen
    Melissa Mekaoui : 21612501
    Pascal Zaragoza : 20130039
"""
import sys
import  os
"""
Fonction qui cree un fichier arff
avec les commentaires du dataset comme attribut
et la classe "classe" qui vaut -1 pour les 5000
premiers commentaires et 1 pour les 5000 restants

@param : fichier contenant les commentaires
@return : void
"""
def Convert(datasetTTG):

# ------------Ouverture des fichiers-----------------#
    comm = open(datasetTTG, 'r')
    A = open("Commentaires.arff", 'w')

# ------------Entete du fichier arff -----------------#
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")

#------------Ecriture sur le fichier arff -----------------#
    i = 0
    while (i < 5000):
        line = "\"%s\",-1\n" % comm.readline().replace("\n", "").replace(",", "").replace("\"", "") # les carracteres speciaux (", et \n) sont remplaces afin d'eviter les conflits
        A.write(line)
        i = i + 1

    while (i < 10000):
        line = "\"%s\",1\n" % comm.readline().replace("\n", "").replace(",", "").replace("\"", "")
        A.write(line)
        i = i + 1

"""
Fonction qui cree un fichier arff
avec les commentaires du dataset comme attribut,
le poids du commentaire selon PNParser
et la classe "classe" qui vaut -1 pour les 5000
premiers commentaires et 1 pour les 5000 restants

@param : fichier contenant les commentaires : datasetTTG
         fichier contenant les poids des commentaires : PNFile
@return : void
"""
def ConvertPN(datasetTTG,PNFile):
# ------------Ouverture des fichiers-----------------#
    dataset = open(datasetTTG, 'r')
    poids = open(PNFile, 'r')
    comms = open("CommentairesPN.arff", 'w')

# ------------Entete du fichier arff -----------------#
    comms.write("@RELATION comment\n")
    comms.write("@ATTRIBUTE comm string\n")
    comms.write("@ATTRIBUTE weight  { 'positive', 'negative', 'neutral'}\n")
    comms.write("@attribute classe {-1,1}\n")
    comms.write("@data\n")
#------------Ecriture sur le fichier arff -----------------#
    i = 0
    while (i < 5000):
        line = "\"" + dataset.readline().replace("\n", "").replace("\"", "'") + "\"," + poids.readline().replace("\n",
                                                                                                               "") + ",-1\n"
        comms.write(line)
        i = i + 1
    while (i < 10000):
        line = "\"" + dataset.readline().replace("\n", "").replace("\"", "'") + "\"," + poids.readline().replace("\n",
                                                                                                               "") + ",1\n"

        comms.write(line)
        i = i + 1
    return 1

"""
Fonction equivalente a Convert ,sauf que les classes valent "?"
"""
def ConvertDataTest(datatestTTG):
# ------------Ouverture des fichiers-----------------#
    comm = open(datatestTTG, 'r')
    A    = open("CommentairesTest.arff", 'w')

# ------------Entete du fichier arff -----------------#
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")

#------------Ecriture sur le fichier arff -----------------#

    i = 0
    while (i <= 4000):
        line = "\"%s\",?\n" % comm.readline().replace("\n", "").replace(",", "").replace("\"",                                                                                        "")  # les carracteres speciaux (", et \n) sont remplaces afin d'eviter les conflits
        A.write(line)
        i+=1

if __name__ == '__main__':
    print("Starting...")

    if len(sys.argv) != 3:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable") #resultat du script TreeTaggerParser
        exit(1)
    elif not os.path.isfile(sys.argv[2]):
        print("Erreur: fichier ", sys.argv[2], "introuvable")  #resultat du script PNParser
        exit(1)

    Convert(sys.argv[1]) #resultat du script TreeTaggerParser
    #ConvertDataTest(sys.argv[1])  # resultat du script TreeTaggerParser sur les tests
    #ConvertPN(sys.argv[1],sys.argv[2]) #resultats du script TreeTaggerParser et PNParser

    print ("\nEnd.")
