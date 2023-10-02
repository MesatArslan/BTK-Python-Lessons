import pandas as pd


list= [["Ahmet",50],["Ali",60],["Yağmur",70],["Çinar",80]]
dict = {"Name": ['Ahmet','Ali','Yağmur','Çinar'], "Grade": [50,60,70,80]}
dict_list= [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":70},
                {"Name":"Yağmur","Grade":80},
                {"Name":"Çinar","Grade":90}
           ]



# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(list ,index = [1,2,3,4], columns = ['Name','Grade'], dtype = float)
# df = pd.DataFrame(dict, index = ['232','323', '454','567'])
df = pd.DataFrame(dict_list, index = ['232','323', '454','567'])




print(df)





# s1 = pd.Series([3,2,1,0])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)