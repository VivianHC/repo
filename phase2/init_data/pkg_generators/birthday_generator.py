# -*- coding: UTF-8 -*-
import random
import datetime


def generate_birthday(is_teacher):
    if is_teacher == True:
        yyyy = random.randint(1959, 1995)
    else:
        yyyy = random.randint(2001, 2004)
    mm = random.randint(1, 12)
    if mm == 2:
        dd = random.randint(1, 28)
    elif (mm==4)or(mm == 6)or(mm == 9)or(mm == 11):
        dd = random.randint(1, 30)
    else:
        dd = random.randint(1, 31)
    birthday = datetime.date(yyyy, mm, dd)
    return birthday


# --------------------------------------------------------
if __name__ == '__main__':
    for idx in range(5):
        print(generate_birthday(True))
        print(generate_birthday(False))
