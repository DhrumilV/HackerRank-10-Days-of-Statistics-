# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

mean_x = sum(x)/n
mean_y = sum(y)/n

numerator_x = 0
numerator_y = 0 
for i in range(n):
    numerator_x += (x[i]-mean_x)**2
    numerator_y += (y[i]-mean_y)**2

var_x = numerator_x/n
var_y = numerator_y/n

sd_x = (var_x)**(1/2)
sd_y = (var_y)**(1/2)

numerator = 0
for i in range(n):
    numerator += (x[i] - mean_x) * (y[i] - mean_y)

cov = numerator/n

pearson_correlation_coefficient = cov / (sd_x * sd_y)

print(round(pearson_correlation_coefficient,3))
