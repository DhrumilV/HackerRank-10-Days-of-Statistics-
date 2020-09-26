# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial

b1, b2, p, n = 0, 0, 0.12, 10
for i in range(0,3):
    b1 += (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))
for i in range(2,11):
    b2 += (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))
      
print("%.3f" %b1)
print("%.3f" %b2)
