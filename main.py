# -*-coding:utf-8-*-

import csv

from moudle.finData import FinData
from moudle.readMergeFile import ReadMergeFile

def main():

    mergeDict = ReadMergeFile.readFile()
    finData = FinData(mergeDict)
    quoteDailyChangeList = finData.quoteChange('daily')

    csv_columns = ['date','stockChange','dollarChange']
    csv_file = "quoteDailyChange.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for quoteDailyChange in quoteDailyChangeList:
                writer.writerow(quoteDailyChange)
    except IOError:
        print("I/O error") 

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