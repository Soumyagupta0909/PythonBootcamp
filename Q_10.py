#print the element in particular index(cyclic rotation)
'''k=3
3 6 8 4 61 2
op=4
--------
k=8
80 70 54 36 72
op=36'''

ab=list(map(int,input().split(",")))
k=int(input("enter k"))
idx=k%len(ab)
print(ab[idx])# if it is 1 base index idx-1
