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

  
list=[]
while True: 
    name = input("Product Name: ")
    price = float(input("Product Price: "))
    imgUrl = input("Products Image: ")
    description = input("Product Description: ")

    list.append((name, price, imgUrl, description))
    result = input("Do you want to countinue? (e/h)")
    if result == 'h':
        print('Your records are transferred to database...')
        print(list)
        insertProducts(list)
        break

        
# insertProduct(name,price,imgUrl,description)