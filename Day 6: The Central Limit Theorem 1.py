# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt, erf

x = 9800
n = 49
mean = 205
sd = 15

new_mean = n * mean
new_sd = sqrt(n) * sd

p = 0.5 * ( 1 +( erf((x - new_mean) / (new_sd * sqrt(2)))))

print(round(p,4))

