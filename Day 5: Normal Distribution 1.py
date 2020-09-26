from math import erf, sqrt 

mean = 20
sd = 2
x0 = 19.5
x1 = 20
x2 = 22

p0 = 0.5 * ( 1 +( erf((x0 - mean) / (sd * sqrt(2)))))

p1 = 0.5 * ( 1 +( erf((x1 - mean) / (sd * sqrt(2)))))
p2 = 0.5 * ( 1 +( erf((x2 - mean) / (sd * sqrt(2)))))

print(round(p0,3))
print(round(p2-p1,3))
