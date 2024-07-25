#print all the vowels followed by consonants
n=input()
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyz"
ans=" "
#i="hello world"
inp=n.lower()
for n in inp:
    if(n in vowels):
        ans+=n
for n in inp:
    if n in consonants:
        ans+=n
print(ans)
