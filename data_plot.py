import matplotlib.pyplot as plt
import numpy as np
Years = np.array([1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
     1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016])
Win_time = np.array([12.20, 11.90, 11.15, 11.90, 11.50, 11.50, 11.00, 11.40, 11.00, 11.07,
     11.08, 11.06, 10.97, 10.54, 10.82, 10.94, 11.12, 10.93, 10.78, 10.75, 10.71])
y_pred = 10.571
# plt.plot(Years,Win_time)
# plt.xlabel('Years')
# plt.ylabel('Win_time (sec)')
# plt.show()

# Finding Cosine similarity
# import cmath

# Years = [1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972,
#       1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
# Win_time = [12.20, 11.90, 11.15, 11.90, 11.50, 11.50, 11.00, 11.40, 11.00, 11.07,
#       11.08, 11.06, 10.97, 10.54, 10.82, 10.94, 11.12, 10.93, 10.78, 10.75, 10.71]


# res = np.dot(Years, Win_time) / np.linalg.norm(Years) / np.linalg.norm(Win_time)
# print (res)
# cosine_similarity_angle = cmath.acos(res) 
# print(cosine_similarity_angle)
# BEST FIT LINE

plt.plot(Years, Win_time, 'o')
m,b = np.polyfit(Years,Win_time,1)
plt.plot(Years, m*Years + b)
plt.title('Comparing Bestfit Line for Mens and Womens Olymics')
plt.show()



