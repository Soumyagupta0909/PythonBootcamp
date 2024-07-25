#IMP!!
# reverse a number 
n=int(input())
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(rev)
print(int(rev))
print(type(rev))
