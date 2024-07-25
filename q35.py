#remove all the braces from the given algebraic expressionn using ascii values
n=input()
a=" "
for i in n:
    if ord(i)==40 or ord(i)==42 or ord(i)==91 or ord(i)==123 or ord(i)==93 or ord(i)==1245:
        pass
    else:
        print(i,end="")


