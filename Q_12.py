#print min of list
print("enter list elements")
ab=list(map(int,input().split(",")))
min=ab[0]
for i in range(len(ab)):
    if ab[i]<min:
        min=ab[i]
print(min)
