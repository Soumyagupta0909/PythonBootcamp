# leap year
# logic=year should be divisible by400 or divisible by 4 and not divisible by 100
'''leap=int(input())
if leap%400==0 or (leap%4==0 and leap%100!=0):
    print("leap year")
else:
    print("not leapyear")'''

leap1=int(input())
leap2=int(input())
for i in range(leap1,leap2+1):
    if i%400==0 or (i%4==0 and i%100!=0):
        print(i)