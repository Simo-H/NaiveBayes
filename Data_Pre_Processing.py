import pandas as pd
import re
class Data_Pre_Processing:

    def __init__(self,path,bins):
        self.attributeDictionary = {}
        with open('C:\\Users\\Simo\\Desktop\\NaiveBayesData\\Structure.txt','r') as dataStructureFile:
            for line in dataStructureFile:
                splitted = line.split();
                self.attributeDictionary[splitted[1]] = splitted[2]
        self.data = pd.read_csv("C:\\Users\\Simo\\Desktop\\NaiveBayesData\\train.csv");

        for key in self.attributeDictionary:
            if(key == 'class'):
                a = re.split(',', self.attributeDictionary[key][1:-1])
                self.attributeDictionary[key] = a
                continue
            if(self.attributeDictionary[key] == 'NUMERIC'):
                self.data[key] = self.data.groupby("class").transform(lambda x: x.fillna(x.mean()))
                self.data[key] = pd.cut(self.data[key], bins,labels=False)
                self.attributeDictionary[key] = [0,1,2]
            else:
                a = re.split(',',self.attributeDictionary[key][1:-1])
                self.attributeDictionary[key] = a
                b = self.data[key].mode()[0]
                self.data[key].fillna(b,inplace=True)

    def processTestSet(self,path,bins):
        testSet = pd.read_csv("C:\\Users\\Simo\\Desktop\\NaiveBayesData\\test.csv");
        for key in self.attributeDictionary:
            if(key == 'class'):
                continue
            if(all(isinstance(item, int) for item in self.attributeDictionary[key])):
                testSet[key] = testSet.groupby("class").transform(lambda x: x.fillna(x.mean()))
                testSet[key] = pd.cut(testSet[key], bins,labels=False)
            else:
                b = testSet[key].mode()[0]
                testSet[key].fillna(b,inplace=True)
        return testSet