z=True
medals_mrz= 14 * 50/100
print(medals_mrz)
print("selection of badminton")
p1=input("enter name")
height=int(input("enter ur height"))
weight=int(input("enter weight"))
if(height==140 and weight%2==0):
    print("selected")
    x=True
else:
    print("not selected")
    x=False
ht=int(input("enter ur height"))
wt=int(input("enter weight"))
if(ht>=118 and ht<148 and wt%medals_mrz==0):
    print("selected")
    y=True
else:
    print("not selected")
    y=False
if(x==True and y==True and z==True):
    print("all 3 same plane")
else:
    print("no")
