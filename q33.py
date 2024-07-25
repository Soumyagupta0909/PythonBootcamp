#sum of digits in a string using ascii values
n=input()
sum=0
for i in n:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)
