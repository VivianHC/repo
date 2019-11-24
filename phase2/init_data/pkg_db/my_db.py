import mysql.connector
class MyDB():
    def __init__(self):
        self.__myconn=None
        self.__mycursor=None
        self.get_conn()
        self.get_cursor()
        return
    def get_conn(self):
        self.__myconn=mysql.connector.connect(
            host="localhost",
            database='rmgc20-senior',
            user='mydev',
            password='I-love-HCY99',
            auth_plugin='mysql_native_password'
        )
        return self.__myconn
    def get_cursor(self):
        self.__mycursor=self.__myconn.cursor()
        return
    def commit(self):
        self.__myconn.commit()
        return
    @property
    def conn(self):
        return self.__myconn
    @property
    def cursor(self):
        return self.__mycursor

if __name__=='__main__':
    test_db=MyDB()

    tbl_name='course_info'
    sql='SELECT cid,c_name,introduce \
          From %s'% tbl_name

    test_db.cursor.execute(sql)
    myresult=test_db.cursor.fetchall()
    print(myresult)
    print('----------------------------------------------------------------------')
    for row in myresult:
        print(row[0])
#myresult=[(cid,c-name,introduce)]
