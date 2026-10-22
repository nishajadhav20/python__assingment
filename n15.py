'''check whether number divisible by 3 and 7'''

num=int(input("enter the number:"))
if num%3==0:   
    print("number divisible by 3")
else: 
    print("number is not divisible by 3:")
    if num%7==0: 
        print("number divisible by 7")
    else: 
        print("number is not divisible by 7:")