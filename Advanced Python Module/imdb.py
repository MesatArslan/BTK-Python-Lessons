import requests
from bs4 import BeautifulSoup



url = "https://chia-anime.cc/popular-anime"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list =soup.find("ul",{"class":"items"}).find_all("li",limit=10)

count = 1
for li in list:

    title = li.find("div",{"class":"thumb_anime"}).find("div").text 
    
    year = li.find("div",{"class":"thumb_anime_hor even"}).find("span",{"class":"time_ago"}).text

    
    print(f"{count}.Movie Name: {title} & Released date: {year}  ")
    count += 1

