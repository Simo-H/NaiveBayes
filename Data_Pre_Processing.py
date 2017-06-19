import pandas as pd
import re
# This class is responsible for reading the structure and data_train files, generating a structure dictionary containing
# all the attributes and class options in a organized manner.
# After generating the structure, the class preparing the training data for building the classifier.
# The data preparation includes filling missing values with legal values.
# If the type of the data is numeric , categorization by bins will be done as well.
class Data_Pre_Processing:

    def __init__(self,path,bins):
        # structure dictionary
        self.attributeDictionary = {}
        self.binsAreGood = True;
        # reading the structure file
        with open(path+"\\Structure.txt",'r') as dataStructureFile:
            for line in dataStructureFile:
                splitted = line.split();
                self.attributeDictionary[splitted[1]] = splitted[2]
        self.data = pd.read_csv(path+"\\train.csv");
        # building the structure dictionary and filling missing value
        for key in self.attributeDictionary:
            if(key == 'class'):
                a = re.split(',', self.attributeDictionary[key][1:-1])
                self.attributeDictionary[key] = a
                continue
            #     handling numeric data
            if(self.attributeDictionary[key] == 'NUMERIC'):
                #checking if the bin number is valid
                if (abs(self.data[key].max() - self.data[key].min()) < bins):
                    # if number of bins is invalid exiting the constuctor and returning false;
                    self.binsAreGood = False;
                    return;
                # filling missing numeric value by class mean
                self.data[key] = self.data.groupby("class").transform(lambda x: x.fillna(x.mean()))[key]
                # categorizing numeric value by bins number.
                self.data[key] = pd.cut(self.data[key], bins,labels=False)
                # updating the structure dictionary with the number of categories
                self.attributeDictionary[key] =range(0,bins) ;
            else:
                # handling categorize data
                a = re.split(',',self.attributeDictionary[key][1:-1])
                self.attributeDictionary[key] = a
                # filling missing values by the most common value.
                b = self.data[key].mode()[0]
                self.data[key].fillna(b,inplace=True)

    # This method reads the test data set and pre processing it, filling missing data and categorizing numeric data in the same manner as the train data.
    def processTestSet(self,path,bins):
        # reading the test data
        testSet = pd.read_csv(path+"\\test.csv");
        # pre processing
        for key in self.attributeDictionary:
            if(key == 'class'):
                continue
            #     handling numeric data
            if(all(isinstance(item, int) for item in self.attributeDictionary[key])):
                testSet[key] = testSet.groupby("class").transform(lambda x: x.fillna(x.mean()))[key]
                testSet[key] = pd.cut(testSet[key], bins,labels=False)
            #     handling categorized data
            else:
                b = testSet[key].mode()[0]
                testSet[key].fillna(b,inplace=True)
        return testSet