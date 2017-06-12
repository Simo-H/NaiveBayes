from Data_Pre_Processing import Data_Pre_Processing
from NaiveBayesModel import NaiveBayesModel

import pandas as pd

class  Preprossing_and_Classfiy:
    def __init__(self, path, bins,m):
        self.path=path;
        self.bins=bins;
        self.DPP;
        self.testSet;
        this.m=m;

    def Bulid(self):
        self.DPP=Data_Pre_Processing(self.path,self.bins)
        self.testSet = Data_Pre_Processing.processTestSet(self.DPP,"",self.bins);
        self.NBM = NaiveBayesModel(DPP.data,DPP.attributeDictionary,this.m);

    def classfiy(self):
        self.NBM(self.path, self.testSet);
        self.Accuracy(self.path, self.testSet);


