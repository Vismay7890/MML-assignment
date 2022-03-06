# 100 Meter women olympic race data
# importing numpy
import numpy as np
import cmath
# Given data 'x' as years and 'y' as time taken
x = [1896, 1900, 1904, 1906, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 1948, 1952, 1956,
     1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
y = [12.00, 11.00, 11.00, 11.20, 10.18, 10.80, 10.80, 10.60, 10.80, 10.30, 10.30, 10.30, 10.40, 10.50,
     10.20, 10.00, 9.95, 10.14, 10.06, 10.25, 9.99, 9.92, 9.96, 9.84, 9.87, 9.85, 9.69, 9.63, 9.81]
print(len(x))
print(len(y))
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
x_mean = round(x_mean, 3)
print("Mean of X is :", x_mean)
# Finding mean of y
y_mean = sum_y/len(y)
y_mean = round(y_mean, 3)

print("Mean of Y is :", y_mean)
# Findind Xi-x̅
xi_x_mean = []
for i in range(len(x)):
    xi_x_mean.append(round(x[i]-x_mean, 3))
xi_x_mean

# converting it into numpy array
xi_x_mean = np.array(xi_x_mean)
# Findind Yi-ȳ
yi_y_mean = []
for i in range(len(y)):
    yi_y_mean.append(round(y[i]-y_mean, 3))
yi_y_mean

# Converting it into numpy array
yi_y_mean = np.array(yi_y_mean)
# Findind numerator of B1
numer = (xi_x_mean * yi_y_mean)
numer
# Finding denominator of B1
denome = (xi_x_mean * xi_x_mean)
denome
# Finding sum of numerator array
numer_sum = 0
for i in range(len(numer)):
    numer_sum += numer[i]
numer_sum = abs(numer_sum)
numer_sum = round(numer_sum, 3)
print("Upper part of B1 is :", numer_sum)
# Finding sum of denominator array
denome_sum = 0
for i in range(len(denome)):
    denome_sum += denome[i]
denome_sum = round(denome_sum, 3)
print("Lower part of B1 is :", denome_sum)
# Finding B1
B1 = numer_sum/denome_sum
B1 = round(B1, 3)
print("B1 is :", B1)
# Finding Bo
B0 = (y_mean - (-1)*(B1 * x_mean))
B0 = round(B0, 3)
print("B0 is :", B0)
predic_y = B0 + (-1)*(B1 * 2020)
predic_y = round(predic_y, 3)
print("Prediction is :", predic_y)
y_square = yi_y_mean * yi_y_mean
y_square = y_square
# Finding sum of yi-ymean square
y_square_sum = 0
for i in range(len(y_square)):
    y_square_sum += y_square[i]
y_square_sum = round(y_square_sum, 3)

jam_x = denome_sum/len(x)
jam_x = round(jam_x)
sigma_x = cmath.sqrt(jam_x)
sigma_x = sigma_x
jam_y = y_square_sum/len(y)
jam_y = round(jam_y, 3)
sigma_y = cmath.sqrt(jam_y)
sigma_y = sigma_y
R2_denome = sigma_x * sigma_y
R2_denome = R2_denome
R2_numer = numer_sum/len(x)
R2_numer = round(R2_numer, 3)
R2_1 = R2_numer/R2_denome
R2_1 = np.round(R2_1, 3)
R2 = R2_1 * R2_1
R2 = np.round(R2, 3)

print(R2)
