from Data_Pre_Processing import Data_Pre_Processing
from NaiveBayesModel import NaiveBayesModel
import pandas as pd
path = 'C:\\Users\\Simo\\Desktop\\NaiveBayesData\\Structure.txt'
DPP = Data_Pre_Processing(path)
NBM = NaiveBayesModel(DPP.data,DPP.attributeDictionary,2)
