#find the duplicates in an array,membership operATOR = in,notin
m=list(map(int,input().split(" ")))
a=[]
b=[]
for element in m:
    if element in a and element not in b:
        b.append(element)
    else:
        a.append(element)
print(b)
