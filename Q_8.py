#given an space separated integer list .find avg of elements present in the even index
my=list(map(int,input().split(" ")))
evensum=0
count=0
for i in range(len(my)):
    if i%2==0:
        evensum += my[i]
        count += 1
print(evensum/count)