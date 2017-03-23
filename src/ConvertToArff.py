'''
Created on Mar 23, 2017

@author: MELY
'''
import sys
import os.path

def main():
    print("main")
    Avis= open("DataOut.txt", 'r')
    A= open("Commentaires.arff",'w')
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE 'weight' { 'positive', 'negative', 'neutral'}\n")
    A.write("@attribute 'Class' { 'positive', 'negative'}\n")
    A.write("@data\n")
    i=0;

    
    while(i<5000):
        line="\'%s\',\'negative\'\n" % Avis.readline().replace("\n","")
        A.write(line)
        i=i+1;
    while(i<10000):
        line="\'%s\',\'positive\'\n" % Avis.readline().replace("\n","")
        A.write(line)
        i=i+1;

    return 1

if __name__ == '__main__':
    print("hey")
    main()
