import mysql.connector

def insertProduct(name,price,imgUrl,description):
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imgUrl,description) VALUES(%s,%s,%s,%s)"
    # values = ("Samsung S5", 1000, "1.jpeg","nice phone")
    values = (name,price,imgUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} product added.')
        print(f'Id {cursor.lastrowid} of the last record.')
    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print("Database connection closed.")


def insertProducts(list):
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imgUrl,description) VALUES(%s,%s,%s,%s)"
    # values = ("Samsung S5", 1000, "1.jpeg","nice phone")
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} products added.')
        print(f'Id {cursor.lastrowid} of the last record.')
    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print("Database connection closed.")


# def getProducts():
#     connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
#     cursor = connection.cursor()

#     # cursor.execute("Select * From Products Where name = 'Iphone 8'") 
#     # cursor.execute("Select * From Products Where price = 3000") 
#     # cursor.execute("Select * From Products Where price = 3000 and name = 'Samsung S8'") 
#     # cursor.execute("Select * From Products Where price = 3000 or name = 'Samsung S8'") 
#     # cursor.execute("Select * From Products Where name LIKE '%samsung%'") # yukarıdaki işlemlerde telefon ismiyle yazdığımız alanın birebir aynı olması gerekiyor lakin bu kısımda telefonun içinde geçen br kısmı yazmamız yeterli oluyor
#     # cursor.execute("Select * From Products Where name LIKE 'Samsung%'")
#     # cursor.execute("Select * From Products Where name LIKE '%samsung'")
#     cursor.execute("Select * From Products Where name LIKE '%samsung%' and price >=3000")

#     result = cursor.fetchall() # dediğimizde tuple listesi şeklinde gelir  fetchall yerine fetchone dersek sadece tek bir eleman gelir

#     for product in result:
#         print(f'id: {product[0]} name: {product[1]},price: {product[2]}')

# getProducts()


def getProductById(id):
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]},price: {result[2]}')

getProductById(1)
