import numpy as np
# Describing weights

w1 = [0.15,0.20]
w2 = [0.25,0.30]
w3 = [0.40,0.45]
w4 = [0.50,0.55]
w1 = np.array(w1)
w2 = np.array(w2)
w3 = np.array(w3)
w4 = np.array(w4)
x = [0.05,0.10]
b = [0.35,0.60]
x = np.array(x)
b = np.array(b)
target = [0.01,0.99]

# defining the Sigmoid Function
def sigmoid (x):
    return 1/(1 + np.exp(-x))

# derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

epoch = int(input("Enter the no. of iterations::"))
for i in range(epoch):
    # Forward propagation
    neth1 = np.dot(w1,x)+b[0]
    neth2 = np.dot(w2,x)+b[0]
    outh1 = sigmoid(neth1)
    outh2 = sigmoid(neth2)
    out = [outh1,outh2]
    out = np.array(out)   
    nety1 = np.dot(w3,out)+b[1]
    nety2 = np.dot(w4,out)+b[1]
    outy1 = sigmoid(nety1)
    outy2 = sigmoid(nety2)
    
    # Backpropagation
    Ey1 = 0.5*pow(target[0]-outy1,2)
    Ey2 = 0.5*pow(target[1]-outy2,2)
    E_total = np.add(Ey1,Ey2)
    print("error epoch :",E_total)
    w3_delta_1 = w3[1] - ((-1)*(target[1]-outy1) * derivatives_sigmoid(outy1) * out[1])
    w3_delta_0 = w3[0] - ((-1)*(target[0]-outy1) * derivatives_sigmoid(outy1) * out[0])
    w4_delta_0 = w4[0] - ((-1)*(target[0]-outy2) * derivatives_sigmoid(outy2) * out[0])
    w4_delta_1 = w3[1] - ((-1)*(target[0]-outy1) * derivatives_sigmoid(outy1) * out[1])
    temp1 = (-1)*(target[0]-outy1) * derivatives_sigmoid(outy1) * w3[0]
    temp2 = (-1)*(target[1]-outy2) * derivatives_sigmoid(outy2) * w4[0]
    temp3 = temp1-temp2
    w1_delta_0 = w1[0]- (derivatives_sigmoid(outh1) * x[0] * temp3)
    w1_delta_1 = w1[1]- (derivatives_sigmoid(outh1) * x[1] * temp3)
    temp4 = (-1)*(target[0]-outy1) * derivatives_sigmoid(outy1) * w3[1]
    temp5 = (-1)*(target[1]-outy2) * derivatives_sigmoid(outy2) * w4[1]
    temp6 = temp1-temp2
    w2_delta_0 = w2[0] - (derivatives_sigmoid(outh2) * x[0] * temp6)
    w2_delta_1 = w2[1] - (derivatives_sigmoid(outh2) * x[1] * temp6)
    
    w1[0] = w1[0] - (0.5) * (w1_delta_0) 
    w1[1] = w1[1] - (0.5) * (w1_delta_1) 
    w2[0] = w2[0] - (0.5) * (w2_delta_0) 
    w2[1] = w2[1] - (0.5) * (w2_delta_1) 
    w3[0] = w3[0] - (0.5) * (w3_delta_0) 
    w3[1] = w3[1] - (0.5) * (w3_delta_1) 
    w4[0] = w4[0] - (0.5) * (w4_delta_0) 
    w4[1] = w4[1] - (0.5) * (w4_delta_1) 

print("------Updated weights are------")
print("W1",w1[0])
print("W2",w1[1])
print("W3",w2[0])
print("W4",w2[1])
print("W5",w3[0])
print("W6",w3[1])
print("W7",w4[0])
print("W8",w4[1])