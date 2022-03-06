import numpy as np
ch=0
def addition():
   x=int(input("\nENTER ROWS FOR MATRIX :>"))
   y=int(input("\nENTER COLOUMN FOR MATRIX :>"))
   arr= np.zeros((x,y),dtype=int)
   arr2= np.zeros((x,y),dtype=int)
   arr3 = np.zeros((x,y),dtype=int)
   for i in range(len(arr)):
       for j in range(len(arr[i])):
           print("\nFOR MATRIX 1 ENTER ELEMENT ROW",i,"COLOUMN",j)
           arr[i][j]=int(input())
   for i in range(len(arr2)):
       for j in range(len(arr2[i])):
           print("\nFOR MATRIX 2 ENTER ELEMENT ROW",i,"COLOUMN",j)
           arr2[i][j]=int(input())
   arr3=arr2+arr
   print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")        
   print("\nADDITION OF TWO MATRIX IS \n",arr3)
   print("\nVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
   
def multiplication():
    x1=int(input("\nENTER ROWS FOR MATRIX 1:>"))
    y1=int(input("\nENTER COLOUMN FOR MATRIX 1:>"))
    arr= np.zeros((x1,y1),dtype=int)
    x2=int(input("\nENTER ROWS FOR MATRIX 2:>"))
    y2=int(input("\nENTER COLOUMN FOR MATRIX 2:>"))
    arr2= np.zeros((x2,y2),dtype=int)
    arr3= np.zeros((x1,y2),dtype=int)
    for i in range(len(arr)):
       for j in range(len(arr[i])):
           print("\nFOR MATRIX 1 ENTER ELEMENT ROW",i,"COLOUMN",j)
           arr[i][j]=int(input())
    for i in range(len(arr2)):
       for j in range(len(arr2[i])):
           print("\nFOR MATRIX 2 ENTER ELEMENT ROW",i,"COLOUMN",j)
           arr2[i][j]=int(input())
    for i in range(len(arr)):  
       for j in range(len(arr2[0])):   
           for k in range(len(arr[0])):    
             arr3[i][j]= arr3[i][j] + arr[i][k]*arr2[k][j]
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")        
    print(arr3)
    print("\nVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")         
    
def inverse():
    x=int(input("\nENTER ROWS FOR MATRIX :>"))
    y=int(input("\nENTER COLOUMN FOR MATRIX :>"))
    arr= np.zeros((x,y),dtype=int)
    inverse=np.zeros((x,y),dtype=float)
    for i in range(len(arr)):
       for j in range(len(arr[i])):
           print("\nFOR MATRIX 1 ENTER ELEMENT ROW",i,"COLOUMN",j)
           arr[i][j]=int(input())
    if x==2 and y==2 :
        inverse[0][0]= (1/(arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0])) *(arr[1][1])  
        inverse[0][1]= (1/(arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0])) *(-arr[0][1]) 
        inverse[1][0]= (1/(arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0])) *(-arr[1][0])  
        inverse[1][1]= (1/(arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0])) *(arr[0][0]) 
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")        
        print("INVERSE OF ")
        print(arr)
        print("\nis")
        print(inverse)
        print("\nVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV") 
    elif x==3 and y==3:
        det_matrix = arr[0][0]*(arr[1][1]*arr[2][2]-arr[1][2]*arr[2][1]) - arr[0][1]*(arr[1][0]*arr[2][2]-arr[1][2]*arr[2][0]) + arr[0][2]*(arr[1][0]*arr[2][1]-arr[1][1]*arr[2][0])
        inverse[0][0] = (arr[1][1]*arr[2][2]-arr[1][2]*arr[2][1])/det_matrix
        inverse[1][0] = -(arr[1][0]*arr[2][2]-arr[1][2]*arr[2][0])/det_matrix
        inverse[2][0] = (arr[1][0]*arr[2][1]-arr[1][1]*arr[2][0])/det_matrix
        inverse[0][1] = -(arr[0][1]*arr[2][2]-arr[0][2]*arr[2][1])/det_matrix
        inverse[1][1] = (arr[0][0]*arr[2][2]-arr[0][2]*arr[2][0])/det_matrix
        inverse[2][1] = -(arr[0][0]*arr[2][1]-arr[0][1]*arr[2][0])/det_matrix
        inverse[0][2] = (arr[0][1]*arr[1][2]-arr[0][2]*arr[1][1])/det_matrix
        inverse[1][2] = -(arr[0][0]*arr[1][2]-arr[0][2]*arr[1][0])/det_matrix
        inverse[2][2] = (arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0])/det_matrix
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")        
        print("INVERSE OF ")
        print(arr)
        print("\nis")
        print(inverse)
        print("\nVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
    else :
        print("\n************************")
        print("\nWE FIND INVERSE ONLY FOR 2X2 AND 3X3")    
        print("\n************************")

while ch != 4:
    print("\n************************")
    print("\n1.ADDITION\n")
    print("2.MULTIPLICATION\n")
    print("3.INVERSE\n")
    print("4.exit\n")
    print("\n************************")
    ch = int(input("ENTER YOUR CHOISE :>  "))
    if ch == 1:
       addition()
    elif ch == 2:
        multiplication()   
    elif ch == 3:
        inverse()
    elif ch==4:
        exit
    else :
        exit