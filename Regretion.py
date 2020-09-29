import pandas as pd
import math
from decimal import Decimal
import matplotlib.pyplot as plt


def data_range(x):
    return max(x) - min(x)


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


def get_y_pred(x, slope, intercept):
    return (x * slope + intercept)


def get_residuals(list1, list2):
    residuals = []
    i = 0
    while i < len(list1):
        residuals.append(round((list1[i] - list2[i]), 2))
        i+= 1
    return residuals


def get_ssr(list1, list2):
    res = get_residuals(list1, list2)
    ssr = 0
    i = 0
    while i < len(res):
        ssr = ssr + ((res[i])**2)
        i+= 1
    return ssr


def get_sum_residuals(list1, list2):
    res = get_residuals(list1, list2)
    sum_res = 0
    i = 0
    while i < len(res):
        sum_res += res[i]
        i+= 1
    return round(sum_res, 1)


def do_all_regression_stuff(x, y):
    mean_exploratory = mean(x)
    mean_response = mean(y)
    
    cov_xy = round(covariance(x, y), 4)
    var_x = round(variance(x), 4)
    
    beta_1_hat = round((cov_xy/var_x), 6) # Slope of the best fit straight line
    beta_0_hat = round((mean_response - beta_1_hat * mean_exploratory), 6) # Intercept of the best fit straight line
    response_value_list = []
    
    for x_i in x:
        response_value_list.append(round(get_y_pred(x_i, beta_1_hat, beta_0_hat), 2))
    
    errors = get_residuals(y,response_value_list)
    
    response_sum_residuals = get_sum_residuals (y, response_value_list)
    response_value_ssr = round(get_ssr(y, response_value_list), 4)
    
    r_xy = correlation(x, y)
    r_sq = r_xy**2 * 100
    
    
    newdf = pd.DataFrame({
        'X Mean':[mean_exploratory],
        'Y Mean':[mean_response],
        'Beta-0(Slope)': [beta_1_hat],
        'Beta-1(Intercept)': [beta_0_hat],
        'SumOfResiduals':[response_sum_residuals],
        'SumSquareResiduals':[response_value_ssr],
        'R-XY(Correlation)':[round(r_xy, 2)],
        'R-Square-XY':[round(r_sq, 2)],
        'Goodness of fit(%)':[round(r_sq,2)]
    })
    
    resultdict = {
        'X Mean' : mean_exploratory,
        'Y Mean' : mean_response,
        'Beta_1_hat': beta_1_hat,
        'Beta_0_hat': beta_0_hat,
        'SumOfResiduals' : response_sum_residuals,
        'SumSquareResiduals' : response_value_ssr,
        'R-XY(Correlation)' : round(r_xy, 2),
        'R-Square-XY' : round(r_sq, 2),
        'Goodness of fit(%)' : round(r_sq,2),
        'errors' : errors,
        'response_value_list' : response_value_list,
        'cov_xy' : cov_xy,
        'var_x' : var_x,
        'r_xy' : r_xy,
        'r_sq' : r_sq
        
    }
    
    
    newdf = newdf[['X Mean', 'Y Mean', 'Beta-0(Slope)', 'Beta-1(Intercept)', 'SumOfResiduals', 'SumSquareResiduals', 'R-XY(Correlation)', 'R-Square-XY', 'Goodness of fit(%)']]
    
    return resultdict, newdf