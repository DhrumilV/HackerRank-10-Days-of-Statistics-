n = int(input())
arr = [int(i) for i in input().split(' ')]
mean = sum(arr)/n
arr.sort()
if n % 2 == 0:
    median = (arr[n//2] + arr[n//2 - 1])/2
else:
    median = arr[n//2]
mode = arr[0]
modeInstances = 1
instances = 0
for i in range(1,n):
    if arr[i] == mode:
        modeInstances += 1
    elif arr[i] == arr[i - 1]:
        instances += 1
        if instances > modeInstances:
            mode = arr[i]
            modeInstances = instances
    else:
        instances = 1
print(mean)
print(median)
print(mode)
