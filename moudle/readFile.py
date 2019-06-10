# -*-coding:utf-8-*-

import csv

class ReadFile():
    
    def readMerge():

        merge = '../data/merge.csv'
        mergeSimple = './data/merge_simple.csv'
        mergeDict = {}

        with open(mergeSimple, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader :
                mergeDict[row['ID']] = {'Date': row['Date'], 'Close_US': row['Close_US'], 'Close_SP': row['Close_SP']}
                
        return mergeDict    

    def readChange():

        dailyChange = './data/quoteDailyChange.csv'
        dailyChangeDict = {}

        with open(dailyChange, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader :
                dailyChangeDict[row['date']] = {'stockChange': float(row['stockChange']), 'dollarChange': float(row['dollarChange']), 'us10Change': float(row['us10Change']), 'gdpChange': float(row['gdpChange'])}
                
        return dailyChangeDict 
        
