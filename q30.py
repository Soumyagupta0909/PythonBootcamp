#print the sum of numbers in a given string
n=input()
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
#i="hello world"
inp=n.lower()
for n in inp:
    if(n in check):
        ans += int(n)
print(ans)
