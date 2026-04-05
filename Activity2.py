numlarge=int(input("Enter the largest number"))
numsmall=int(input("Enter the small number"))

while(numsmall):
    numstore=numsmall
    numsmall=numlarge%numsmall
    numlarge=numstore

print(f"HCF is:  {numlarge}")