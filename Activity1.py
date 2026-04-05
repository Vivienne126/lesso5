# number=int(input("Enter your number"))

# orig_num=number
# rever=0

# while number>0:
#     digit=number%10   #TO FIND REMAINDER
#     rever=rever*10+digit
#     number=number//10 #TO FIND QUOTIENT

# if rever==orig_num:
#     print(f"{orig_num} is a palindrome")
# else:
#     print(f"{orig_num} is not a palindrome")



#SHORTCUT

number1=int(input("Enter your number"))

# number2=str(number1)
# reversed=number2[::-1]
# reversed_int=int(reversed)

reversed_int=int((str(number1))[::-1])

if reversed_int==number1:
    print(f"{number1} is a palindrome")
else:
    print(f"{number1} is not a palindrome")



