from __future__ import division
import pandas as pd
# This class constructing the classifying naive bayes model
class NaiveBayesModel:
    # the constructor receive the training data and the structure dictionary
    def __init__(self,trainingDataFrame,structure,m):
        self.structure = structure
        # counting the total number of rows (observation) in the training data
        self.TotalNum = trainingDataFrame.shape
        # counting the number of rows for each class
        countClasses = trainingDataFrame.groupby("class")['class'].agg('count')
        self.n = {}
        # saving the amount of each class observation in a simple dictionary
        for i in range(countClasses.index.size):
            self.n[countClasses.index[i]] = countClasses[i]
        #    This is the most important field of the object, containing the calculation of the model for each class and attribute.
        #  This is a complex dictionary holding dictionaries such that each combination of class and attribute is orginized in a easy to understang manner
        # for example m_estimator[class][attribute][specificMode] = Estimator value by the naive bayes equation ----> (Nc + 1/M * m)/(N+m) --- as learned in the classroom
        self.m_estimators = {}
        # grouping data by class
        groupsByClass = trainingDataFrame.groupby('class')
        for Class in structure['class']:
            self.m_estimators[Class] = {}
            # class specific data
            specificClass = groupsByClass.get_group(Class)
            for Attribute in structure:
                if(Attribute != 'class'):
                   #  grouping specific class data by attributes
                   self.m_estimators[Class][Attribute] = {}
                   attributeWithClass = specificClass.groupby(Attribute)[Attribute].agg('count')
                   for i in attributeWithClass.index:
                       # this is the calculation for each option of a specific class and specific attribute
                       self.m_estimators[Class][Attribute][i] = (attributeWithClass[i]+(1/len(structure['class']))*m)/(self.n[Class]+m);
        # checking for unaddressed classes/attribute -- for example : if the training data didnt have a certain class with a certain att
        # filling the value such as Nc is 0;
        for Class in structure['class']:
            for Attribute in structure:
                if (Attribute == 'class'):
                    continue
                for item in structure[Attribute]:
                    if item in self.m_estimators[Class][Attribute]:
                        continue
                    else: self.m_estimators[Class][Attribute][item] = ((1/len(structure['class']))*m)/(self.n[Class]+m)

    # This class classify each row of the test data set and writing the result to an output file by the naive bayes model calculation
    def Classfiy(self,path,testSet):
        # creating new output file overwriting the old file or creating new
        open(path+"\\output.txt", 'w+')
        for row in testSet.itertuples(index=True):
            # This array holds all the calculation for each class of the row (observation in the test set)
            argsArray = []
            for Class in self.structure['class']:
                arg = 1
                for Attribute in self.structure:

                    if(Attribute != 'class'):
                       #  multiplying each estimator for the observed row by class
                       arg = arg*self.m_estimators[Class][Attribute][getattr(row,Attribute)]
                #         adding the class part of the calculation --> multiplying by the probabilty for the class and entering it to an array
                argsArray.append(arg*(self.n[Class]/self.TotalNum[0]))
            #     getting the max value of the class estimation array
            a = argsArray.index(max(argsArray))
            # classifying by the maxed class probability
            classified = self.structure['class'][a]
            # writing the classification to the output file
            with open(path+"\\output.txt", 'a') as output:
                output.write(str(getattr(row,Attribute))+ " "+ classified+"\n")
        print ("finished")


    # a helping method to estimate the accuracy of the model by the test set real classifications
    def Accuracy(self,testData, pathToOutput):
        with open(pathToOutput+"\\output.txt",'r') as f:
            content = f.readlines()
            total = 0
            matching = 0
            for i in range(len(content)):
                total = total + 1
                if(testData['class'].iloc[i] == content[i].split()[1]):
                    matching = matching+1

            print (matching/total)

