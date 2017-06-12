from __future__ import division
import pandas as pd

class NaiveBayesModel:


    def __init__(self,trainingDataFrame,structure,m):
        self.structure = structure
        self.TotalNum = trainingDataFrame.shape
        countClasses = trainingDataFrame.groupby("class")['class'].agg('count')
        self.n = {}
        for i in range(countClasses.index.size):
            self.n[countClasses.index[i]] = countClasses[i]
        self.m_estimators = {}
        groupsByClass = trainingDataFrame.groupby('class')
        for Class in structure['class']:
            self.m_estimators[Class] = {}
            specificClass = groupsByClass.get_group(Class)
            for Attribute in structure:
                if(Attribute != 'class'):
                   self.m_estimators[Class][Attribute] = {}
                   attributeWithClass = specificClass.groupby(Attribute)[Attribute].agg('count')
                   for i in range(attributeWithClass.index.size):
                       print(Attribute + " = " + str(len(structure[Attribute])))
                       self.m_estimators[Class][Attribute][attributeWithClass.index[i]] = (attributeWithClass[i]+(1/len(structure[Attribute]))*m)/(self.n[Class]+m);
        for Class in structure['class']:
            for Attribute in structure:
                if (Attribute == 'class'):
                    continue
                for item in structure[Attribute]:
                    if item in self.m_estimators[Class][Attribute]:
                        continue
                    else: self.m_estimators[Class][Attribute][item] = ((1/len(structure[Attribute]))*m)/(self.n[Class]+m)


    def Classfiy(self,path,testSet):
        open('C:\\Users\\Stav\\Desktop\\output.txt', 'w+')
        for row in testSet.itertuples(index=True):
            argsArray = []
            for Class in self.structure['class']:
                arg = 1
                for Attribute in self.structure:

                    if(Attribute != 'class'):
                       arg = arg*self.m_estimators[Class][Attribute][getattr(row,Attribute)]
                argsArray.append(arg*(self.n[Class]/self.TotalNum[0]))
            a = argsArray.index(max(argsArray))
            classified = self.structure['class'][a]
            with open('C:\\Users\\Stav\\Desktop\\output.txt', 'a') as output:
                output.write(str(getattr(row,Attribute))+ " "+ classified+"\n")
        print ("finished")

    def Accuracy(self,testData, pathToOutput):
        with open('C:\\Users\\Stav\\Desktop\\output.txt','r') as f:
            content = f.readlines()
            total = 0
            matching = 0
            for i in range(len(content)):
                total = total + 1
                if(testData['class'].iloc[i] == content[i].split()[1]):
                    matching = matching+1

            print (matching/total)

