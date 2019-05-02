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

JoinQuery =  "select cust2.fullname, cust1.salary from cust1 INNERJOIN cust2 ON cust1.eid = cust2.eid where salary between 5000 and 8000"
cursor.execute(JoinQuery)
records1 = cursor.fetchall()
for fullname, salary in records1:
    print(f"{fullname}, {salary}")
cursor.close()
mySQLconnection.close()
