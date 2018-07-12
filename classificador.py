from scipy.spatial import distance
from matplotlib import pyplot as plt
import statistics
import copy

class classificador:
    def __init__(self, pathZ1, pathZ2, pathZ3):
        self.z1 = self.getSamples(pathZ1)
        self.z2 = self.getSamples(pathZ2)
        self.z3 = self.getSamples(pathZ3)

    def generateBoxplot(self, method1List, method2List, path):
        data = []
        data.append(method1List)
        data.append(method2List)
        box = plt.boxplot(data, patch_artist=True)
        colors = ['lightgreen', 'tan']
        for patch,color in zip(box['boxes'],colors):
            patch.set_facecolor(color)
        plt.xticks([1, 2], ['Método 1', 'Método 2'])
        plt.ylabel('Erros por execução')
        plt.savefig(path)
        plt.clf()

    def generateGraphs(self, yList1, yList2, xList, path):
        xList = [i+1 for i in xList]
        plt.figure(figsize=(12, 6))
        plt.plot(xList, yList1, 'b--', marker='o', label='Validação')
        plt.plot(xList, yList2, 'r--', marker='o', label='Teste')
        plt.legend(loc='upper right')
        plt.xticks(xList)
        aux1 = max(yList1)
        if aux1 < max(yList2):
            aux1 = max(yList2)
        aux2 = min(yList1)
        if aux2 > min(yList2):
            aux2 = min(yList2)
        plt.ylim(0, aux1+(aux1*0.2))
        #plt.xlim(0, max(xList))
        plt.ylabel('Probabilidade média dos erros por execução (%)')
        plt.xlabel('Número de iterações')
        plt.savefig(path)
        plt.clf()


    def getSamples(self, pathTxt):
        with open(pathTxt) as f:
            samples = f.readlines()
        for i in range(0, len(samples)):
            samples[i] = samples[i].replace('[', '').replace(']', '').replace('\n', '').replace('\'', '').replace(' ', '').split(',')

        for i in range(0, len(samples)):
            for j in range(0, len(samples[i])):
                try:
                    samples[i][j] = float(samples[i][j])
                except ValueError:
                    samples[i][j] = samples[i][j]
         
        return samples
        

    def calculateDist(self, idClass, train=True):
        base_busca = copy.deepcopy(self.z1)
        if train == True:
            base_ref = copy.deepcopy(self.z2)
        elif train == False:
            base_ref = copy.deepcopy(self.z3)
        
        for i in range(0,len(base_ref)):
            #print(base_ref[i])
            base_ref[i].pop(idClass)
            
        for i in range(0,len(base_busca)):
            #print(base_busca[i])
            base_busca[i].pop(idClass)

        distList = []
        for rs in range(0,len(base_ref)):
            distList.append([])
            for bs in range(0,len(base_busca)):
                distList[rs].append([])
                distList[rs][bs].append(distance.euclidean(base_ref[rs], base_busca[bs]))
                distList[rs][bs].append(self.z1[bs])

        return distList


    def calculateError(self, idClass, K, train=True):
        distList = self.calculateDist(idClass, train=train)
        nErrors = 0
        sErrors = []
        for i in range(0,len(distList)):
            distList[i] = sorted(distList[i])
            flag=1
            kn = K
            while(flag==1):
                try:
                    flag=0
                    kClasses = []
                    for k in range(kn):
                        kClasses.append(distList[i][k][1][idClass])
                    attrClass = statistics.mode(kClasses)
                except statistics.StatisticsError:
                    kn=kn-1
                    flag=1
            
            if train == True:
                if self.z2[i][idClass] != attrClass:
                    nErrors=nErrors+1
                    sErrors.append(self.z2[i])
            elif train == False:
                if self.z3[i][idClass] != attrClass:
                    nErrors=nErrors+1
                    sErrors.append(self.z3[i])
        
        return nErrors,sErrors
    
    def findBestK(self, idClass, kList, train=True):
        minNErrors = None
        xList = []
        yList = []
        for k in kList:
            nErrors,sErrors = self.calculateError(idClass, k, train=train)
            xList.append(k)
            yList.append(nErrors)
            if minNErrors == None or nErrors < minNErrors:
                bestK = k
                minNErrors = nErrors
                minSErrors = sErrors

        return minNErrors,minSErrors,bestK

if __name__=='__main__':
    import classificador as cl

    kList = []
    kList.append(1)
    kList.append(3)
    kList.append(5)
    kList.append(9)
    kList.append(11)
    kList.append(13)
    kList.append(15)
    kList.append(17)
    kList.append(19)
    kList.append(21)
    kList.append(23)


    pathZ1 = 'data/ecoli.data/z1.txt'
    pathZ2 = 'data/ecoli.data/z2.txt'
    pathZ3 = 'data/ecoli.data/z3.txt'
    obj = cl.classificador(pathZ1, pathZ2, pathZ3)
    NErrors,SErrors,bestK = obj.findBestK(idClass=7, kList=kList, train=True)
    print('bestK: %i' % bestK)
    print('NErrors: %i' % NErrors)
    print('SErrors: %s\n' % str(SErrors))

    pathZ1 = 'data/iris.data/z1.txt'
    pathZ2 = 'data/iris.data/z2.txt'
    pathZ3 = 'data/iris.data/z3.txt'
    obj = cl.classificador(pathZ1, pathZ2, pathZ3)
    NErrors,SErrors,bestK = obj.findBestK(idClass=4, kList=kList, train=True)
    print('bestK: %i' % bestK)
    print('NErrors: %i' % NErrors)
    print('SErrors: %s\n' % str(SErrors))

    pathZ1 = 'data/seeds.data/z1.txt'
    pathZ2 = 'data/seeds.data/z2.txt'
    pathZ3 = 'data/seeds.data/z3.txt'
    obj = cl.classificador(pathZ1, pathZ2, pathZ3)
    NErrors,SErrors,bestK = obj.findBestK(idClass=7, kList=kList, train=True)
    print('bestK: %i' % bestK)
    print('NErrors: %i' % NErrors)
    print('SErrors: %s\n' % str(SErrors))

    pathZ1 = 'data/wine.data/z1.txt'
    pathZ2 = 'data/wine.data/z2.txt'
    pathZ3 = 'data/wine.data/z3.txt'
    obj = cl.classificador(pathZ1, pathZ2, pathZ3)
    NErrors,SErrors,bestK = obj.findBestK(idClass=0, kList=kList, train=True)
    print('bestK: %i' % bestK)
    print('NErrors: %i' % NErrors)
    print('SErrors: %s\n' % str(SErrors))
     
    pathZ1 = 'data/yeasts.data/z1.txt'
    pathZ2 = 'data/yeasts.data/z2.txt'
    pathZ3 = 'data/yeasts.data/z3.txt'
    obj = cl.classificador(pathZ1, pathZ2, pathZ3)
    NErrors,SErrors,bestK = obj.findBestK(idClass=8, kList=kList, train=True)
    print('bestK: %i' % bestK)
    print('NErrors: %i' % NErrors)
    print('SErrors: %s\n' % str(SErrors))


























