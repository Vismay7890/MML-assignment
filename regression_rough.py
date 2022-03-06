# 100 Meter women olympic race data
# importing numpy
import numpy as np
import cmath
# Given data 'x' as years and 'y' as time taken
x = [1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
     1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
y = [12.20, 11.90, 11.15, 11.90, 11.50, 11.50, 11.00, 11.40, 11.00, 11.07,
     11.08, 11.06, 10.97, 10.54, 10.82, 10.94, 11.12, 10.93, 10.78, 10.75, 10.71]
# Finding sum of all elements of x
sum_x = 0
for i in range(len(x)):
    sum_x += x[i]
sum_x
print("Sum of all elements of x is :,", sum_x)
# Finding sum of all elemnts of y
sum_y = 0
for i in range(len(y)):
    sum_y += y[i]
sum_y
print("Sum of all elements of y is :,", sum_y)
# Finding mean of x
x_mean = sum_x/len(x)
x_mean
print("Mean of X is :", x_mean)
# Finding mean of y
y_mean = sum_y/len(y)
y_mean
print("Mean of Y is :", y_mean)
# Findind Xi-x̅
xi_x_mean = []
for i in range(len(x)):
    xi_x_mean.append(x[i]-x_mean)
xi_x_mean

# converting it into numpy array
xi_x_mean = np.array(xi_x_mean)
# Findind Yi-ȳ
yi_y_mean = []
for i in range(len(y)):
    yi_y_mean.append(y[i]-y_mean)
yi_y_mean

# Converting it into numpy array
yi_y_mean = np.array(yi_y_mean)
# Findind numerator of B1
numer = xi_x_mean * yi_y_mean
numer
# Finding denominator of B1
denome = xi_x_mean * xi_x_mean
denome
# Finding sum of numerator array
numer_sum = 0
for i in range(len(numer)):
    numer_sum += numer[i]
numer_sum = abs(numer_sum)
print("Upper part of B1 is :",numer_sum)
# Finding sum of denominator array
denome_sum = 0
for i in range(len(denome)):
    denome_sum += denome[i]
denome_sum
print("Lower part of B1 is :",denome_sum)
# Finding B1
B1 = numer_sum/denome_sum
B1
print("B1 is :",B1)
# Finding Bo
B0 = (y_mean - (-1)*(B1 * x_mean))
print("B0 is :",B0)
predic_y = B0 + (-1)*(B1 * 2020)
print("Prediction is :",predic_y)
y_square = yi_y_mean * yi_y_mean
# Finding sum of yi-ymean square
y_square_sum = 0
for i in range(len(y_square)):
    y_square_sum += y_square[i]
y_square_sum

jam_x = denome_sum/len(x)
sigma_x = cmath.sqrt(jam_x)
jam_y = y_square_sum/len(y)
sigma_y = cmath.sqrt(jam_y)
R2_denome = sigma_x * sigma_y
R2_numer = numer_sum/len(x)
R2_1 = R2_numer/R2_denome
R2 = R2_1 * R2_1
print("Sigma x is :",sigma_x)
print("Sigma y is :",sigma_y)
print(R2)
