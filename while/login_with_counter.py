print("Hi there, this is a superuser gateway")
loop = True
attempts = 0
while loop:
    username = input("Username: ")
    if username != "c4e":
        print("You are not superuser")
    else:
        password = input("Password: ")
        if password != "codethechange":
            print("Password is incorrect")
        else:
            print("Welcome, c4e")
            break

    attempts += 1
    if attempts == 3:
        print("You filed to log in 3 times, go away")
        loop = False
