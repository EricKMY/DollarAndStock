# -*-coding:utf-8-*-

class StockData():

    def quoteChange(timeLen, mergeDict):

        quoteChange = {}

        if timeLen == 'daily':
            i = 0
            oldClose = float(mergeDict['0']['Close_SP'])

            for key, value in mergeDict.items():
                date = mergeDict[key]['Date']

                newClose = float(mergeDict[key]['Close_SP'])
                percentage = (newClose - oldClose) / oldClose * 100
                oldClose = float(mergeDict[key]['Close_SP'])

                if percentage > 0:
                    change = 'rise'
                elif percentage < 0:
                    change = 'fall'
                else:
                    change = 'unchange'

                quoteChange[i] = {'date': date ,'percentage': percentage, 'change': change}
                i += 1
        
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