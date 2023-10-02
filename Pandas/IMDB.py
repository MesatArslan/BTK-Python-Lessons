import pandas as pd
import numpy as np
df = pd.read_csv("IMDB.csv")

#1- Information about you in the file.
result = df

#2- Show top 5 posts
result = df.head()

#3- Show top 10 posts
result = df.head(10)

#4- Show last 5 posts
result = df.tail()

#5- Show last 10 posts
result = df.tail(10)

#6 - Just get the Movie_Title column.
result = df["Movie_Title"]

#7 - Only the first 5 containing the Movie_Title column can be saved.
result = df["Movie_Title"].head()

#8- Get only the first 5 records containing Movie_Title and Rating column.
result = df[["Movie_Title","Rating"]].head()

#9- Get only the last 7 records containing Movie Title and Rating column.
result = df[["Movie_Title","Rating"]].head(7)

#10- Get the second 5 portables containing only Movie_Title and Rating column.
result = df[5:][["Movie_Title","Rating"]].head()

#11- Only contains Movie_Title and Rating column and Rating is upper 8
#     Take the first 50 of the records.
result = df[(df["Runtime"] >= 100)][["Movie_Title","Rating","Runtime"]].head(50)

#12 - Get the names of movies whose release date was between 2014 and 2015.
       
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)]["Movie_Title"]


# 13- Number of reviews (Number of Comments) IMDb score more than 100,000
#     List the movies between Rating 8 and 9.
result = df[(df["Rating"] >= 8) & (df["Rating"] <= 9) | (df["Runtime"] >= 100)]

print(result)
