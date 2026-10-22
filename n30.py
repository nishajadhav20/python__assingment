'''code to check number is single, two or three digit'''

num = int(input("Enter a number="))

if num >= 0 and num<= 9:
    print("The number is single digit:")
elif num >= 10 and num <= 99:
    print("The number is two digit:")
elif num >= 100 and num <= 999:
    print("The number is three digit:")
else:
    print("number is out of range:")