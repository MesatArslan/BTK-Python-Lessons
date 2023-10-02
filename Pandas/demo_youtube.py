import pandas as pd 

df = pd.read_csv('datasets/youtube-ing.csv')


# 1- Get the first 10 records.
# result = df.head(10)

# 2- Get the second 5 records.
result = df[5:].head(5)

# 3- Find the column names and numbers in the dataset.
result = df.columns
result = len(df.columns)

# 4- Delete and list some of the columns below.
#  ('thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed','description')
df = df.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed','description'], axis=1)

result = df

# 5- Calculate like and dislike average.
result = df['likes'].mean()
result = df['dislikes'].mean()

# 6- Bring the like and dislike ratio of the first 50 videos.
result = df[['title','likes','dislikes']].head(50)

# 7- What is the most viewed video?
result = df[(df.views.max()) == df['views']]['title'].iloc[0]

# 8- What is the lowest viewed video?
result = df[(df.views.min()) == df['views']]['title'].iloc[0]

# 9- What are the most viewed 10 videos?
result = df.sort_values('views',ascending = False)[['title','views']].head(10)

# 10- Please list the average likes by category in order.
# result = df.groupby('category_id').mean().sort_values('likes')["likes"]

# 11- List the number of comments by category from top to bottom.
# result = df.groupby('category_id').mean().sort_values('comment_count', ascending= False)["comment_count"]

# 12-How many videos are in each category?
# result = df['category_id'].value_counts()

# 3 of theese not working but thats true i'll seaerch.

# 13- Show the title information length of each video in a column.
df['title_len'] = df['title'].apply(len)

# result = df

# 14- Show the number of tags used for each video in a new column
# df['tags_count'] = df['tags'].apply(lambda x: len(x.split('|'))) 
# result = df

def tagCount (tag) :
    return len(tag.split('|'))
df["tag_count"] = df["tags"] .apply (tagCount)

# 15- List the most popular videos.(According to like and dislike ratio)



def likedislikeratiocalculate(dataset):
    likelist = list(dataset['likes'])
    dislikelist = list(dataset['dislikes'])

    liste = list(zip(likelist,dislikelist))

    ratiolist = []

    for like,dislike in liste:
        if (like+dislike) == 0:
            ratiolist.append(0)
        else:
            ratiolist.append(like/(like+dislike))
    return ratiolist

df['like_ratio']= likedislikeratiocalculate(df)

print(df.sort_values('like_ratio', ascending= False)[['title', 'likes', 'dislikes','like_ratio']])
  






likedislikeratiocalculate(df)



