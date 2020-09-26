from math import factorial

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += (factorial(n)/(factorial(i)*factorial(n-i)))*(p**i)*((1-p)**(n-i))
      
print("%.3f" %b)
