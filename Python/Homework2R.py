from __future__ import division
import scipy.stats as stats
from scipy.stats import norm
from decimal import Decimal
import math
from math import sqrt
import csv
import pandas as pd
import numpy as np
import mysql.connector


def LeftPValue(zScore):
    return(stats.norm.cdf(zScore))

# if new number is bigger than old number then its left tail other way around is right
# if left tail we want to be smaller than .05 or crit value


def RightPValue(zScore):
    return(1 - stats.norm.cdf(zScore))

def zScore(oldMean, newMean, stdDev):
    return ((oldMean- newMean)/stdDev)


def ConfidenceLevel(sigLevel):
    return abs(sigLevel - 1)


def SignificanceLevel(confLevel):
    return (1 - confLevel)


def LeftPValueAndZScore(oldMean,newMean,stdDev, sampleSize, critValue):
    
    zscore = zScore(oldMean, newMean, stdDev)
    return (LeftPValue(zscore), zscore)


def RightPValueAndZScore(oldMean,newMean,stdDev, sampleSize, critValue):
    
    zscore = zScore(oldMean, newMean, stdDev)
    results = [zscore, RightPValue(zscore)]
    return (results)






def init():
    oldMean = int(input("Please input the mean of the sample: "))#Mean
    newMean = int(input("Please input the new mean of test sample: "))#Mean
    stdDev = int(input("Please input the Standard Deviation of the sample: ")) #mui
    critValue = float(input("Please input the level of significance: "))
    sampleSize = int(input("Please input sample size: "))
    
    
    RightPValueAndZScoreResult = RightPValueAndZScore(newMean, oldMean, stdDev, sampleSize, critValue)
    LeftPValueAndZScoreResult = LeftPValueAndZScore(newMean, oldMean, stdDev, sampleSize, critValue)
    
    
    
    print("\nLeft Tail:\nP value: ", LeftPValueAndZScoreResult[0], "\nZ score: ", LeftPValueAndZScoreResult[1])
    print("\nRight Tail:\nP value: ", RightPValueAndZScoreResult[0], "\nZ score: ", RightPValueAndZScoreResult[1], '\n')


if __name__ == '__main__':
    
    init()
    
    
    my_connection = mysql.connector.connect(user='root', password='root',
                                        host= 'localhost',
                                        database='test',
                                        auth_plugin='caching_sha2_password') 
    mycursor = my_connection.cursor()
    
    with open('./CSV/popNames.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        # Add the header/column names
        header = ['id', 'Name', 'Year', 'Gender', 'Count']
        writer.writerow(header)
        mycursor.execute('Select * from PoplNames')
        data = mycursor.fetchall()
        # Iterate over `data`  and  write to the csv file
        for row in data:
            #print(row)
            writer.writerow(row)
        f_handle.close()
    
    NewCases = pd.read_csv("./CSV/sevenday_rolling_average_of_new_cases.csv").head(100) # converts .csv to dataframe
    NewDeaths = pd.read_csv("./CSV/sevenday_rolling_average_of_new_deaths.csv").head(100) # converts .csv to dataframe
    
    
    
    
    
    
    