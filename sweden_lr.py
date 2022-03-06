import pandas as pd
import numpy as np
import cmath
import matplotlib.pyplot as plt
def lin_regress(x, y, claims):
    # Finding x_mean and y_mean
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    #print("Xmean is ",x_mean)
    #print("Ymean is ",y_mean)
    # Finding xi-x_mean and yi-y_mean
    xi_xmean = []
    yi_ymean = []
    for i in range(len(x)):
        xi_xmean.append(round(x[i]-x_mean, 3))
    for i in range(len(y)):
        yi_ymean.append(round(y[i]-y_mean, 3))
    xi_xmean = np.array(xi_xmean)
    yi_ymean = np.array(yi_ymean)
    b1_numer = sum(xi_xmean*yi_ymean)
    b1_denome = sum(pow((xi_xmean), 2))
    b1 = b1_numer/b1_denome
    bo = y_mean - (b1 * x_mean)
    print("beta 1 is:",b1)
    print("beta 0 is:",bo)
    y_predic = bo + (b1 * claims)
    y_square = yi_ymean * yi_ymean
    y_square =y_square
    # Finding sum of yi-ymean square
    y_square_sum = 0
    for i in range(len(y_square)):
        y_square_sum += y_square[i]
    y_square_sum = round(y_square_sum,3)

# jam_x and jam_y are the inside data of sigma_x and sigma_y, i have just given them a name

    jam_x = b1_denome/len(x)
    jam_x = round(jam_x)
    sigma_x = cmath.sqrt(jam_x)
    sigma_x = sigma_x
    jam_y = y_square_sum/len(y)
    jam_y = round(jam_y,3)
    sigma_y = cmath.sqrt(jam_y)
    sigma_y = sigma_y
    R2_denome = sigma_x * sigma_y
    R2_denome = R2_denome
    R2_numer = b1_numer/len(x)
    R2_numer = round(R2_numer,3)
    R2_1 = R2_numer/R2_denome
    R2_1 = np.round(R2_1,3)
    R2 = R2_1 * R2_1
    R2 = np.round(R2,3)

    return y_predic,print("Coefficient of distribution is::",R2)


df = pd.read_csv('ins.csv')
x=df['x']
y=df['y']

x=np.array(x)
y=np.array(y)
# Finding sum of all elements of x
plt.plot(x, y, 'o')
m,b = np.polyfit(x,y,1)
plt.plot(x, m*x + b)
plt.title('Comparing Bestfit Line for Auto insurance')    
plt.show()
ch=0
while ch!=2:
    print("\n1.Give input")
    print("\n2.Exit")
    ch = int(input("Enter your choice:::"))
    if ch==1:
        claims = int(input("Enter no.of claims::"))
        print("Predicton is::",lin_regress(x,y,claims))
    elif ch==2:
        exit() 


