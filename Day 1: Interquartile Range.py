# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
x = [int(i) for i in input().strip().split(' ')]
y = [int(i) for i in input().strip().split(' ')]

s = list()
 
for i in range(n):
    for j in range(y[i]):
        s.append(x[i])

s.sort()
#print(s)
n0 = len(s)

if n0 % 2 == 0 :
    s1 = s[:int((n0/2))]
    s2 = s[int((n0/2)):]
else :
    s1 = s[:int((n0-1)/2)]
    s2 = s[int((n0+1)/2):]

s1.sort()
s2.sort()
n1 = len(s1)
n2 = len(s2)

if n1 % 2 == 0 :
    q1 = (s1[int((n1/2)-1)] + s1[int((n1/2))])/2
else:
    q1 = (s1[int((n1-1)/2)])
        
if n2 % 2 == 0 :
    q3 = (s2[int((n2/2)-1)] + s2[int((n2/2))])/2
else :
    q3 = (s2[int((n2-1)/2)])

print(float(q3-q1))
