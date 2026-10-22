'''code for vowel or consonant'''
charecter=str(input("enter the charecter:"))
if charecter in ("a","e","i","o","u"):  #it is use membership operator (in)
    print("it is a vowel:")
else:
    print("it is a consonant:")