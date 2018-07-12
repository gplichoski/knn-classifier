import classificador as cl
from random import choice
from matplotlib import pyplot as plt
import math
import os

def method1(obj, idClass, kList, stopCriteria, dtName, run):
    # find the best K
    NErrors,SErrors,bestK = obj.findBestK(idClass, kList, train=True)
    kList = [bestK]
    minNErrors = NErrors
    minZ1 = obj.z1
    errListTrain = []
    errListTest = []
    for t in range(stopCriteria):
        errListTest.append(obj.findBestK(idClass, kList, train=False)[0])
        NErrors,SErrors,bestK = obj.findBestK(idClass, kList, train=True)
        errListTrain.append(NErrors)
        if NErrors < minNErrors:
            minNErrors = NErrors
            minZ1 = [s for s in obj.z1]

        samplesList = []
        i = 0
        for e in range(0,len(SErrors)):
            for s in range(i,len(obj.z1)):
                if SErrors[e][idClass] == obj.z1[s][idClass]:
                    samplesList.append(obj.z1[s])
                    i = s+1
                    break
        
        for s in samplesList:
            obj.z1.remove(s)
            obj.z2.append(s)

        for e in range(0,len(samplesList)):
            obj.z2.remove(SErrors[e])
            obj.z1.append(SErrors[e])
    
    NErrors = obj.findBestK(idClass, kList, train=False)[0]
    
    return NErrors,errListTrain,errListTest,bestK
    
def method2(obj, idClass, kList, stopCriteria, dtName, run):
    errListTrain = []
    errListTest = []
    minNErrors = math.inf
    for t in range(stopCriteria):
        #print('Iter: %i\n' % (t))
        NErrors,SErrors,bestK = obj.findBestK(idClass, kList, train=True)
        #print('NErrors: %i\n' % (NErrors))
        #input('...')
        errListTest.append(obj.findBestK(idClass, kList, train=False)[0])
        errListTrain.append(NErrors)
        if NErrors < minNErrors or t==0:
            minNErrors = NErrors
            minBestK = bestK
            minZ1 = [s for s in obj.z1]

        samplesList = []
        i = 0
        for e in range(0,len(SErrors)):
            for s in range(i,len(obj.z1)):
                if SErrors[e][idClass] == obj.z1[s][idClass]:
                    samplesList.append(obj.z1[s])
                    i = s+1
                    break
        
        for s in samplesList:
            obj.z1.remove(s)
            obj.z2.append(s)

        for e in range(0,len(samplesList)):
            obj.z2.remove(SErrors[e])
            obj.z1.append(SErrors[e])
    
    NErrors = obj.findBestK(idClass, kList, train=False)[0]
    
    return NErrors,errListTrain,errListTest,minBestK

