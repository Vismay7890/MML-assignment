import numpy as np
def addition():
    rows = int(input("Enter the Number of rows : " ))
    column = int(input("Enter the Number of Columns: "))

    print("Enter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]


    print("Enter the elements of Second Matrix:")
    matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]

    
    result=[[0 for i in range(column)] for i in range(rows)]

    for i in range(rows):
        for j in range(column):
            result[i][j] = matrix_a[i][j]+matrix_b[i][j]

    print("The Sum of Above two Matrices is : ")
    for r in result:
        print(r)

def multiplication():
    rows = int(input("Enter the Number of rows : " ))
    column = int(input("Enter the Number of Columns: "))

    print("Enter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]


    print("Enter the elements of Second Matrix:")
    matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
    result=[[0 for i in range(column)] for i in range(rows)]

    for i in range(len(matrix_a)):
 
    # iterating by column by B
        for j in range(len(matrix_b[0])):
 
        # iterating by rows of B
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
 
    for r in result:
        print(r)

def inverse():
    rows = int(input("Enter the Number of rows : " ))
    column = int(input("Enter the Number of Columns: "))

    print("Enter the elements of Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
    inverse = [[0 for i in range(column)] for i in range(rows)]
    if rows==2 and column==2 :
        inverse[0][0]= (1/(matrix_a[0][0]*matrix_a[1][1]-matrix_a[0][1]*matrix_a[1][0])) *(matrix_a[1][1])  
        inverse[0][1]= (1/(matrix_a[0][0]*matrix_a[1][1]-matrix_a[0][1]*matrix_a[1][0])) *(-matrix_a[0][1]) 
        inverse[1][0]= (1/(matrix_a[0][0]*matrix_a[1][1]-matrix_a[0][1]*matrix_a[1][0])) *(-matrix_a[1][0])  
        inverse[1][1]= (1/(matrix_a[0][0]*matrix_a[1][1]-matrix_a[0][1]*matrix_a[1][0])) *(matrix_a[0][0]) 
        print("\n-------------------------------------------------------------")        
        print(inverse)
        print("\n-------------------------------------------------------------") 
    elif rows==3 and column==3:
        det_matrix = matrix_a[0][0]*(matrix_a[1][1]*matrix_a[2][2]-matrix_a[1][2]*matrix_a[2][1]) - matrix_a[0][1]*(matrix_a[1][0]*matrix_a[2][2]-matrix_a[1][2]*matrix_a[2][0]) + matrix_a[0][2]*(matrix_a[1][0]*matrix_a[2][1]-matrix_a[1][1]*matrix_a[2][0])
        inverse[0][0] = (matrix_a[1][1]*matrix_a[2][2]-matrix_a[1][2]*matrix_a[2][1])/det_matrix
        inverse[1][0] = -(matrix_a[1][0]*matrix_a[2][2]-matrix_a[1][2]*matrix_a[2][0])/det_matrix
        inverse[2][0] = (matrix_a[1][0]*matrix_a[2][1]-matrix_a[1][1]*matrix_a[2][0])/det_matrix
        inverse[0][1] = -(matrix_a[0][1]*matrix_a[2][2]-matrix_a[0][2]*matrix_a[2][1])/det_matrix
        inverse[1][1] = (matrix_a[0][0]*matrix_a[2][2]-matrix_a[0][2]*matrix_a[2][0])/det_matrix
        inverse[2][1] = -(matrix_a[0][0]*matrix_a[2][1]-matrix_a[0][1]*matrix_a[2][0])/det_matrix
        inverse[0][2] = (matrix_a[0][1]*matrix_a[1][2]-matrix_a[0][2]*matrix_a[1][1])/det_matrix
        inverse[1][2] = -(matrix_a[0][0]*matrix_a[1][2]-matrix_a[0][2]*matrix_a[1][0])/det_matrix
        inverse[2][2] = (matrix_a[0][0]*matrix_a[1][1]-matrix_a[0][1]*matrix_a[1][0])/det_matrix
        print("\n-------------------------------------------------------------")        
       
        print(inverse)

ch = 0 
while ch != 4:
    print("-----------------------------\n")
    print("\n 1. Addition\n")
    print("\n 2. Multiplication\n")
    print("\n 3. Inverse\n")
    print("\n 4. Exit\n")
    ch = int(input("Enter your Choice:::"))
    if ch==1:
        addition()
    elif ch==2:
        multiplication()
    elif ch==3:
        inverse()
    elif ch==4:
        exit
    else :
        exit
