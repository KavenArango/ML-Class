import math
from math import sqrt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

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

def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))




def covariance(x, y):
    n = len(x) # length of both x and y are required to be the same
    return (dot(diff_from_mean(x), diff_from_mean(y)))/ (n-1)



def correlation(x, y):
    sdev_x = standard_deviation(x)
    sdev_y = standard_deviation(y)
    if sdev_x > 0 and sdev_y > 0:
        return covariance(x,y)/(sdev_x * sdev_y)
    else:
        return 0
    

print('Correlation between x and y = ', correlation(x, y))
print('===================================================')