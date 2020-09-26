# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
x = [int(i) for i in input().strip().split(' ')]

mean = sum(x)/n

numerator = 0
for i in range(n):
    numerator += (x[i]-mean)**2

var = numerator/n
standar_deviation = (var)**(1/2)

print(round(standar_deviation,1))
