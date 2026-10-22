'''to check given number positive or  even/odd'''

num= int (input("Enter the number = "))

if num > 0 :
    if num % 2 == 0:
        print("The number is positive but even:")
    else:
        print("The number is positive but odd:")
else:
    print("The number is not positive")
    