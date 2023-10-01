html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My first website</title>
</head>
<body>
    <h1 id="header">
        Python Course
    </h1>


    <div class = "Group 1">
        <h2>Programming</h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>


    <div class = "Group 2">
        <h2>Moduls</h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <div class = "Group 3">
        <h2>Django</h2>

        <ul>
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
        </ul>
    </div>

    <img src="sssddddsss.jpeg" alt="">

    <a cLass="sister" href="http:///example1.com/elsie" id="Link1">Elsie </a>,
    <a cLass="sister" href="http:///example2.com/elsie" id="Link1">Elsie </a>,
    <a cLass="sister" href="http:///example3.com/elsie" id="Link1">Elsie </a>,


</body>
</html>
"""



from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1
result = soup.h2
result = soup.h2.name
result = soup.h2.string

result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]

result = soup.div
result = soup.find_all('div')
result = soup.find_all('div')[1].ul
result = soup.find_all('div')[1].ul.li
result = soup.find_all('div')[1].ul.find_all('li')[2]

result = soup.div.findChildren()

result = soup.div

result = soup.div.findNextSibling()
result = soup.div.findNextSibling().findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()


result = soup.find_all('a')
for links in result:
    # print(links)
    print(links.get('href'))




# print(result)