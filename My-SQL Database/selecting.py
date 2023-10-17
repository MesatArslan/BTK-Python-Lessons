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


def getProducts():
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    # cursor.execute('Select * From Products') # bütün kolonları alıyoruz
    cursor.execute('Select name,price From Products') # bütün kolonları almaktansa sadece işimize yarayan kolonları alıyoruz

    # result = cursor.fetchall()
    result = cursor.fetchone()
    print(f'name: {result[0]},price: {result[1]}')


    # for product in result:
    #     # print(f'name: {product[1]},price: {product[2]}')
    #     print(f'name: {product[0]},price: {product[1]}')
getProducts()
