# -*-coding:utf-8-*-

import csv

from moudle.finData import FinData
from moudle.readMergeFile import ReadMergeFile

def main():

    mergeDict = ReadMergeFile.readFile()
    finData = FinData(mergeDict)
    quoteDailyChangeDict = finData.quoteChange('daily')

    with open('quoteDailyChange.csv', 'w') as f:
        for key in quoteDailyChangeDict.keys():
            f.write("%s,%s\n"%(key,quoteDailyChangeDict[key]))

    # for key, value in quoteDailyChangeDict.items():
    #     print(value)

    # positive = 0
    # negative = 0

    # for key, value in quoteDailyChangeDict.items():

    #     if value['stockChange'] * value['dollarChange'] > 0:
    #         positive += 1
        
    #     elif value['stockChange'] * value['dollarChange'] < 0:
    #         negative += 1
            
    # print(positive)
    # print(negative)


print(main())