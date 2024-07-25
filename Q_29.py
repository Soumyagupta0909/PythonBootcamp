#print unique characters(non repeated) in a string
i=input()
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyz"
ans=" "
#i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)
