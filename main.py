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
    dailyChangeList = finData.quoteDailyChangePerYear()
    regression = Regression(dailyChangeList)
    coef, intercept = regression.cauculatePerYear()

    print(coef, intercept)
    

    # total = []
    # positive = []
    # negative = []

    # for dailyChange in dailyChangeList:
    #     dot = dailyChange['stockChange'] * dailyChange['dollarChange']
    #     total.append(dot)
    #     if dot > 0:
    #         positive.append(dot)
    #     elif dot < 0:
    #         negative.append(dot)
    
    # print(len(positive)/len(total))
    # print(len(negative)/len(total))

    # csv_columns = ['date','stockChange','dollarChange']
    # csv_file = "quoteDailyChange.csv"
    # try:
    #     with open(csv_file, 'w') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #         writer.writeheader()
    #         for quoteDailyChange in quoteDailyChangeList:
    #             writer.writerow(quoteDailyChange)
    # except IOError:
    #     print("I/O error") 

    # for key, value in quoteDailyChangeDict.items():
    #     print(value)


    # stdOne = stdTwo = stdThree = stdFoure = 0
    # for quoteDailyChange in quoteDailyChangeList:
    #     count = quoteDailyChange['stockChange'] * quoteDailyChange['dollarChange']
    #     if count <= totalStd and count >= -totalStd:
    #         stdOne += 1
    #     elif count <= totalStd * 2 and count >= -totalStd * 2:
    #         stdTwo += 1
    #     elif count <= totalStd * 3 and count >= -totalStd * 3:
    #         stdThree += 1
    #     else:
    #         stdFoure += 1
        
    # print(stdOne/totalCount)
    # print(stdTwo/totalCount)
    # print(stdThree/totalCount)
    # print(stdFoure/totalCount)


print(main())