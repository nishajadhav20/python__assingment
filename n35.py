'''check the number devisible by 3 or 5'''


num=int(input("enter the number:"))
if num%3==0:   
    print("number divisible by 3")
else: 
    print("number is not divisible by 3:")
    if num%5==0: 
        print("number divisible by 5")
    else: 
        print("number is not divisible by 5:")