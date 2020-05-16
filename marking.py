import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics

def marker(arr): 
	dataset=pd.read_csv("C:\\Users\\ahuja\\Dataset##.csv")
	X=dataset.iloc[:,:-1].values
	Y=dataset.iloc[:,-1].values
	from sklearn.linear_model import LinearRegression
	regressor=LinearRegression()
	regressor.fit(X,Y)
	X_test=[arr]
	Y_pred=regressor.predict(X_test)
	if(Y_pred<0):
	print("'0' marks should be awarded to student")
	else:
	print(Y_pred[0]*marks,"marks should be awarded to student")