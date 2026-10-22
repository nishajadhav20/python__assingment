'''check user role using match case'''

role=input("Enter the role user/admin/guest = ")

match role:
    case "ADMIN":
        print("ADMIN..! you have full access:")
    case "USER" :
        print("USER..! you have normal access:")   
    case "GUEST" :
        print("GUEST..! you have limited access:")   
    case _:
        print("Invali Role... Please Enter Valid Role.")     