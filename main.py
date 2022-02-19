import json

from peewee import *
from logic.models import *
from loguru import logger
from logic.logic import average_summ_for_month, find_regression

with db:
    expenses = Expenses.select().order_by(Expenses.d1)
    data = average_summ_for_month(expenses)

    singleornot = input("""Predict 1 month? \n(Y if you wonna see single month)\n(N if you wonna see 12 months):  """)
    if singleornot.lower() == 'y':
        try:
            whichmonth = int(input("1 = January, 2 = February, 3 = March, 4 = April,\n5 = May, 6 = June, 7 = July, 8 = August,\n9 = September, 10 = October, 11 = November, 12 = December\nwhich month? : "))
            if whichmonth > 0 and whichmonth < 13:
                print('For {} month prediction is {} '.format(whichmonth, find_regression(data, whichmonth)))
                input()
        except:
            logger.error("Wrong Input! | Number must be in ranger from 1 to 12 | Try again")
    elif singleornot.lower() == 'n':
        allmonths = {}
        for month in range(1, 13):
            allmonths[month] = float(find_regression(data, month))
        print('For all months prediction is\n {}'.format(allmonths))
        with open("allmonths.json", "w") as file:
            json.dump(allmonths, file)
    else:
        print('Wrong input')
