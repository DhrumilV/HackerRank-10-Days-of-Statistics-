# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
x = [int(i) for i in input().strip().split(' ')]
w = [int(i) for i in input().strip().split(' ')]

numerator = 0
denominator = 0
for i in range(n):
    numerator += (x[i]*w[i])
    denominator += w[i]
    
ans = numerator/denominator
print(round(ans,1))
