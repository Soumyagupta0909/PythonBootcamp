'''find max element in agiven list
TestCase0
12 23 36 44 45 57
57

'''
'''rint("enter list elements")
ab=list(map(int,input().split(",")))
print(max(ab))'''

print("enter list elements")
ab=list(map(int,input().split(",")))
max=ab[0]
for i in range(len(ab)):
    if ab[i]>max:
        max=ab[i]
print(max)
