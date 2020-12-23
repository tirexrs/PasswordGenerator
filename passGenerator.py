import random
import string

domain = input("""Welcome to this password generator!
For which app or website would you like to generate the password? """)
lvl = int(input("How much do you want the lenght of your password? "))
type = input("Choose your password type (P for PIN; L for Letters And Digits; S for Strongest Password Ever): ")
usernameOrEmail = input("What's your username or email to save it with the password? ")
strongest = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()_+=-<>?/:;{}[]", k= lvl))
pin = ''.join(random.choices(string.digits , k= lvl))
lettersAndDigits = ''.join(random.choices(string.ascii_letters + string.digits, k= lvl))
password = 0
if type == "S" or type == "s":
    password = strongest
    print(password)
    print("Your password have been saved to 'Password Generator.txt'")
elif type == "P" or type == "p":
    password = pin
    print(password)
    print("Your password have been saved to 'Password Generator.txt'")
elif type == "L" or type == "l":
    password = lettersAndDigits
    print(password)
    print("Your password have been saved to 'Password Generator.txt'")
else:
    print("Please answer with 'S', 'P', or 'L'.")
with open("Password Generator.txt", "a+") as appendFile:
    appendFile.write(f"{domain} : email or username = {usernameOrEmail}, password = {password}\n")