import mysql.connector
mySQLconnection = mysql.connector.connect(host='localhost',
                             database='Cust_db',
                             user='User_dev',
                             password='123456')
Query = "select fname, lname, eid from cust1"
cursor = mySQLconnection .cursor()
cursor.execute(Query)
records = cursor.fetchall()
for row in records:
    insertvalues = (row[0]+" "+row[1], row[2])
    InsertQuery = "INSERT INTO cust2 (fullname, eid) VALUES (%s,%s)"
    cursor.execute(InsertQuery, insertvalues)
    connection.commit()
