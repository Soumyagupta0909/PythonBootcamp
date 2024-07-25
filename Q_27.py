#wap to print all the consonants
'''n=input()
vowels="aeiouAEIOU"
count=0
for i in n:
    if i not in vowels:
        count+=1
print(count)
  #or

n=input()
vowels="bcdhghjklmnpqrstvwxyz"
count=0
hey=vowels.upper()
for i in n:
    if i not in hey:
        count+=1
print(count)
'''
check="aeiou"
abc="bcdhghjklmnpqrstvwxyz"
count=0
c=0
n="hello world"
n=n.lower()
for i in n:
    if(i in check):
        count+=1
print(count)
for i in n:
    if(i in abc):
        count+=1
print(abc)
