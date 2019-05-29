# -*-coding:utf-8-*-

class FinData():

    def __init__(self, mergeDict):
        self.mergeDict = mergeDict

    def quoteChange(self, timeLen):

        if timeLen == 'daily':
            quoteChange = self.dailyChange()

        elif timeLen == 'weekly':
            pass
        
        elif timeLen == 'monthly':
            pass
            
        elif timeLen == 'quartly':
            pass
        
        elif timeLen == 'yearly':
            pass

        else:
            print('timeLen error: ' + timeLen)

        return quoteChange
    
    def dailyChange(self):

        
        i = 0
        quoteChange = {}
        mergeDict = self.mergeDict
        oldStockClose = float(mergeDict['0']['Close_SP'])
        oldDollarClose = float(mergeDict['0']['Close_US'])

        for key, value in mergeDict.items():

            date = mergeDict[key]['Date']

            newStockClose = float(mergeDict[key]['Close_SP'])
            stockChange = (newStockClose - oldStockClose) / oldStockClose * 100
            oldStockClose = float(mergeDict[key]['Close_SP'])

            newDollarClose = float(mergeDict[key]['Close_US'])
            dollarChange = (newDollarClose - oldDollarClose) / oldDollarClose * 100
            oldDollarClose = float(mergeDict[key]['Close_US'])

            quoteChange[i] = {'date': date ,'stockChange': stockChange, 'dollarChange': dollarChange}
            i += 1

        return quoteChange