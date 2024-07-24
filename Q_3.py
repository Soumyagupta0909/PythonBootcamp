''' x goes to market,he buys 10 apples,2dz bananas,8 oranges
    1-apple=15
    1-banana=4
    1-orange=5
mother of x gave 700 to x 
findout whether x got cheated by shopkeeper or not'''
n=int(input("how much you have?"))
noa=int(input("enter no of apples"))
nob=int(input("enter no of bananas"))
noo=int(input("enter no of oranges"))
totalcost=(noa*15)+(nob*4)+(noo*5)
if(totalcost<n):
    print("not cheated")
else:
    print("cheated")
