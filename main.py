# -*-coding:utf-8-*-

from moudle.stockData import StockData
from moudle.moneyData import MoneyData

def main():

    stockQuoteChange = StockData.quoteChange('weekly')
    moneyQuoteChange = MoneyData.quoteChange('weekly')

    result = compare(stockQuoteChange, moneyQuoteChange, weeks)

def compare(stockQuoteChange, moneyQuoteChange, dateList):
    result = {}

    for date in dateList:
        if moneyQuoteChange[date] == 0:
            result[date] = 0
        else:
            result[date] = stockQuoteChange[date] / moneyQuoteChange[date]
    
    return result