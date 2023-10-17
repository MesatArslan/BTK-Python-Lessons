import mysql.connector

def getProducts ():
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    # sql = "Select * From Categories"
    # sql = "Select * From Products"
    # sql = "Select * From Products inner join Categories on Categories.id=Prodoucts.Categoryid"
    # sql = "Select Products.name, Products.price, Categories.name From Products inner join Categories on Categories.id=Products.categoryid"
    # sql = "Select Products.name, Products.price, Categories.name From Products inner join Categories on Categories.id=Products.categoryid where categories.name = 'Phone'"
    # sql = "Select Products.name, Products.price, Categories.name From Products inner join Categories on Categories.id=Products.categoryid where Products.name = 'Samsung S5'"
    sql = "Select p.name, p.price, c.name From Products as p inner join Categories as c on c.id=p.categoryid where p.name = 'Samsung S5'"

    cursor.execute(sql)
    try:
        result = cursor.fetchall()
        for product in result:
             print(product)
    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print('Database connection closed.')


getProducts()