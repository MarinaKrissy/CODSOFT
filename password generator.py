import string
import random

length = int(input("Enter password length: "))

print("Choose character set for password:")
print("1. Digits")
print("2. Letters")
print("3. Special Characters")
print("4. Generate Password")

characters = ""

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        characters = characters + string.digits

    elif choice == 2:
        characters = characters + string.ascii_letters

    elif choice == 3:
        characters = characters + string.punctuation

    elif choice == 4:
        break

    else:
        print("Invalid choice!")

if characters == "":
    print("No character set selected.")

else:
    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    print("Generated Password:", password)