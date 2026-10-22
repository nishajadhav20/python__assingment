'''to check student eligible for exam'''
from colorama import Fore,Back,init
init()
marks = int( input("Enter the marks = "))
attendance = int( input(" Enter the Attendance="))
if marks >= 40 and attendance >= 75:

    print(Fore.GREEN+Back.WHITE+"Student elligible for exam:")
else:
    print(Fore.RED+Back.GREEN+"student not elligible for exam:")