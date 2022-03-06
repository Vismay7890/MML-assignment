import numpy as np
import math
from numpy import dot
from numpy.linalg import norm
c = int(input("Enter the size of vector 'A' :"))
d = int(input("Enter the size of vector 'B' :"))
A = []
for i in range(c):
	a = input("Enter element in A:")
	A.append(float(a))
print(A)
A = np.array(A)
B = []
for j in range(d):
	b = input("Enter element in B:")
	B.append(float(b))
print(B)
B = np.array(B)
res= dot(A,B)/(norm(A)*norm(B))

print("Cosine similarity between these two vectors is:",res)

