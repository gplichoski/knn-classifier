from random import shuffle
from operator import itemgetter
import os

def split(datasetTxt, ratioSplit, idClass, removeAttr=None):
    with open(datasetTxt) as f:
        dataset = f.readlines()
    
    for i in range(0,len(dataset)):
        dataset[i] = dataset[i].rstrip().split(',')
        if removeAttr != None:
            dataset[i].pop(removeAttr)

    dataset = sorted(dataset, key=itemgetter(idClass))
    currentClass = dataset[0][idClass]
    subset = []
    subset.append([])
    count = 0
    for data in dataset:
        if data[idClass] == currentClass:
            subset[count].append(data)
        else:
            subset.append([])
            count=count+1
            currentClass = data[idClass]

    for s in range(0,len(subset)):
        shuffle(subset[s])
    
    z1,z2,z3 = [],[],[]
    #for s in range(0,len(subset)):
    z1 = [subset[s][i] for s in range(0,len(subset)) for i in range(0, int((ratioSplit/2)*len(subset[s])))]
    z2 = [subset[s][i] for s in range(0,len(subset)) for i in range(int((ratioSplit/2)*len(subset[s])), int(ratioSplit*len(subset[s])))]
    z3 = [subset[s][i] for s in range(0,len(subset)) for i in range(int(ratioSplit*len(subset[s])), len(subset[s]))]

    name = datasetTxt.split('/')
    name = name[len(name)-1]
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/'+name):
        os.mkdir('data/'+name)

    pathZ1 = 'data/' + name + '/z1.txt'
    pathZ2 = 'data/' + name + '/z2.txt'
    pathZ3 = 'data/' + name + '/z3.txt'
    fileZ1 = open(pathZ1, 'w')
    fileZ2 = open(pathZ2, 'w')
    fileZ3 = open(pathZ3, 'w')
    
    for z in z1:
        fileZ1.write('%s\n' % str(z)) 
    for z in z2:
        fileZ2.write('%s\n' % str(z)) 
    for z in z3:
        fileZ3.write('%s\n' % str(z))

    return pathZ1,pathZ2,pathZ3

if __name__=='__main__':
    from geraBases import split

    split('data_raw/ecoli.data', 0.5, 7, 0)
    split('data_raw/iris.data', 0.5, 4)
    split('data_raw/seeds.data', 0.5, 7)
    split('data_raw/wine.data', 0.5, 0)
    split('data_raw/yeasts.data', 0.5, 8, 0)





