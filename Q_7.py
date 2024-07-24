#you are given with a comma separated natural numbers 1 to 10 now print only even numbers
#my_list=list(map(int,input().split(",")))
a=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in range(1,11,2):
    print(a[i])
    count+=1
    #print(my_list[i])
print(count)
#you are given with a space separated integer list find no of even and no of odd elements
my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(0,len(my_list),1):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)