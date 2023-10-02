import pandas as pd 
import numpy as np

data = {
    'Column1' : [1,2,3,4,5],
    'Column2' : [10,20,13,20,50],
    'Column3' : ['abcd', 'bca','ae','cda','dea']
}

df = pd.DataFrame(data)

def squareit(x):
    return x * x

squareit2 = lambda x: x * x

result = df
result = df['Column2'].unique()# tekrarlanan sayıları eleriz
result = df['Column2'].nunique()
result = df['Column2'].value_counts()
result = df['Column1'] * 2
result = df['Column1'].apply(squareit)
result = df['Column1'].apply(squareit2)
result = df['Column1'].apply(lambda x: x * x)
result = df['Column3'].apply(len)
df['Column4'] = df['Column3'].apply(len)

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values('Column2')
result = df.sort_values('Column3')
result = df.sort_values('Column3', ascending= False)

data = {
"Ay": ["Mayis", "Haziran", "Nisan", "Mayis", "Haziran", "Nisan","Mayis","Haziran","Nisan"],
"Kategori":["Elektronik", "Elektronik" ,"Elektronik", "Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
"Gelir": [20,30, 15, 14, 32,42, 12, 36,52]
}

df = pd.DataFrame(data)
print(df.pivot_table(index = "Ay", columns= "Kategori",values= "Gelir" ))

# print(result)