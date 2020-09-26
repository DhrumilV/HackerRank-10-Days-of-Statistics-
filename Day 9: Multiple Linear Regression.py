# Enter your code here. Read input from STDIN. Print output to STDOUT

# First Try (only first test case successful) ; Final submission (All test cases successful) below 

# from sklearn import linear_model
# import numpy as np

# input_1 = input().strip().split()
# m = int(input_1[0])
# n = int(input_1[1])

 
# b1_coeff, b2_coeff, c_coeff = [], [], []
# for _ in range(n):
#     input_2 = input().strip().split()
#     b1_coeff.append(float(input_2[0]))
#     b2_coeff.append(float(input_2[1]))
#     c_coeff.append(float(input_2[2]))
    
# q = int(input())

# new_b1_coeff, new_b2_coeff = [], []
# for _ in range(q):
#     input_4 = input().strip().split()
#     new_b1_coeff.append(float(input_4[0]))
#     new_b2_coeff.append(float(input_4[1]))

# x = np.zeros((n,m))
# y = np.zeros((n))
# for i in range(n):
#     y[i] = c_coeff[i]
#     for j in range(m):
#         if j == 0:
#             x[i][j] = b1_coeff[i]
#         else:
#             x[i][j] = b2_coeff[i]    

# lm = linear_model.LinearRegression()
# lm.fit(x,y)
# a = lm.intercept_
# b = lm.coef_

# new_c_coeff = []
# for i in range(q):
#     new_c_coeff.append( a + (new_b1_coeff[i] * b[0]) + (new_b2_coeff[i] * b[1]) )
#     print(new_c_coeff[i])

#Final Submission

from sklearn import linear_model

m, n = [int(e) for e in input().split(" ")]
y = []
x = []
for i in range(n):
    x.append([float(e) for e in input().split(" ")])
    y.append(x[i][m])
    x[i].pop()
    
q = int(input())


lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

for i in range(q):
    res = a
    z = ([float(e) for e in input().split(" ")])
    for i in range(m):
        res += b[i] * z[i]
    print(res)





