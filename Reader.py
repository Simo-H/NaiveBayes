import pandas as pd
attributeDictionary = {}
with open('C:\\Users\\Simo\\Desktop\\NaiveBayesData\\Structure.txt','r') as dataStructureFile:
    for line in dataStructureFile:
            splitted = line.split();
            attributeDictionary[splitted[1]] = splitted[2]
data = pd.read_csv("C:\\Users\\Simo\\Desktop\\NaiveBayesData\\test.csv");
# groupByclassData = data.groupby('class');
# data.groupby(['class'])['age'].mean()
ageAvg = data.groupby(['class'],as_index=True)['age'].mean()

print ()