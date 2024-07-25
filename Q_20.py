#mr.x is trying to create a new password for hois inmstagram account .these are the required conditiuons for creating a new password
# 1.minimum length is 8,max is 15
# 2.only @,/is must include in a passwoed
# 3.nospaces are allowed
# 4.only alpha numerics are allowed
# 5.you are suopposed to print weak if length is exact 8
# medium if length is between 8 to 12 -strong
# 12-15 = print very strong
print("reset password")
print("type your password")
password=input()
n=len(password)
count=0
if(n<8 or n>15):
    print("please follow rules")
str="@,/"
for i in password:
    if i in str[0] or str[1]:
        count+=1
        break




count=0
for i in a:
    count+=0
    print("go ahead")
if "@" in a and "/" in a:
if(len(password)<8 or len(password)>15):
    print("please follow rules")
if()
elif(len(password)==8):
    print("weak")
elif(len(password)>8 and len(password)<12):
    print("medium")
elif(len(password>12) and len(password)<15):
    print("strong")