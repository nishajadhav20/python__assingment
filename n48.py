'''check language choice based on based on match case'''

Language = int(input("Enter the language choice = "))

match Language:
    case 1:
        print("You choose MARATHI language:")
    case 2:
        print("You choose HINDI language:")
    case 3:
        print("You choose ENGLISH language:")
    case 4:
        print("You choose KANNAD language:")
    case 5:
        print("You choose GUJRATI language:")    
    case 6:
        print("You choose SANSKIT language:") 
    case _:
        print("Invalid language choice:")      