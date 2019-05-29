# -*-coding:utf-8-*-

from moudle.stockData import StockData
from moudle.moneyData import MoneyData
from moudle.readMergeFile import ReadMergeFile

def main():

    mergeDict = ReadMergeFile.readFile()
    quoteChange = stockQuoteChange = StockData.quoteChange('daily', mergeDict)
    for key, value in quoteChange.items():
        print(value)
    # moneyQuoteChange = MoneyData.quoteChange('weekly')

    # result = compare(stockQuoteChange, moneyQuoteChange, weeks)

# def compare(stockQuoteChange, moneyQuoteChange, dateList):
#     result = {}

#     for date in dateList:
#         if moneyQuoteChange[date] == 0:
#             result[date] = 0
#         else:
#             result[date] = stockQuoteChange[date] / moneyQuoteChange[date]
    
#     return result

print(main())