if __name__=='__main__':
    import geraBases
    import methods
    import statistics as stat

    # Parameters
    # ratioSplit
    ratioSplit=0.5
    # kList
    maxK = 15
    kList = [i for i in range(maxK+1) if i%2!=0]
    # stopCriteria
    stopCriteria = 30
    # runs
    runs = 30 
  
    ## iris database
    ## idClass
    #idClass = 4
    ## dtName
    #dtName = 'iris'
    #if not os.path.exists(dtName):
        #os.mkdir(dtName) 
    #results = open(dtName + '/results.txt', 'w')
    #testErrorMethod1 = []
    #trainErrorListMethod1 = []
    #testErrorListMethod1 = []
    #bestKList1 = []
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/iris.data', ratioSplit=ratioSplit, idClass=idClass)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method1(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList1.append(bestK)
        #testErrorMethod1.append(NErrors)
        #trainErrorListMethod1.append(errListTrain)
        #testErrorListMethod1.append(errListTest)

    #trainErrorListMeanMethod1 = []
    #for i in range(len(trainErrorListMethod1[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod1)):
            #aux=aux+trainErrorListMethod1[j][i]
        #trainErrorListMeanMethod1.append(aux/len(trainErrorListMethod1))
    
    #testErrorListMeanMethod1 = []
    #for i in range(len(testErrorListMethod1[0])):
        #aux=0
        #for j in range(len(testErrorListMethod1)):
            #aux=aux+testErrorListMethod1[j][i]
        #testErrorListMeanMethod1.append(aux/len(testErrorListMethod1))
    #trainErrorListMeanMethod1 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod1]
    #testErrorListMeanMethod1 = [i*100/len(obj.z3) for i in testErrorListMeanMethod1]
    #obj.generateGraphs(trainErrorListMeanMethod1, testErrorListMeanMethod1, range(stopCriteria), dtName + '/plotMethod1.jpg')

    #testErrorMethod2 = []
    #trainErrorListMethod2 = []
    #testErrorListMethod2 = []
    #bestKList2 =[]
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/iris.data', ratioSplit=ratioSplit, idClass=idClass)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method2(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList2.append(bestK)
        #testErrorMethod2.append(NErrors)
        #trainErrorListMethod2.append(errListTrain)
        #testErrorListMethod2.append(errListTest)

    #trainErrorListMeanMethod2 = []
    #for i in range(len(trainErrorListMethod2[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod2)):
            #aux=aux+trainErrorListMethod2[j][i]
        #trainErrorListMeanMethod2.append(aux/len(trainErrorListMethod2))
    
    #testErrorListMeanMethod2 = []
    #for i in range(len(testErrorListMethod2[0])):
        #aux=0
        #for j in range(len(testErrorListMethod2)):
            #aux=aux+testErrorListMethod2[j][i]
        #testErrorListMeanMethod2.append(aux/len(testErrorListMethod2))
    #trainErrorListMeanMethod2 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod2]
    #testErrorListMeanMethod2 = [i*100/len(obj.z3) for i in testErrorListMeanMethod2]
    #obj.generateGraphs(trainErrorListMeanMethod2, testErrorListMeanMethod2, range(stopCriteria), dtName + '/plotMethod2.jpg')

    #obj.generateBoxplot(testErrorMethod1, testErrorMethod2, dtName + '/boxplot.jpg')

    #results.write('# Runs = %i\n' % (runs))
    #results.write('# stopCriteria = %i\n' % (stopCriteria))
    #results.write('# ratioSplit = %f\n\n' % (ratioSplit*100))
    #results.write('# Method 1\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList1))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod1)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod1),stat.stdev(testErrorMethod1)))
    #results.write('# Method 2\n')
    #results.write(str(bestKList2))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod2)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod2),stat.stdev(testErrorMethod2)))

    #print('Done: %s\n' % (str(dtName)))


    ## ecoli database
    ## idClass
    #idClass = 7
    ## dtName
    #dtName = 'ecoli'
    #if not os.path.exists(dtName):
        #os.mkdir(dtName) 
    #results = open(dtName + '/results.txt', 'w')
    #testErrorMethod1 = []
    #trainErrorListMethod1 = []
    #testErrorListMethod1 = []
    #bestKList1 = []
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/ecoli.data', ratioSplit=ratioSplit, idClass=idClass, removeAttr=0)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method1(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList1.append(bestK)
        #testErrorMethod1.append(NErrors)
        #trainErrorListMethod1.append(errListTrain)
        #testErrorListMethod1.append(errListTest)

    #trainErrorListMeanMethod1 = []
    #for i in range(len(trainErrorListMethod1[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod1)):
            #aux=aux+trainErrorListMethod1[j][i]
        #trainErrorListMeanMethod1.append(aux/len(trainErrorListMethod1))
    
    #testErrorListMeanMethod1 = []
    #for i in range(len(testErrorListMethod1[0])):
        #aux=0
        #for j in range(len(testErrorListMethod1)):
            #aux=aux+testErrorListMethod1[j][i]
        #testErrorListMeanMethod1.append(aux/len(testErrorListMethod1))
    #trainErrorListMeanMethod1 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod1]
    #testErrorListMeanMethod1 = [i*100/len(obj.z3) for i in testErrorListMeanMethod1]
    #obj.generateGraphs(trainErrorListMeanMethod1, testErrorListMeanMethod1, range(stopCriteria), dtName + '/plotMethod1.jpg')

    #testErrorMethod2 = []
    #trainErrorListMethod2 = []
    #testErrorListMethod2 = []
    #bestKList2 = []
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/ecoli.data', ratioSplit=ratioSplit, idClass=idClass, removeAttr=0)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method2(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList2.append(bestK)
        #testErrorMethod2.append(NErrors)
        #trainErrorListMethod2.append(errListTrain)
        #testErrorListMethod2.append(errListTest)

    #trainErrorListMeanMethod2 = []
    #for i in range(len(trainErrorListMethod2[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod2)):
            #aux=aux+trainErrorListMethod2[j][i]
        #trainErrorListMeanMethod2.append(aux/len(trainErrorListMethod2))
    
    #testErrorListMeanMethod2 = []
    #for i in range(len(testErrorListMethod2[0])):
        #aux=0
        #for j in range(len(testErrorListMethod2)):
            #aux=aux+testErrorListMethod2[j][i]
        #testErrorListMeanMethod2.append(aux/len(testErrorListMethod2))
    #trainErrorListMeanMethod2 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod2]
    #testErrorListMeanMethod2 = [i*100/len(obj.z3) for i in testErrorListMeanMethod2]
    #obj.generateGraphs(trainErrorListMeanMethod2, testErrorListMeanMethod2, range(stopCriteria), dtName + '/plotMethod2.jpg')

    #obj.generateBoxplot(testErrorMethod1, testErrorMethod2, dtName + '/boxplot.jpg')

    #results.write('# Runs = %i\n' % (runs))
    #results.write('# stopCriteria = %i\n' % (stopCriteria))
    #results.write('# ratioSplit = %f\n\n' % (ratioSplit*100))
    #results.write('# Method 1\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList1))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod1)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod1),stat.stdev(testErrorMethod1)))
    #results.write('# Method 2\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList2))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod2)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod2),stat.stdev(testErrorMethod2)))

    #print('Done: %s\n' % (str(dtName)))

    ## seeds database
    ## idClass
    #idClass = 7
    ## dtName
    #dtName = 'seeds'
    #if not os.path.exists(dtName):
        #os.mkdir(dtName) 
    #results = open(dtName + '/results.txt', 'w')
    #testErrorMethod1 = []
    #trainErrorListMethod1 = []
    #testErrorListMethod1 = []
    #bestKList1 = []
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/seeds.data', ratioSplit=ratioSplit, idClass=idClass)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method1(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList1.append(bestK)
        #testErrorMethod1.append(NErrors)
        #trainErrorListMethod1.append(errListTrain)
        #testErrorListMethod1.append(errListTest)

    #trainErrorListMeanMethod1 = []
    #for i in range(len(trainErrorListMethod1[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod1)):
            #aux=aux+trainErrorListMethod1[j][i]
        #trainErrorListMeanMethod1.append(aux/len(trainErrorListMethod1))
    
    #testErrorListMeanMethod1 = []
    #for i in range(len(testErrorListMethod1[0])):
        #aux=0
        #for j in range(len(testErrorListMethod1)):
            #aux=aux+testErrorListMethod1[j][i]
        #testErrorListMeanMethod1.append(aux/len(testErrorListMethod1))
    #trainErrorListMeanMethod1 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod1]
    #testErrorListMeanMethod1 = [i*100/len(obj.z3) for i in testErrorListMeanMethod1]
    #obj.generateGraphs(trainErrorListMeanMethod1, testErrorListMeanMethod1, range(stopCriteria), dtName + '/plotMethod1.jpg')

    #testErrorMethod2 = []
    #trainErrorListMethod2 = []
    #testErrorListMethod2 = []
    #bestKList2 =[]
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/seeds.data', ratioSplit=ratioSplit, idClass=idClass)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method2(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList2.append(bestK)
        #testErrorMethod2.append(NErrors)
        #trainErrorListMethod2.append(errListTrain)
        #testErrorListMethod2.append(errListTest)

    #trainErrorListMeanMethod2 = []
    #for i in range(len(trainErrorListMethod2[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod2)):
            #aux=aux+trainErrorListMethod2[j][i]
        #trainErrorListMeanMethod2.append(aux/len(trainErrorListMethod2))
    
    #testErrorListMeanMethod2 = []
    #for i in range(len(testErrorListMethod2[0])):
        #aux=0
        #for j in range(len(testErrorListMethod2)):
            #aux=aux+testErrorListMethod2[j][i]
        #testErrorListMeanMethod2.append(aux/len(testErrorListMethod2))
    #trainErrorListMeanMethod2 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod2]
    #testErrorListMeanMethod2 = [i*100/len(obj.z3) for i in testErrorListMeanMethod2]
    #obj.generateGraphs(trainErrorListMeanMethod2, testErrorListMeanMethod2, range(stopCriteria), dtName + '/plotMethod2.jpg')

    #obj.generateBoxplot(testErrorMethod1, testErrorMethod2, dtName + '/boxplot.jpg')

    #results.write('# Runs = %i\n' % (runs))
    #results.write('# stopCriteria = %i\n' % (stopCriteria))
    #results.write('# ratioSplit = %f\n\n' % (ratioSplit*100))
    #results.write('# Method 1\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList1))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod1)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod1),stat.stdev(testErrorMethod1)))
    #results.write('# Method 2\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList2))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod2)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod2),stat.stdev(testErrorMethod2)))

    #print('Done: %s\n' % (str(dtName)))
    
    ## wine database
    ## idClass
    #idClass = 0
    ## dtName
    #dtName = 'wine'
    #if not os.path.exists(dtName):
        #os.mkdir(dtName) 
    #results = open(dtName + '/results.txt', 'w')
    #testErrorMethod1 = []
    #trainErrorListMethod1 = []
    #testErrorListMethod1 = []
    #bestKList1 = []
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/wine.data', ratioSplit=ratioSplit, idClass=idClass)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method1(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList1.append(bestK)
        #testErrorMethod1.append(NErrors)
        #trainErrorListMethod1.append(errListTrain)
        #testErrorListMethod1.append(errListTest)

    #trainErrorListMeanMethod1 = []
    #for i in range(len(trainErrorListMethod1[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod1)):
            #aux=aux+trainErrorListMethod1[j][i]
        #trainErrorListMeanMethod1.append(aux/len(trainErrorListMethod1))
    
    #testErrorListMeanMethod1 = []
    #for i in range(len(testErrorListMethod1[0])):
        #aux=0
        #for j in range(len(testErrorListMethod1)):
            #aux=aux+testErrorListMethod1[j][i]
        #testErrorListMeanMethod1.append(aux/len(testErrorListMethod1))
    #trainErrorListMeanMethod1 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod1]
    #testErrorListMeanMethod1 = [i*100/len(obj.z3) for i in testErrorListMeanMethod1]
    #obj.generateGraphs(trainErrorListMeanMethod1, testErrorListMeanMethod1, range(stopCriteria), dtName + '/plotMethod1.jpg')

    #testErrorMethod2 = []
    #trainErrorListMethod2 = []
    #testErrorListMethod2 = []
    #bestKList2 = []
    #for r in range(0, runs):
        #pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/wine.data', ratioSplit=ratioSplit, idClass=idClass)
        #obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        #NErrors,errListTrain,errListTest,bestK = methods.method2(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        #bestKList2.append(bestK)
        #testErrorMethod2.append(NErrors)
        #trainErrorListMethod2.append(errListTrain)
        #testErrorListMethod2.append(errListTest)

    #trainErrorListMeanMethod2 = []
    #for i in range(len(trainErrorListMethod2[0])):
        #aux=0
        #for j in range(len(trainErrorListMethod2)):
            #aux=aux+trainErrorListMethod2[j][i]
        #trainErrorListMeanMethod2.append(aux/len(trainErrorListMethod2))
    
    #testErrorListMeanMethod2 = []
    #for i in range(len(testErrorListMethod2[0])):
        #aux=0
        #for j in range(len(testErrorListMethod2)):
            #aux=aux+testErrorListMethod2[j][i]
        #testErrorListMeanMethod2.append(aux/len(testErrorListMethod2))
    #trainErrorListMeanMethod2 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod2]
    #testErrorListMeanMethod2 = [i*100/len(obj.z3) for i in testErrorListMeanMethod2]
    #obj.generateGraphs(trainErrorListMeanMethod2, testErrorListMeanMethod2, range(stopCriteria), dtName + '/plotMethod2.jpg')

    #obj.generateBoxplot(testErrorMethod1, testErrorMethod2, dtName + '/boxplot.jpg')

    #results.write('# Runs = %i\n' % (runs))
    #results.write('# stopCriteria = %i\n' % (stopCriteria))
    #results.write('# ratioSplit = %f\n\n' % (ratioSplit*100))
    #results.write('# Method 1\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList1))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod1)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod1),stat.stdev(testErrorMethod1)))
    #results.write('# Method 2\n')
    #results.write('# bestKs:\n')
    #results.write(str(bestKList2))
    #results.write('\n# Errors\n')
    #results.write('%s\n' % testErrorMethod2)
    #results.write('# mean and standard devitation of Error\n')
    #results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod2),stat.stdev(testErrorMethod2)))
    
    #print('Done: %s\n' % (str(dtName)))
    
    # yeasts database
    # idClass
    idClass = 8
    # dtName
    dtName = 'yeasts'
    if not os.path.exists(dtName):
        os.mkdir(dtName) 
    results = open(dtName + '/results.txt', 'w')
    testErrorMethod1 = []
    trainErrorListMethod1 = []
    testErrorListMethod1 = []
    bestKList1 = []
    for r in range(0, runs):
        pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/yeasts.data', ratioSplit=ratioSplit, idClass=idClass, removeAttr=0)
        obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        NErrors,errListTrain,errListTest,bestK = methods.method1(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        bestKList1.append(bestK)
        testErrorMethod1.append(NErrors)
        trainErrorListMethod1.append(errListTrain)
        testErrorListMethod1.append(errListTest)

    trainErrorListMeanMethod1 = []
    for i in range(len(trainErrorListMethod1[0])):
        aux=0
        for j in range(len(trainErrorListMethod1)):
            aux=aux+trainErrorListMethod1[j][i]
        trainErrorListMeanMethod1.append(aux/len(trainErrorListMethod1))
    
    testErrorListMeanMethod1 = []
    for i in range(len(testErrorListMethod1[0])):
        aux=0
        for j in range(len(testErrorListMethod1)):
            aux=aux+testErrorListMethod1[j][i]
        testErrorListMeanMethod1.append(aux/len(testErrorListMethod1))
    trainErrorListMeanMethod1 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod1]
    testErrorListMeanMethod1 = [i*100/len(obj.z3) for i in testErrorListMeanMethod1]
    obj.generateGraphs(trainErrorListMeanMethod1, testErrorListMeanMethod1, range(stopCriteria), dtName + '/plotMethod1.jpg')

    testErrorMethod2 = []
    trainErrorListMethod2 = []
    testErrorListMethod2 = []
    bestKList2 = []
    for r in range(0, runs):
        pathZ1,pathZ2,pathZ3 = geraBases.split(datasetTxt='../data_raw/yeasts.data', ratioSplit=ratioSplit, idClass=idClass, removeAttr=0)
        obj = cl.classificador(pathZ1,pathZ2,pathZ3)
        NErrors,errListTrain,errListTest,bestK = methods.method2(obj, idClass,kList,stopCriteria, dtName=dtName, run=r)
        bestKList2.append(bestK)
        testErrorMethod2.append(NErrors)
        trainErrorListMethod2.append(errListTrain)
        testErrorListMethod2.append(errListTest)

    trainErrorListMeanMethod2 = []
    for i in range(len(trainErrorListMethod2[0])):
        aux=0
        for j in range(len(trainErrorListMethod2)):
            aux=aux+trainErrorListMethod2[j][i]
        trainErrorListMeanMethod2.append(aux/len(trainErrorListMethod2))
    
    testErrorListMeanMethod2 = []
    for i in range(len(testErrorListMethod2[0])):
        aux=0
        for j in range(len(testErrorListMethod2)):
            aux=aux+testErrorListMethod2[j][i]
        testErrorListMeanMethod2.append(aux/len(testErrorListMethod2))
    trainErrorListMeanMethod2 = [i*100/len(obj.z2) for i in trainErrorListMeanMethod2]
    testErrorListMeanMethod2 = [i*100/len(obj.z3) for i in testErrorListMeanMethod2]
    obj.generateGraphs(trainErrorListMeanMethod2, testErrorListMeanMethod2, range(stopCriteria), dtName + '/plotMethod2.jpg')

    obj.generateBoxplot(testErrorMethod1, testErrorMethod2, dtName + '/boxplot.jpg')
    
    results.write('# Runs = %i\n' % (runs))
    results.write('# stopCriteria = %i\n' % (stopCriteria))
    results.write('# ratioSplit = %f\n\n' % (ratioSplit*100))
    results.write('# Method 1\n')
    results.write('# bestKs:\n')
    results.write(str(bestKList1))
    results.write('\n# Errors\n')
    results.write('%s\n' % testErrorMethod1)
    results.write('# mean and standard devitation of Error\n')
    results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod1),stat.stdev(testErrorMethod1)))
    results.write('# Method 2\n')
    results.write('# bestKs:\n')
    results.write(str(bestKList2))
    results.write('\n# Errors\n')
    results.write('%s\n' % testErrorMethod2)
    results.write('# mean and standard devitation of Error\n')
    results.write('%.2f+-%.2f\n\n' % (stat.mean(testErrorMethod2),stat.stdev(testErrorMethod2)))
    
    print('Done: %s\n' % (str(dtName)))
