# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
x = [int(i) for i in input().strip().split(' ')]

x = sorted(x)
if n % 2 == 0:
    q2 = ( x[int((n/2)-1)] + x[int(((n/2)+1)-1)] )/2
    li1 = x[:int((n/2))]
    li2 = x[int(((n/2)+1)-1):]
else:
    q2 = x[int(((n+1)/2)-1)]
    li1 = x[:int(((n+1)/2)-1)]
    li2 = x[int(((n+1)/2)):] 

n1 = len(li1)
li1 = sorted(li1)
if n1 % 2 == 0:
    q1 = ( li1[int((n1/2)-1)] + li1[int(((n1/2)+1)-1)] )/2
else:
    q1 = li1[int(((n1+1)/2)-1)]

n2 = len(li2)
li1 = sorted(li2)     
if n2 % 2 == 0:
    q3 = ( li2[int((n2/2)-1)] + li2[int(((n2/2)+1)-1)] )/2
else:
    q3 = li2[int(((n2+1)/2)-1)]

print(int(q1))
print(int(q2))
print(int(q3))
