#find the missing number in an array of natural numbers
m=list(map(int,input().split(" ")))
n=len(m)+1
totalsum=n*(n+1)//2
listsum=sum(m)
missingnum=totalsum-listsum
print(missingnum)
