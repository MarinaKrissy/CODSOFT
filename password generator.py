import random
import string

length = int(input("Enter the password length: "))

chars = ""

print("Select the characters you want in the password")
print("1. Numbers")
print("2. Letters")
print("3. Special Characters")
print("4. Generate Password")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        chars += string.digits
    elif choice == "2":
        chars += string.ascii_letters
    elif choice == "3":
        chars += string.punctuation
    elif choice == "4":
        break
    else:
        print("Please enter a valid option.")

if chars:
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Your Password is:", password)
else:
    print("You did not select any character set.")