import pandas as pd
class NaiveBayesModel:

    def __init__(self,trainingDataFrame,structure,m):
        countClasses = trainingDataFrame.groupby("class")['class'].agg('count')
        n = {}
        for i in range(countClasses.index.size):
            n[countClasses.index[i]] = countClasses[i]
        self.m_estimators = {}
        groupsByClass = trainingDataFrame.groupby('class')
        for Class in structure['class']:
            self.m_estimators[Class] = {}
            specificClass = groupsByClass.get_group(Class)
            for Attribute in structure:
                if(Attribute != 'class'):
                    self.m_estimators[Class][Attribute] = {}
                    attCount = specificClass.groupby(Attribute)[Attribute].agg('count')
                    a = attCount.index[i]
                    b = attCount[i]
                    for i in range(attCount.index.size):
                        self.m_estimators[Class][Attribute][attCount.index[i]] = attCount[i];
        print(self.m_estimators)






    def estimate(self,trainingDataFrame,Attribute,Class,m,n):
         a = trainingDataFrame.groupby(['class',Attribute])[Attribute].agg('count')



    def Classfiy(self):
        print()