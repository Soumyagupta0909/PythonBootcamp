'''take input from user and print whether the number is even +ve or even-ve or odd+ve or odd-ve'''
a=int(input("enter a"))
if(a%2==0 and a>0):
    print("even positive")
elif(a%2==0 and a<0):
    print("even negative")
elif(a%2!=0 and a>0):
     print("odd positive")
else:
    print("odd negative")
    a=int(input("enter a"))
if(a%2==0 and a>0):
    print("even positive")
elif(a%2==0 and a<0):
    print("even negative")
elif(a%2!=0 and a>0):
     print("odd positive")
else:
    print("odd negative")
