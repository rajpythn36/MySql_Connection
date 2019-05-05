demotable = sqlContext.read.format("jdbc").options( url="localhost",driver = "com.mysql.jdbc.Driver",dbtable = "demotable",user="root", password="XXXXX").load()
demotable.show()
demotable.take(10)
