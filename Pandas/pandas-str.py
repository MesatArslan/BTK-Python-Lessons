import pandas as pd

data = pd.read_csv('nba.csv')

data.dropna(inplace = True)

# data['player_name'] = data['player_name'].str.upper()
# data['player_name'] = data['player_name'].str.lower()
# data['index'] = data['player_name'].str.find('a')
# data = data['player_name'].str.contains('Ed')
# data = data[data.player_name.str.contains('Ed')]
# data = data.player_name.str.replace(' ','-')
data[['FirstName','LastName']] = data['player_name'].loc[data['player_name'].str.split().str.len() == 2].str.split(expand= True)




print(data.head(10))