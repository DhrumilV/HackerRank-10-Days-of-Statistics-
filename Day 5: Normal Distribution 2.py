# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf, sqrt 

mean = 70
sd = 10
x0 = 80
x1 = 60

p1 = 1 - ( 0.5 * ( 1 +( erf((x0 - mean) / (sd * sqrt(2))))))

p2 = 1-(0.5 * ( 1 +( erf((x1 - mean) / (sd * sqrt(2))))))
p3 = 0.5 * ( 1 +( erf((x1 - mean) / (sd * sqrt(2)))))

print(round(p1*100,2))
print(round(p2*100,2))
print(round(p3*100,2))
