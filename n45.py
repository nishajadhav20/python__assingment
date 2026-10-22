'''print menu base food selection'''

menu=int(input("Enter the menu number =  "))
match menu:
    case 1:
        print("Dal rice")
    case 2:
        print("Bhaji chapati")
    case 3:
        print("Manchurian rice")
    case 4:
        print("Idali sanber with chatani")        
    case 5:
        print("Italian pasta")
    case 6:
        print("fride rice")    
    case _:
        print("please! Enter valid menu number")    