'''check password valid using nested if'''

password = str(input("Enter the password ="))

if len(password) >= 10:
    print("Length criteria met")
    if "@" in password and "#" in password:
        print("Password valid ... access granted")
    else:
        print("Invalid password...! password must contain atleast on special charecter(@ or #)")

else:
    print("Password invalid:  password contain atlest 10 charecter")
