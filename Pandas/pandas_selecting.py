import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index= ["A","B","C"], columns= ["Column1","Column2","Column3"])

result = df 
result = df["Column1"]
result= type(df["Column1"])
result = df[["Column1","Column2"]]

#loc["row","column"] ==> loc["row"]    or   loc[:, "column "]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.iloc[1]
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column3"]
result = df.loc[:,:"Column2"]
result = df.loc["A":"B",:"Column2"]
result = df.loc[:"B",:"Column2"]
result = df.loc["A", "Column2"]
result = df.loc["C", "Column3"]
result = df.loc[["A","C"], ["Column3", "Column1"]]

df["Column4"] = pd.Series(randn(3), ["A", "B", "C"])
df["Column5"] = df["Column1"]+ df["Column3"]
print(df.drop("Column5", axis = 1))
# print(df.drop("Column5", axis = 1), inplace = False)
# print(df.drop("Column5", axis = 1), inplace = True)#eğer bunu yapmazsak orijinalinde değişiklik olmaz

print(df)
# print(result)

