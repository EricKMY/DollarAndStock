# -*-coding:utf-8-*-

import csv
import numpy as np
import matplotlib.pyplot as plt

from moudle.finData import FinData
from moudle.readMergeFile import ReadMergeFile
from moudle.regression import Regression

def main():

    mergeDict = ReadMergeFile.readFile()
    finData = FinData(mergeDict)
    dailyChangeList = finData.quoteDailyChange()
    reg = Regression(dailyChangeList)
    coef, intercept = reg.cauculate()
    print(coef, intercept)

print(main())