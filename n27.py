'''code to check login status'''

username = int(input("Enter the username  ="))
password = int(input("Enter the password  ="))
 

if username ==  2062005 and password == 223344:
    otp = int(input("Enter the OTP ="))
    if otp == 305687:
        print("Login successful done")
    else:
        print("Entet valid OTP:") 
else:
    print("login unsuccessful:")   