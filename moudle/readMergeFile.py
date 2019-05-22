# -*-coding:utf-8-*-

import csv

class ReadMergeFile():
    
    def readFile():

        merge = '../data/merge.csv'
        mergeSimple = './data/merge_simple.csv'
        mergeDict = {}

        with open(mergeSimple, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader :
                mergeDict[row['ID']] = {'Date': row['Date'], 'Close_US': row['Close_US'], 'Close_SP': row['Close_SP']}

        # for key, value in mergeDict.items() :
        #     print(key)
        return mergeDict    
        
