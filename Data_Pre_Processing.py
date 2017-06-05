import pandas as pd
import re
class Data_Pre_Processing:

    def __init__(self,path):
        self.attributeDictionary = {}
        with open('C:\\Users\\Simo\\Desktop\\NaiveBayesData\\Structure.txt','r') as dataStructureFile:
            for line in dataStructureFile:
                splitted = line.split();
                self.attributeDictionary[splitted[1]] = splitted[2]
        self.data = pd.read_csv("C:\\Users\\Simo\\Desktop\\NaiveBayesData\\train.csv");
        # groupByclassData = data.groupby('class');
        # data.groupby(['class'])['age'].mean()
        # print(data.isnull().sum())
        for key in self.attributeDictionary:
            if(key == 'class'):
                a = re.split(',', self.attributeDictionary[key][1:-1])
                self.attributeDictionary[key] = a
                continue
            if(self.attributeDictionary[key] == 'NUMERIC'):
                self.data[key] = self.data.groupby("class").transform(lambda x: x.fillna(x.mean()))
                self.data[key] = pd.cut(self.data[key], 3,labels=False)
                self.attributeDictionary[key] = [0,1,2]
            else:
                a = re.split(',',self.attributeDictionary[key][1:-1])
                self.attributeDictionary[key] = a
                max_item = self.data[key].value_counts().idxmax()
                self.data[key] = self.data.groupby("class").transform(lambda x: x.fillna(max_item))
