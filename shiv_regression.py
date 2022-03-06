import pandas as pd
import numpy as np
import cmath


df = pd.read_csv('ins.csv')
x=df['x']
y=df['y']

x=np.array(x)
y=np.array(y)

sum_x = sum(x)
print("Sum of all elements of x is :,", sum_x)
# Finding sum of all elemnts of y
sum_y = sum(y)
print("Sum of all elements of y is :,", sum_y)
# Finding mean of x
x_mean = sum_x/len(x)
x_mean = round(x_mean,3)
print("Mean of X is :", x_mean)
# Finding mean of y
y_mean = sum_y/len(y)
y_mean = round(y_mean,3)

print("Mean of Y is :",y_mean)
# Findind Xi-x̅
xi_x_mean = []
for i in range(len(x)):
    xi_x_mean.append(round(x[i]-x_mean,3))

# converting it into numpy array
xi_x_mean = np.array(xi_x_mean)
# Findind Yi-ȳ
yi_y_mean = []
for i in range(len(y)):
    yi_y_mean.append(round(y[i]-y_mean,3))

# Converting it into numpy array
yi_y_mean = np.array(yi_y_mean)
# Findind numerator of B1
numer = (xi_x_mean * yi_y_mean)
# Finding denominator of B1
denome = (xi_x_mean * xi_x_mean)
# Finding sum of numerator array
numer_sum = 0
for i in range(len(numer)):
    numer_sum += numer[i]
numer_sum = abs(numer_sum)
numer_sum = round(numer_sum,3)
print("Upper part of B1 is :",numer_sum)
# Finding sum of denominator array
denome_sum = 0
for i in range(len(denome)):
    denome_sum += denome[i]
denome_sum = round(denome_sum,3)
print("Lower part of B1 is :",denome_sum)
# Finding B1
B1 = numer_sum/denome_sum
B1 = round(B1,3)
print("B1 is :",B1)
# Finding Bo
B0 = (y_mean - (B1 * x_mean))
B0 = round(B0,3)
print("B0 is :",B0)
predic_y = B0 + (B1 * 30)
predic_y = round(predic_y,3)
print("Prediction is :",predic_y)
y_square = yi_y_mean * yi_y_mean

# Finding sum of yi-ymean square
y_square_sum = 0
for i in range(len(y_square)):
    y_square_sum += y_square[i]
y_square_sum = round(y_square_sum,3)

# jam_x and jam_y are the inside data of sigma_x and sigma_y, i have just given them a name

jam_x = denome_sum/len(x)
jam_x = round(jam_x)
sigma_x = cmath.sqrt(jam_x)
jam_y = y_square_sum/len(y)
jam_y = round(jam_y,3)
sigma_y = cmath.sqrt(jam_y)
R2_denome = sigma_x * sigma_y
R2_denome = R2_denome
R2_numer = numer_sum/len(x)
R2_numer = round(R2_numer,3)
R2_1 = R2_numer/R2_denome
R2_1 = np.round(R2_1,3)
R2 = R2_1 * R2_1
R2 = np.round(R2,3)

print("R square is:",R2)

