'''code for ticket price based on age'''

age=int(input("Enter the age ="))
if age>=18 and age<=30:
    print("ticket price is 150:")
elif age>=31 and age<=55:
    print("ticket price is 130:")
elif age>=56 and age<=70:
    print("ticket price is 100:") 
else:
    print("There is an age limit...:")