# -*-coding:utf-8-*-

import numpy as np
from sklearn.linear_model import LinearRegression

class Regression():

    def __init__(self, dataList):
        self.dataList = dataList
    
    def cauculate(self):

        XList = []
        yList = []

        for data in self.dataList:
            XList.append([data['dollarChange']])
            yList.append(data['stockChange'])

        X = np.array(XList)
        y = np.array(yList)

        lm = LinearRegression()
        lm.fit(X,y)

        return(lm.coef_, lm.intercept_)
    
    def cauculatePerYear(self):
        
        XList = []
        yList = []

        for data in self.dataList:
            XList.append([data['dollarChange']])
            yList.append(data['stockChange'])

        X = np.array(XList)
        y = np.array(yList)

        lm = LinearRegression()
        lm.fit(X,y)

        return(lm.coef_, lm.intercept_)


