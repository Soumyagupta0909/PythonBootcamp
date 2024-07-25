#replace the elements in an array with avg of max and min of element
#13 2 67 20 68
#68+2=70,70/2=35
#op=[35 35 35 35 35 ]


print("enter list elements")
ab=list(map(int,input().split(" ")))
max=ab[0]
min=ab[0]
for i in range(len(ab)):
    if ab[i]>max:
        max=ab[i]
for i in range(len(ab)):
    if ab[i]<min:
        min=ab[i]
sum=max+min
avg=sum//2
print(avg)
for i in range(len(ab)):
    ab[i]=avg
print(ab)
