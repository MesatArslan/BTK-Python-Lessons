import mysql.connector

def getProductInfo():
    connection = mysql.connector.connect( host ='localhost', user = 'root',password='Justmysql1234', database = 'node-app')
    cursor = connection.cursor()

    # sql = "Select COUNT(*)From Products"
    # sql = "Select COUNT(*)From Products WHERE price >2000"
    # sql = "Select AVG(price)From Products"
    # sql = "Select SUM(price)From Products"
    # sql = "Select MAX(price)From Products"
    # sql = "Select MIN(price)From Products"
    sql = "Select Name From Products WHERE price = (Select MIN(price)From Products)"
 


    cursor.execute(sql)

    result = cursor.fetchone()

    print(f'result: {result[0]}')

getProductInfo()