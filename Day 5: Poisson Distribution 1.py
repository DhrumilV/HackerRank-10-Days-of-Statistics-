# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import exp, factorial

l = 2.5
k = 5

p = ((l**k) * exp(-l)) / factorial(k)

print('%.3f' %p)
