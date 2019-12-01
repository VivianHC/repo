import random
import sys
sys.path.append('..')
from pkg_db.my_db import MyDB
from pkg_generators.birthday_generator import generate_birthday as gbd
from pkg_generators.work_number_generate import generate_work_number as gwn
from pkg_generators.naming_machine import pick_a_full_name_by_sex as pfnbs

db=MyDB()
tbl_name='teacher_info'
is_teacher=True
is_man=1
'''
sql='DELETE FROM %s'% tbl_name
db.cursor.execute(sql)
db.commit()
'''
tid=gwn()
class_code=''
name=pfnbs(is_man)
sex=is_man
birthday=gbd(is_teacher)
in_charge=False

sql = 'INSERT INTO %s '% tbl_name
sql +='(tid,class_code,t_name,t_sex,t_birthday,in_charge)'
sql +='VALUES('
sql += '"%s","%s","%s",%d,"%s",%s' % (
    tid, class_code, name, sex, birthday, in_charge)
sql +=')'
print(name)
db.cursor.execute(sql)
db.commit()

for idx in range(100):
    is_man=random.randint(1,2)
    tid=gwn()
    class_code=''
    name=pfnbs(is_man)
    sex=is_man
    birthday=gbd(is_teacher)
    in_charge=False

    sql='INSERT INTO %s '%tbl_name
    sql+='(tid,class_code,t_name,t_sex,t_birthday,in_charge)'
    sql+='VALUES('
    sql += '"%s","%s","%s",%d,"%s",%s' % (
        tid, class_code, name, sex, birthday, in_charge)
    sql+=')'
    db.cursor.execute(sql)
db.commit()
