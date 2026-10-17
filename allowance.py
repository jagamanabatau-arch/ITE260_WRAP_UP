sn=input("Enter your Name: ")
da=int(input("How much your Daily Allowance: ")
te=int(input("Your transportation expences: ")
fe=int(input("Food expences: ")
se=int(input("School expences: ")
oe=int(input("Other expences: ")

e=te+fe+se+oe
bud=da-e

if e <= bud:
    print("You are within your budget")
    
else:
    print("You exceeded your budget")
    
print("Total expences: ",e)
print("Remaining money: ",bud)(e)