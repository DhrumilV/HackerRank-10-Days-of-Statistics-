# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

n = 100
mean = 500
sd = 80
new_sd = sd/sqrt(n)
ci = 0.95
z_score = 1.96

A = mean - (z_score * new_sd)
B = mean + (z_score * new_sd)

print(round(A,2))
print(round(B,2))
