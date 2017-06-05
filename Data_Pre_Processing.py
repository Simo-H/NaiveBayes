import pandas as pd
attributeDictionary = {}
with open('C:\\Users\\Simo\\Desktop\\NaiveBayesData\\Structure.txt','r') as dataStructureFile:
    for line in dataStructureFile:
            splitted = line.split();
            attributeDictionary[splitted[1]] = splitted[2]
data = pd.read_csv("C:\\Users\\Simo\\Desktop\\NaiveBayesData\\train.csv");
# groupByclassData = data.groupby('class');
# data.groupby(['class'])['age'].mean()
# print(data.isnull().sum())
print("\n --------------------------------- \n")
for key in attributeDictionary:
    if(attributeDictionary[key] == 'NUMERIC'):
        data[key] = data.groupby("class").transform(lambda x: x.fillna(x.mean()))
        data[key] = pd.cut(data[key], 3,labels=False)
    else:
        max_item = data[key].value_counts().idxmax()
        data[key] = data.groupby("class").transform(lambda x: x.fillna(max_item))
print(data)