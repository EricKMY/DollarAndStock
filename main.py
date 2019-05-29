# -*-coding:utf-8-*-

# from moudle.stockData import StockData
# from moudle.moneyData import MoneyData
from moudle.finData import FinData
from moudle.readMergeFile import ReadMergeFile

def main():

    mergeDict = ReadMergeFile.readFile()
    finData = FinData(mergeDict)
    quoteDailyChangeDict = finData.quoteChange('daily')
    quoteWeeklyChangeDict = finData.quoteChange('weekly')
    quoteMonthlyChangeDict = finData.quoteChange('monthly')
    quoteQuartlyChangeDict = finData.quoteChange('quartly')
    # for key, value in quoteDailyChangeDict.items():
    #     print(value)
    positive = 0
    negative = 0

    for key, value in quoteDailyChangeDict.items():

        if value['stockChange'] * value['dollarChange'] > 0:
            positive += 1
        
        elif value['stockChange'] * value['dollarChange'] < 0:
            negative += 1
            
    print(positive)
    print(negative)

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