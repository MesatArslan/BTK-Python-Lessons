import requests
from bs4 import BeautifulSoup

url= "https://www.akakce.com/laptop-notebook.html"

url1 = "https://www.akakce.com"


html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"pw_v8"}, limit=1)

for li in list:
    name = li.span.h3.string
    link = li.a.get("href")
    # print(url1+link)
    price =li.find("div",{"class":"p_w_v9"}).find_all("span")[1].text.strip()
    # print(name)




    print(price)
