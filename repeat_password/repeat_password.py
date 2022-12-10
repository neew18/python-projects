password = input("Password: ")

while True:
    repeatPassword = input("Repeat password: ")
    if repeatPassword == password :
        break
    print("They do not match!")
print("User account created!")
