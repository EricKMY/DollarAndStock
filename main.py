# -*-coding:utf-8-*-

# from moudle.stockData import StockData
# from moudle.moneyData import MoneyData
from moudle.finData import FinData
from moudle.readMergeFile import ReadMergeFile

def main():

    mergeDict = ReadMergeFile.readFile()
    stockDailyChange = FinData.quoteChange(mergeDict, 'daily', 'stock')
    moneyDailyChange = FinData.quoteChange(mergeDict, 'daily', 'dollar')
    # quoteChange = stockQuoteChange = StockData.quoteChange('daily', mergeDict)
    # for key, value in quoteChange.items():
    #     print(value)
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