import  pymysql
database = pymysql.connect("localhost","root","111111","db",charset = "utf8")

#初始化指针
cursor = database.cursor()

#增
# sql = "INSERT INTO data (date,company,province,price,weight) VALUES ('2023-1-1','河北粮食','河北','2200','45.1')"
# cursor.execute(sql)

#改
#语法：“UPDATE 表名 SET 字段1=内容1，字段2=内容2 WHERE 条件” 条件的写法：字段=内容
# sql1 = "UPDATE date SET data='2023-1-2' WHERE data='2023-1-1'"
# cursor.execute(sql1)
# database.commit()
# database.close()
#查
#语法：“SELECT 字段 FROM 表名 WHERE 条件”
# sql2 = "SELECT * FROM date WHERE data = '2020-08-17'"
# cursor.execute(sql2)
# result = cursor.fetchall()
# print(result)
#删
#语法：“DELETE FROM 表名 WHERE 条件；”
sql3 = "DELETE FROM date WHERE data = '2020-08-17'"
cursor.execute(sql3)
database.commit()
database.close()