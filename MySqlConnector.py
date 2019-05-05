import mysql.connector
mySQLconnection = mysql.connector.connect(host='localhost',
                             database='Cust_db',
                             user='User_dev',
                             password='123456')
Query = "SELECT fname, lname, eid FROM cust1"
cursor = mySQLconnection .cursor()
cursor.execute(Query)
records = cursor.fetchall()
for row in records:
    insertvalues = (row[0]+" "+row[1], row[2])
    InsertQuery = "INSERT INTO cust2 (fullname, eid) VALUES (%s,%s)"
    cursor.execute(InsertQuery, insertvalues)
    connection.commit()

JoinQuery =  "SELECT cust2.fullname, cust1.salary FROM cust1 INNERJOIN cust2 ON cust1.eid = cust2.eid WHERE salary BETWEEN 5000 and 8000"
cursor.execute(JoinQuery)
records1 = cursor.fetchall()
for fullname, salary in records1:
    print(f"{fullname}, {salary}")

NewQuery = 'SELECT COUNT(salary), city FROM cust1 WHERE lname LIKE 'A%S' GROUP BY city'
cursor.execute(NewQuery)
records2 = cursor.fetchall()
for salary, city in records2:
    print(f"{salary}, {city}")

cursor.close()
mySQLconnection.close()
