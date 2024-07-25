#prime using square root(mosttttttt optimised code for prime number)
n=int(input())
r=n**0.5
count=0
if n==1:
    print("neither prime nor composite")
for i in range(2,int(r+1)):
    if n%i==0:
        count=1
        break
if count==0:
    print("prime")
else:
    print("not prime")
