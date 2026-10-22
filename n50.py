'''code for ATM menu using match case'''

print("....ATM menu....")
print("1..Check your balence.")
print("2..withdraw money.")
print("3..Deposite monoy")
print("4...Exit.")

choice=int(input("Enter the choice = "))

match choice:
    case 1:
        print("Your balance is RS 4000:")
    case 2:
        print("withdraw money:")
    case 3:
        print("Deposite money:")
    case 4:
        print("Thank you for using ATM...visit again.!")
    case _:
        print("Invalid choice:")        