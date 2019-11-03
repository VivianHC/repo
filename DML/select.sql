
SELECT*FROM rmgc20zly.students;

SELECT rmgc20zly.students.id,
FROM rmgc20zly.students,
WHERE rmgc20zly.students.name='Lisa'
rmgc20zly.students.sex=0;

-- 查询数据库的记录总数
SELECT COUNT(*) FROM rmgc20zly.students

# Trial 3 查询数据  (查 Select)
print('\n----- 查询所有数据... -----')
sql = "SELECT * FROM rmgc20db.students LIMIT300"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)
