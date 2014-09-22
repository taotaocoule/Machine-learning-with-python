from numpy import *
import operator
from os import listdir
def filematrix(filename):
    fr=open(filename)
    arraylines=fr.readlines()
    numberoflines=len(arraylines)
    returnmat=zeros((numberoflines,3))
    classlabel=[]
    index=0
    for line in arraylines:
        line=line.strip()
        listformline=line.split('\t')
        returnmat[index,:]=listformline[0:3]
        classlabel.append(listformline[3])
        index +=1
        return returnmat,classlabel