import sys
sys.path.append('..')
from pkg_db.my_db import MyDB
import random

db = MyDB()
db_name = 'rmgc20_student'
tbl_course = 'course_info'
tbl_teacher = 'teacher_info'
tbl_t_c = 'teacher_course'

sql = 'SELECT cid FROM %s' % tbl_course
db.cursor.execute(sql)
myresult = db.cursor.fetchall()

course_list = []
for row in myresult:
    print('%s' % (row[0]))
    course_list.append(row[0])
print('Read database and fetch data into a list...')
print(course_list)

sql = 'DELETE FROM %s' % tbl_t_c
db.cursor.execute(sql)
db.commit()

sql = 'SELECT tid FROM %s' % tbl_teacher
db.cursor.execute(sql)
myresult = db.cursor.fetchall()

for row in myresult:
    tid = row[0]
    cid = random.choice(course_list)

    sql = 'INSERT INTO %s' % tbl_t_c
    sql += '(tid,cid)'
    sql += 'VALUES('
    sql += '"%s","%s"' % (tid, cid)
    sql += ')'
    db.cursor.execute(sql)
db.commit()

for c in course_list:
    sql = 'SELECT %s.c_name, ' % tbl_course
    sql += '%s.tid, ' % tbl_t_c
    sql += '%s.t_name ' % tbl_teacher
    sql += 'FROM %s,%s,%s ' % (tbl_course, tbl_t_c, tbl_teacher)
    sql += 'WHERE %s.cid="%s" ' % (tbl_course, c)
    sql += 'AND %s.cid=%s.cid ' % (tbl_course, tbl_t_c)
    sql += 'AND %s.tid=%s.tid ' % (tbl_t_c, tbl_teacher)
    db.cursor.execute(sql)
    myresult = db.cursor.fetchall()
    print('Course[%s]------------------------' % c)
    for row in myresult:
        print('%s,%s,%s' % (row[0], row[1], row[2]))
