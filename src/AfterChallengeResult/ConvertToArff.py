"""
    Adam Garcia : 20133168
    Fati Chen
    Melissa Mekaoui : 21612501
    Pascal Zaragoza : 20130039
"""
import sys
import os.path

"""
Fonction qui cree un fichier arff
avec les commentaires du dataset comme attribut,
les attributs ratiopos et rationeg recuperes de PositiveNegativeParser
et la classe "classe" qui vaut -1 pour les 5000
premiers commentaires et 1 pour les 5000 restants

@param : fichier contenant les commentaires :datasetTTG
         fichier contennat les ratios : ratio
@return : void
"""
def Convert(datasetTTG, ratio):
# ------------Ouverture des fichiers-----------------#
    comm = open(datasetTTG, 'r')
    PN   = open(ratio, "r")
    A    = open("Commentaires.arff", 'w')

# ------------Entete du fichier arff -----------------#
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@ATTRIBUTE ratiopos numeric\n")
    A.write("@ATTRIBUTE ratineg numeric\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")

#------------Ecriture sur le fichier arff -----------------#

    i = 0
    for pn in PN:
        i = i + 1
        if i < 5000:
            line = "\"%s\",%s,-1\n" % (comm.readline().replace("\n", "").replace("\"", "'"),pn[:len(pn)-1])
            A.write(line)

        else:
            line = "\"%s\",%s,1\n" % (comm.readline().replace("\n", "").replace("\"", "'"),pn[:len(pn)-1])
            A.write(line)

"""
Fonction equivalente a Convert ,sauf que les classes valent "?"
"""
def ConvertDataTest(datatest, ratio):
# ------------Ouverture des fichiers-----------------#
    comm = open(datatest, 'r')
    PN   = open(ratio, "r")
    A    = open("CommentairesTest.arff", 'w')

# ------------Entete du fichier arff -----------------#
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE comm string\n")
    A.write("@ATTRIBUTE ratiopos numeric\n")
    A.write("@ATTRIBUTE ratineg numeric\n")
    A.write("@attribute classe {-1,1}\n")
    A.write("@data\n")

#------------Ecriture sur le fichier arff -----------------#

    i = 0
    for pn in PN:
        i = i + 1
        if i <= 4000:
            line = "\"%s\",%s,?\n" % (comm.readline().replace("\n", "").replace("\"", "'"), pn[:len(pn) - 1])
            A.write(line)


if __name__ == '__main__':
    print("Starting...")

    if len(sys.argv) != 3:
        print("Erreur: pas assez d'arguments")
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ", sys.argv[1], "introuvable")  # resultat du script TreeTaggerParser (DataTag.txt)
        exit(1)
    elif not os.path.isfile(sys.argv[2]):
        print("Erreur: fichier ", sys.argv[2], "introuvable")  # resultat du script PNParser (RatioOut.txt)
        exit(1)

    Convert(sys.argv[1],sys.argv[2])
   # ConvertDataTest(sys.argv[1],sys.argv[2]) #resultat du script TreeTaggerParser sur les tests (NewDataTag.txt)
                                            # resultat du script PNParser sur les tests(RatioOut.txt)
    print("End.")
