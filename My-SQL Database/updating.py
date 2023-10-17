import mysql.connector
   


# def updateProduct():
def updateProduct( id, name , price):
    connection = mysql.connector.connect(
        host = 'localhost', #192.23.43.57
        user = 'root',
        password = 'Justmysql1234',
        database = 'node-app'
    )
    cursor = connection.cursor()

    # sql = "Update products Set name = 'Samsung S10' where id = 5"
    # sql = "Update products Set name = 'Samsung S11' ,price = 6000 where id = 2"
    sql = "Update products Set name =%s, price = %s where id = %s"
   
    values = (name, price, id)
    cursor.execute(sql, values)

    try:
        connection.commit ()
        print (f'{cursor.rowcount} record updated.')
    except mysql.connector.Error as err:
        print ('Error', err)
    finally:
        connection.close()
        print('Database connection closed.')

# updateProduct()
updateProduct(1, 'Iphone-10', 7000)
    

