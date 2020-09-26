# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, erf

x = 250
n = 100
mean = 2.4
sd = 2.0

new_mean = n * mean
new_sd = sqrt(n) * sd

p = 0.5 * ( 1 +( erf((x - new_mean) / (new_sd * sqrt(2)))))

print(round(p,4))
