import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


def find_average(lst: list) -> int:
    sumoavg = sum(lst)
    avg = sumoavg/len(lst)
    return float('%.2f' % avg)


def average_summ_for_month(expenses) -> dict:
    monthinsavg = {}
    avginspermonth = []
    avgsumm = []
    for month in range(1, 13):
        for element in expenses:
            if int(element.d1[3:5]) == month:
                avgsumm.append(int(element.insurance))

        if len(avgsumm) == 0:
            avginspermonth.append(0)
        else:
            avginspermonth.append(find_average(avgsumm))
        avgsumm = []

    monthinsavg['month'] = [x for x in range(1, 13)]
    monthinsavg['insurance'] = avginspermonth

    return monthinsavg


def find_regression(data, month):
    df = pd.DataFrame(data=data)
    X = pd.DataFrame(df.month.values)
    Y = pd.DataFrame(df.insurance)
    model = LinearRegression()
    model.fit(X, Y)

    return  '%.2f' % model.predict([[month]])[0][0]
