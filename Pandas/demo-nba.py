import pandas as pd 
import numpy as np
data = pd.read_csv('nba.csv')

# 1- Get first 10 records.
# print(data.head(10))

# 2- How many records are there in total?
# print(data)

# 3- What is the average weight of all people?
# result = data['player_weight'].mean()

# 4- What is the max weight?
# result = data['player_weight'].max()

# 5- Who is the heaviest player?
# result = data[data['player_weight'] >163]

# 6- Names of players aged between 20 and 25 and the team they play for.
# result = data.query("age >= 20 & age <= 25")[["player_name","team_abbreviation"]]

# 7- Which team does "John Long" play for?
# result1 = data[data['player_name'].str.contains('John Long')]
# result = result1['team_abbreviation']

# 8- Average height information of player by team?
# result = data.groupby('team_abbreviation')['player_height'].mean()
result = data.groupby('team_abbreviation').mean()['player_height']

# 9- How many diffirent teams there are?
# result = data.groupby('team_abbreviation').count()
# result = data.groupby('team_abbreviation').count()

# 10- How many players play in each team?
# result = data.groupby('team_abbreviation')['age'].count()

# 11- Find people whose names contain 'Mik'
# result= data[data['player_name'].str.contains('Mik')]


print(result)
