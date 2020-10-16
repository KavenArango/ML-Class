from __future__ import division
import matplotlib.pyplot as plt 
import scipy.stats as stats
from scipy.stats import norm
from decimal import Decimal
import pandas as pd
import math
from math import sqrt



def get_levelOfSignificance(confidenceLevel):
    return (1 - confidenceLevel)

def get_levelOfConfidence(significanceLevel):
    return abs(significanceLevel - 1)

def getZ_score(X_bar, X_bar2, std_dev):
    return ((X_bar-X_bar2)/std_dev)

def getLeftP_value(z_score):
    return (stats.norm.cdf(z_score))

def getRightP_value(z_score):
    return (1- stats.norm.cdf(z_score))

def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)

def mean(x):
    return round((sum(x) / len(x)), 2)

def diff_from_mean(x):
    x_bar = mean(x)
    return [round((x_i - x_bar), 2) for x_i in x]

def sum_of_squares(x):
    return(sum(x_i**2 for x_i in x))

def variance(x):
    l = len(x)
    deviations = diff_from_mean(x)
    return (sum_of_squares(deviations)/(l - 1))

def testStatistic(X_bar, X_bar2, std_dev, sampleSize):
    return((X_bar2 - X_bar) / ((std_dev) / (math.sqrt(sampleSize))))

def getLeftPValueAndZScore(X_bar,X_bar2,std_dev, sampleSize, critValue):
    
    zscore = getZ_score(X_bar, X_bar2, std_dev)
    return (getLeftP_value(zscore), zscore)


def getRightPValueAndZScore(X_bar,X_bar2,std_dev, sampleSize, critValue):
    
    zscore = getZ_score(X_bar, X_bar2, std_dev)
    results = [zscore, getRightP_value(zscore), zscore]
    return (results)


#my_connection = mysql.connector.connect(user='root', password='root', host= 'localhost',database='mytestdb',auth_plugin='caching_sha2_password')  


def init():
    
    x_bar = int(input("Please input the mean of the sample: "))#Mean
    x_bar2 = int(input("Please input the new mean of test sample: "))#Mean
    std_dev = int(input("Please input the Standard Deviation of the sample: ")) #mui
    critValue = float(input("Please input the level of significance: "))
    sampleSize = int(input("Please input sample size: "))
    
    
    RightPValueAndZScoreResult = getRightPValueAndZScore(x_bar2, x_bar, std_dev, sampleSize, critValue)
    LeftPValueAndZScoreResult = getLeftPValueAndZScore(x_bar2, x_bar, std_dev, sampleSize, critValue)
    
    testScore = testStatistic(x_bar,x_bar2,std_dev,sampleSize)
    testscore = stats.norm.ppf(testScore)
    
    print("test score: ", testscore)
    
    print("\nLeft Tail:\nP value: ", LeftPValueAndZScoreResult[0], "\nZ score: ", LeftPValueAndZScoreResult[1])
    print("\nRight Tail:\nP value: ", RightPValueAndZScoreResult[0], "\nZ score: ", RightPValueAndZScoreResult[1], '\n')


if __name__ == '__main__':
    
    
    z_score_1 = stats.norm.cdf(0.2) # for C= 0.9 i.e. p = 0.1
    print(z_score_1)
    init()
    