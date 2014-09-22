from numpy import *
import operator
def classify(inX,dataset,labels,k):
    datasetsize=dataset.shape[0]
    diffmat=tile(inX,(datasetsize,1))-dataset
    sqdiffmat=diffmat**2
    sqdistance=sqdiffmat.sum(axis=1)
    distance=sqdistance**0.5
    sortdistance=distance.argsort()
    classcount={}
    for i in range(k):
        votelabel=labels[sortdistance[i]]
        classcount[votelabel]=classcount.get(votelabel,0)+1
        sortclasscount=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
        return sortclasscount[0][0]


