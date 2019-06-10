# -*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression

class Regression():

    def __init__(self, dataDict):
        self.dataDict = dataDict
    
    def cauculate(self):

        XList = []
        yList = []

        for key, val in self.dataDict.items():

            value = val['dollarChange']
            XList.append([value])
            yList.append(val['stockChange'])

        self.X = np.array(XList)
        self.y = np.array(yList)

        self.lm = LinearRegression()
        self.lm.fit(self.X,self.y)

        return self.lm
    
    def score(self):

        lm = self.lm
        X = self.X
        y = self.y

        mse = np.mean((lm.predict(X) - y) ** 2)
        r_squared = lm.score(X, y)
        adj_r_squared = r_squared - (1 - r_squared) * (X.shape[1] / (X.shape[0] - X.shape[1] - 1))
        p_value = f_regression(X, y)[1]
        print(mse, r_squared, p_value)

    def pict(self):

        plt.scatter(self.X, self.y, color='black')
        plt.plot(self.X, self.lm.predict(self.X), color='blue')
        plt.savefig('totaldollar')



