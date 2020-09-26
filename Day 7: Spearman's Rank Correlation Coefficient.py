# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

rank_x = [(sorted(x).index(i) + 1) for i in x]
rank_y = [(sorted(y).index(i) + 1) for i in y]

d = []
for i in range(n):
    d.append(float(rank_x[i]-rank_y[i])**2)

r_xy = 1- ( 6 * sum(d)/ (n * (n**2 -1)) )

print(round(r_xy,3))
