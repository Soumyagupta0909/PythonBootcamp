''' if a person's age is >18and less 24 then print can drive 2 wheeler
>24 less 50 can drive 2 and 4 wheeler
>45 can drive 2 4 6 wheeler'''
age=int(input("enter age"))
if(age>=18 and age<24):
    print("only 2 wheeler")
elif(age>=24 and age<50):
    print("4 wheeler")
elif(age<18):
    print("go sleep")
else:
    print("2,4,6 wheeler")
