import random

values = []
for i in range(1,1000):
    values.append(random.randint(1, 1000))
values.sort()
k=20
def busquedabin(values, k):
    l=0
    r=len(values)
    while l<=r:
        m=(l+r)//2
        if(k==values[m]):
            return m
        elif(k<values[m]):
            r=m-1
        else:
            l=m+1
    return -1
result=busquedabin(values,k)
if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")