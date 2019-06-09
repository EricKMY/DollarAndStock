# -*-coding:utf-8-*-

class FinData():

    def __init__(self, mergeDict):
        self.mergeDict = mergeDict
    
    def quoteDailyChange(self):

        quoteDailyChange = []
        mergeDict = self.mergeDict
        oldStockClose = float(mergeDict['0']['Close_SP'])
        oldDollarClose = float(mergeDict['0']['Close_US'])

        for key, value in mergeDict.items():

            date = value['Date']

            newStockClose = float(value['Close_SP'])
            stockChange = (newStockClose - oldStockClose) / oldStockClose
            oldStockClose = float(value['Close_SP'])

            newDollarClose = float(value['Close_US'])
            dollarChange = (newDollarClose - oldDollarClose) / oldDollarClose
            oldDollarClose = float(value['Close_US'])

            quoteDailyChange.append({'date': date ,'stockChange': stockChange, 'dollarChange': dollarChange})

        return quoteDailyChange
    
    def quoteDailyChangePerYear(self):
    
        yearList = ['1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        
        quoteDailyChange = []
        mergeDict = self.mergeDict

        for year in yearList:

            quoteDailyChangePerYear = []

            oldStockClose = float(mergeDict['0']['Close_SP'])
            oldDollarClose = float(mergeDict['0']['Close_US'])

            for key, value in mergeDict.items():

                date = value['Date']
                if date.find(year) != -1:

                    newStockClose = float(value['Close_SP'])
                    stockChange = (newStockClose - oldStockClose) / oldStockClose
                    oldStockClose = float(value['Close_SP'])

                    newDollarClose = float(value['Close_US'])
                    dollarChange = (newDollarClose - oldDollarClose) / oldDollarClose
                    oldDollarClose = float(value['Close_US'])

                    quoteDailyChangePerYear.append({'date': date ,'stockChange': stockChange, 'dollarChange': dollarChange})
            
            quoteDailyChange.append(quoteDailyChangePerYear)

        return quoteDailyChange