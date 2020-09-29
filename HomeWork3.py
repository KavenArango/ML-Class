from sklearn import linear_model
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import scipy.stats as stats
import Regretion as reg
import pandas as pd
import numpy as np
import math


def OpenCSV(CSV):
    return pd.read_csv('./CSV/'+CSV)


def drawGraph(x,y, response_value_list):
    
    plt.scatter(x, y, color='red', marker='o', s=30)
    plt.plot(x, response_value_list, color = "g")
    plt.xlabel('Exploratory (independent) variable values') 
    plt.ylabel('Response (dependent) variable values ')
    plt.show()


def PrintInfo(regdict):
    
    print('Mean of response (dependent) variable = ', regdict["Y Mean"])
    print('Mean of the exploratory (independent) variable = ', regdict["X Mean"])
    print('Covariance between exploratory and response variables = ', regdict["cov_xy"])
    print('Variance of exploratory (independent) variable = ', regdict["var_x"])
    print('beta_1_hat (slope of the best fit straight line) = ', regdict["Beta_1_hat"])
    print('beta_0_hat (intercept of the best fit straight line) = ', regdict["Beta_0_hat"])
    print('Response value list is ', regdict["response_value_list"])
    print('Errors or Residuals of Predicted Response value and Actual Exploratory value =', regdict["errors"])
    print('Sum of Residuals of Predicted and Actual Response Values = ', regdict["SumOfResiduals"])
    print('Sum Squared Residuals of Predicted and Actual Response Values = ', regdict["SumSquareResiduals"])
    print('Correlation between Exploratory and Response variables = ', regdict["r_xy"])
    print('R-square between Exploratory and Response variables = ', regdict["r_sq"])
    print('Goodness of fit :', regdict["r_sq"] , '% of the Response Variable values are explained by the line of best fit')


def OurReg(x,y):
    
    doallreg = reg.do_all_regression_stuff(x, y)
    
    reDF = doallreg[1]
    regdict = doallreg[0]
    
    PrintInfo(regdict)
    
    drawGraph(x, y, regdict["response_value_list"])


def SklearnLinear(x,y):
    
    regr = linear_model.LinearRegression()
    
    regr.fit(x, y)
    print('Intercept: ', regr.intercept_)
    print('Coefficients: ', regr.coef_)
    
    regr.score(x, y)
    
    
    return regr


def SklearnPredict(x,y, regr):
    print ('Predicted Stock Index Price: \n', regr.predict([[x ,y]]))


def SklearnLinearGraph(x,y,regr):
    py = regr.predict(x)
    
    plt.scatter(x, y, color='red', marker='o', s=30)
    plt.plot(x, py, color = "g")
    plt.xlabel('Exploratory (independent) variable values') 
    plt.ylabel('Response (dependent) variable values ')
    plt.show()


def SklearnLinearAndPoly(df):
    
    df1 = pd.DataFrame({
        'date' : df['date'],
        'new_cases': df['positiveIncrease'],
        'new_Hospitalization':df['hospitalizedIncrease'],
        'new_deaths' : df['deathIncrease'],
        'state': df['state']
    })
    
    
    lin = LinearRegression() 
    # Fitting Polynomial Regression to the dataset, degree = 4
    
    
    poly = PolynomialFeatures(degree = 4) 
    print('************* New Cases Vs. New Hospitalization *****************')
    
    
    list_x1 = df1[['new_cases']]
    list_y1 = df1['new_Hospitalization']
    
    lin.fit(list_x1, list_y1)    
    X_poly = poly.fit_transform(list_x1) 
    
    
    poly.fit(X_poly, list_y1) 
    lin2 = LinearRegression()
    lin2.fit(X_poly, list_y1)
    
    
    # Visualising the Linear Regression results 
    plt.scatter(list_x1, list_y1, color = 'red') 
    plt.plot(list_x1, lin.predict(list_x1), color = 'green') 
    plt.title('FL Linear Regression') 
    plt.xlabel('Number of new cases') 
    plt.ylabel('Number of new Hospitalization') 
    plt.show() 
    
    
    ## Visualising the Polynomial Regression results 
    plt.scatter(list_x1, list_y1, color = 'red') 
    plt.plot(list_x1, lin2.predict(poly.fit_transform(list_x1)), color = 'green') 
    plt.title('FL Polynomial Regression') 
    plt.xlabel('Number of new cases') 
    plt.ylabel('Number of new Hospitalization') 
    plt.show()
    
    print('************* New Hospitalization Vs. New Death *****************')
    
    list_x1 = df1[['new_Hospitalization']]
    list_y1 = df1['new_deaths']
    
    lin.fit(list_x1, list_y1)    
    X_poly = poly.fit_transform(list_x1) 
    
    
    poly.fit(X_poly, list_y1) 
    lin2 = LinearRegression()
    lin2.fit(X_poly, list_y1)
    
    # Visualising the Linear Regression results 
    plt.scatter(list_x1, list_y1, color = 'red') 
    plt.plot(list_x1, lin.predict(list_x1), color = 'green') 
    plt.title('FL Linear Regression') 
    plt.xlabel('Number of new Hospitalization') 
    plt.ylabel('Number of new deaths') 
    plt.show() 
    
    
    ## Visualising the Polynomial Regression results 
    plt.scatter(list_x1, list_y1, color = 'red') 
    plt.plot(list_x1, lin2.predict(poly.fit_transform(list_x1)), color = 'green') 
    plt.title('FL Polynomial Regression') 
    plt.xlabel('Number of new Hospitalization') 
    plt.ylabel('Number of new deaths') 
    plt.show()




if __name__ == '__main__':
    
    df = OpenCSV('all-states-history.csv')
    SklearnLinearAndPoly(df.loc[df['state'] == 'FL'])
    
    #openedCSV = OpenCSV('InterestRate.csv')
    #OurReg(openedCSV['Interest_Rate'], openedCSV['Stock_Index_Price'])
    #print("\n\n")
    #OurReg(openedCSV['Unemployment_Rate'], openedCSV['Stock_Index_Price'])
    #print("\n\n")
    #
    #reg = SklearnLinear(openedCSV[['Interest_Rate', 'Unemployment_Rate']], openedCSV['Stock_Index_Price'])
    #SklearnPredict(2.75, 5.3, reg)
    #
    #print("\n\n")
    #openedCSV = OpenCSV('HousePrices.csv')
    #reg = SklearnLinear(openedCSV[['Square Footage']], openedCSV['House Price'])
    #SklearnLinearGraph(openedCSV[['Square Footage']], openedCSV[['House Price']], reg)
    #print("\n\n")
    #
    #openedCSV = OpenCSV('StudentGrades.csv')
    #reg = SklearnLinear(openedCSV[['Midterm']], openedCSV['Final Exam'])
    #SklearnLinearGraph(openedCSV[['Midterm']], openedCSV[['Final Exam']], reg)
    #