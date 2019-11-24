# -*- coding: UTF-8 -*-
import random
def generate_work_number():
    yyyy=random.randint(2000,2019)
    serial_number=random.randint(1,99999)
    num='%d-%05d'%(yyyy,serial_number)
    return num
#------------------------------------------------
if __name__=='__main__':
    for idx in range(5):
        print(generate_work_number())
