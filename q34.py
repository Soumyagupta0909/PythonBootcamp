#write a code to print all the capital letters in a given string
n=input()
s=" "
for i in n:
    if(ord(i)>=65 and ord(i)<=90):
        s+=i
print(s)
