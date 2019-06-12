# -*-coding:utf-8-*-

import csv
import numpy as np
import matplotlib.pyplot as plt

from moudle.finData import FinData
from moudle.readFile import ReadFile
from moudle.regression import Regression

def main():

#     mergeDict = ReadFile.readMerge()
    changeDict = ReadFile.readChange()
#     finData = FinData(mergeDict)
#     dailyChangeList = finData.quoteDailyChange()
    reg = Regression(changeDict)
    lm = reg.cauculate()
    print(lm.coef_, lm.intercept_)
    reg.score()
    reg.pict()
#     dailyChangeList = finData.quoteDailyChangePerYear()
#     for data in dailyChangeList:
#         reg = Regression(data)
#         coef, intercept = reg.cauculate()
#         print(coef, intercept)
#         reg.pict()

print(main())