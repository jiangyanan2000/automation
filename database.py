import  pymysql
database = pymysql.connect("localhost","root","111111","db",charset = "utf8")

#初始化指针
cursor = database.cursor()

#增
sql = "INSERT INTO data (date,company,province,price,weight) VALUES ('2023-1-1','河北粮食','河北','2200','45.1')"
cursor.execute(sql)

#改
sql1 = "UPDATE date SET data='2023-1-2' WHERE data='2023-1-1'"
cursor.execute(sql1)
database.commit()
database.close()
