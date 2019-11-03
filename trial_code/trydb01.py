import mysql.connector
import random
# Trial 1  数据库的连接
print('\n----- 建立数据库链接... -----')
myconn = mysql.connector.connect(
    host='localhost',
    database='rmgc20zly',
    user='rmgc20ytt',
    password='I-love-HCY99',
    auth_plugin='mysql_native_password',
)
#print(myconn)
mycursor = myconn.cursor()

print('\n-----插入一条数据...-----')
sql='INSERT INTO rmgc20zly.students(name,sex,birthday)\
     VALUES(%s,%s,%s)'
val=('Lisa',0,'2004/4/15')
mycursor.execute(sql,val)
myconn.commit()

rows=100000
print('\n-----插入%d条数据...-----'%rows)
for idx in range(rows):
    name='Lisa%03d'%idx
    sex=random.randint(0,1)
    birthday='2004/4/15'
    val=(name,sex,birthday)
    mycursor.execute(sql,val)
myconn.commit()

# Trial 3 查询数据  (查 Select)
print('\n----- 查询所有数据... -----')
sql = "SELECT * FROM rmgc20zly.students LIMIT300"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)
