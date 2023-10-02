import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index =["a","c","e","f","h"], columns= ["Column1","Column2","Column4"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column3"] = newColumn
result = df
result = df.drop(["Column1","Column2"], axis= 1) #1 column
result = df.drop('a', axis= 0)#0 row
result = df.drop(['a','b','c'], axis= 0)
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["Column1"].isnull().sum()
result = df["Column1"].isnull()
result = df[df["Column1"].isnull()]["Column1"]
result = df[df["Column1"].notnull()]["Column1"]
result = df[df["Column1"].notnull()]
result = df.dropna()
result = df.dropna(axis= 1)
result = df.dropna(how = 'any')
result = df.dropna(how = 'all')
result = df.dropna(subset = ['Column1','Column2'], how = 'all')
result = df.dropna(subset = ['Column1','Column2'], how = 'any')
result = df.dropna(thresh= 2)
result = df.dropna(thresh= 4) # en az sayıda normal veri

result = df.fillna(value = ' no input')
result = df.fillna(value = 1)

result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()
result = df.isnull().sum().sum()


def average(df):
    total = df.sum().sum()
    piece = df.size - df.isnull().sum().sum()
    return total / piece

result = df.fillna(value = average(df))




print(df)
print(result)

