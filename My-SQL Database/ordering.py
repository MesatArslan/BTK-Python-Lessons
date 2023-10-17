import mysql.connector


def getProducts ():
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    # cursor.execute("Select * From Products Order By id ")
    # cursor.execute("Select * From Products Order By name ")
    # cursor.execute("Select * From Products Order By price ")
    cursor.execute("Select * From Products Order By name ,price ")
    try:
        result = cursor.fetchall()
        for product in result:
             print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print('Database connection closed.')
    
    
    
    

getProducts()