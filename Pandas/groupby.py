import pandas as pd 
import numpy as np

personnels = {
    'Worker' : ["Ahmet Yimaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Riza Ertürk","Mustafa Can"],
    'Department' : ["İnsan Kaynaklari","Bilgi islem","Muhasebe","İnsan Kaynaklari","Bilgi islem","Muhasebe","Bilgi islem"],
    'Age' : [30, 25,45, 50, 23,34, 42],
    'District' : ["Kadiköy","Tuzla","Maltepe","Tuzla","Kadiköy","Tuzla","Maltepe"],
    'Salary' : [15000,13000,14000,13500,12750,16500,14500]
}

df = pd.DataFrame(personnels)

result = df
result = df["Salary"].sum()
result = df.groupby(['Department','District']).groups

# districts = df.groupby('District')

# for name,group in df.groupby('District'):#yada districts
#     print(name)
#     print(group)


# for name,group in df.groupby('Department'):#yada districts
#     print(name)
#     print(group)

result = df.groupby('District').get_group('Kadiköy')
result = df.groupby('District').get_group('Maltepe')

result = df.groupby('Department').get_group('Muhasebe')
result = df.groupby('Department').get_group('Bilgi islem')
result = df.groupby('Department').sum()
result = df.groupby('Department').sum('Salary')
result = df.groupby('Department')['Salary'].mean()
result = df.groupby('District')['Age'].mean()
result = df.groupby('District')['Salary'].mean()
result = df.groupby('District')['Worker'].count()
result = df.groupby('Department')['Age'].max() 
result = df.groupby('Department')['Age'].min() 
result = df.groupby('Department')['Salary'].min() 
result = df.groupby('Department')['Salary'].max()['Muhasebe']
result = df.groupby('Department')['Salary'].agg(np.sum)
result = df.groupby('Department')['Salary'].agg(np.max)



print(result)