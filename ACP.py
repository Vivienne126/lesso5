
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

maxx=max(num1 , num2)

while True: 
    if maxx%num1==0 and maxx%num2==0:
        lcm=maxx
        break
    maxx=maxx+1

print(f"LCM is {lcm}")

