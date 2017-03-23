'''
Created on Mar 23, 2017

@author: MELY
'''
import sys
import os.path

def main():
   
    comm= open("dataset.csv", 'r')
    A= open("CommentairesTFIDF.arff",'w')
    A.write("@RELATION comment\n")
    A.write("@ATTRIBUTE 'comments' string\n")
    A.write("@attribute 'Class' { positive, negative}\n")
    A.write("@data\n")
    i=0;

    
    while(i<5000):
        line="\"%s\",negative\n" % comm.readline().replace("\n","").replace(",","").replace("\"","")
        A.write(line)
        i=i+1;
    while(i<10000):
        line="\"%s\",positive\n" % comm.readline().replace("\n","").replace(",","").replace("\"","")
        A.write(line)
        i=i+1;

    return 1

if __name__ == '__main__':
    print("hey")
    main()
