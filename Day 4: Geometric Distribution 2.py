# Enter your code here. Read input from STDIN. Print output to STDOUT
p = 1/3.0
q = 1-p
N = 5

sum = p * (1 + q**1 + q**2 + q**3 + q**4)

print(round(sum,3))
