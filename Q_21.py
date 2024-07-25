#peek element VERY IMPPPPPPPPPPPPPP
'''print("enter elements")
peek=list(map(int,input().split(",")))
n=len(peek)-
for i in range(1,n-1):
    if(peek[i]>=peek[i-1] and peek[i]>=peek[i+1]):
        print(peek[i])
'''

#to print all peek
'''print("enter elements")
peek=list(map(int,input().split(",")))
count=0
for i in range(1,len(peek)-1):
    if(peek[i]>=peek[i-1] and peek[i]>=peek[i+1]):
        #count=i     use when u need only one peak element
        print(peek[i],end=" ")'''

#swap 2 numbers 
'''n=int(input())
m=int(input())
n=n-m
n,m=m,n
print(n,m)

'''
n=int(input("enter"))
sum=n*(n+1)/2

print(sum)
