# -*-coding:utf-8-*-

# from moudle.stockData import StockData
# from moudle.moneyData import MoneyData
from moudle.finData import FinData
from moudle.readMergeFile import ReadMergeFile

def main():

    mergeDict = ReadMergeFile.readFile()
    finData = FinData(mergeDict)
    quoteDailyChange = finData.quoteChange('daily')
    for key, value in quoteDailyChange.items():
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