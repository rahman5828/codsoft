import random
import string

char = string.ascii_lowercase

length = int(input("How many characters should the password be?\n"))

sensitive = input("Case sensitive? [Y/N]\n").lower()
if sensitive == "y" or sensitive == "yes":
    case = string.ascii_uppercase
    char += case
elif sensitive == "n" or sensitive== "no":
    characters = char.replace(case, "")


numbers = input("Numbers? [Y/N]\n").lower()
if numbers == "y" or numbers == "yes":
    numbers = "1234567890"
    char += numbers
elif numbers == "n" or numbers == "no":
    char= char.replace(numbers, "")


special = input("Type all special characters you want to allow, or press Enter for no special characters.\n")
char+= special


password = ""
for c in range(length):
    password += random.choice(char)

print('This is your password :',password)
print('*****Password Successfully Generated*****')