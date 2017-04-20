'''
Created on Mar 4, 2017

@author: MELY
'''
import sys
import os.path

def positif(posW,word):
    PW= open(posW,'r')

    for line in PW:
        if word == line.strip():
            return True
        
    return False

def negatif(negW,word):
    NW= open(negW,'r')
    for line in NW:
        if word == line.strip():
            return True
        
    return False
def analyse(dataset,posW,negW):
    D= open(dataset,'r')
    Out= open("DataOut.txt",'a')
    
    pos=0
    neg=0
    i=1

    for line in D:
        words =line.split(' ')
        for w in words:
            if positif(posW,w):
                pos=pos+1
            elif negatif(negW, w):
                neg=neg+1
        if pos>neg+2:
           # print(i,": avis positif ( ",pos," vs",neg,")")
            Out.write("positive\n")
        elif neg>pos+2:
            #print(i,": avis negatif ( ",pos," vs", neg,")")
            Out.write("negative\n")
        else:
            #print(i, ": avis neutre ( ",pos," vs", neg,")")
            Out.write("neutral\n")
        i=i+1
        pos=0
        neg=0
            
    
    return 1

def main():
    if len(sys.argv) != 4: 
        print("Erreur: pas assez d'arguments") 
        exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Erreur: fichier ",sys.argv[1],"introuvable") #dataset
        exit(1)
    elif not os.path.isfile(sys.argv[2]):
        print("Erreur: fichier ",sys.argv[2],"introuvable") #positif words
        exit(1)
    elif not os.path.isfile(sys.argv[3]):
        print("Erreur: fichier ",sys.argv[3],"introuvable") #negatif words
        exit(1)
    print("Debut analyse")
    analyse(sys.argv[1],sys.argv[2],sys.argv[3])
    print("fin analyse")
        
    return 1

if __name__ == '__main__':
    main()
