from Data_Pre_Processing import Data_Pre_Processing
from NaiveBayesModel import NaiveBayesModel

import pandas as pd

class  Preprossing_and_Classfiy:
    def __init__(self, path, bins,m):
        self.path=path;
        self.bins=int(float(bins));
        self.m=int(float(m));

    def Bulid(self):
        self.DPP=Data_Pre_Processing(self.path,self.bins)
        self.testSet = Data_Pre_Processing.processTestSet(self.DPP, "", self.bins);
        self.NBM = NaiveBayesModel(self.DPP.data,self.DPP.attributeDictionary,self.m);

    def Classify(self):
        self.NBM.Classfiy(self.path, self.testSet);
        self.NBM.Accuracy(self.path, self.testSet);


