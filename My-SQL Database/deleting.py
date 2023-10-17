import mysql.connector


def deleteProduct(id):
    
    connection = mysql.connector.connect(
        host = 'localhost', #192.23.43.57
        user = 'root',
        password = 'Justmysql1234',
        database = 'node-app'
    )
    cursor = connection.cursor()

    # sql = "delete from products where id = 6"
    # sql = "delete from products where name like '%S6%' "
    sql = "delete from products where id = %s "
    values = (id,)
   
    cursor.execute(sql, values)
 
    try:
        connection.commit ()
        print (f'{cursor.rowcount} record deleted.')
    except mysql.connector.Error as err:
        print ('Error', err)
    finally:
        connection.close()
        print('Database connection closed.')

# deleteProduct()
deleteProduct(5)