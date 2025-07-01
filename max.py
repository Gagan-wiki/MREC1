a = [1,2,4,5,7,3,2]
max = a[0]
for i in range(len(a)):
    if(a[i] > max):
        max = a[i]
print(max)