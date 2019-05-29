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
            quoteChange = self.monthlyChange()
            
        elif timeLen == 'quartly':
            pass
        
        elif timeLen == 'yearly':
            pass

        else:
            print('timeLen error: ' + timeLen)

        return quoteChange
    
    def dailyChange(self):

        quoteChange = []
        mergeDict = self.mergeDict
        oldStockClose = float(mergeDict['0']['Close_SP'])
        oldDollarClose = float(mergeDict['0']['Close_US'])

        for key, value in mergeDict.items():

            date = value['Date']

            newStockClose = float(value['Close_SP'])
            stockChange = (newStockClose - oldStockClose) / oldStockClose * 100
            oldStockClose = float(value['Close_SP'])

            newDollarClose = float(value['Close_US'])
            dollarChange = (newDollarClose - oldDollarClose) / oldDollarClose * 100
            oldDollarClose = float(value['Close_US'])

            quoteChange.append({'date': date ,'stockChange': stockChange, 'dollarChange': dollarChange})

        return quoteChange
    
    
    def monthlyChange(self):
        
        i = 0
        quoteChange = []
        mergeDict = self.mergeDict
        oldStockClose = float(mergeDict['0']['Close_SP'])
        oldDollarClose = float(mergeDict['0']['Close_US'])

        for key, value in mergeDict.items():
            
            if self.isEndOfMonth(value['Date']):

                newStockClose = float(value['Close_SP'])
                stockChange = (newStockClose - oldStockClose) / oldStockClose * 100
                oldStockClose = float(value['Close_SP'])

                newDollarClose = float(value['Close_US'])
                dollarChange = (newDollarClose - oldDollarClose) / oldDollarClose * 100
                oldDollarClose = float(value['Close_US'])

                quoteChange[i] = {'date': value['Date'] ,'stockChange': stockChange, 'dollarChange': dollarChange}

    
    def isEndOfMonth(date):

        date = date.split('/')


        return True