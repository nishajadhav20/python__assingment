'''check the person apply for a loan'''

age = int(input("Enter the age ="))
salary = int(input("Enter the salary="))

if age >= 21 :
    if salary >= 25000:
     print("Person can apply a loan:")
    elif salary >=15000:
     print("You can apply a small loan:")
    else:
     print("Salary is too low:")
else:
 print("age is too low:")