import csv


def login():
    print("Welcome to the system, please log in!")

    with open("users.csv", "r+") as file:
        reader = csv.reader(file)
        findUser(reader)
        print(file.readline())
        file.write("\nHello")
        file.close()


def findUser(file):
    user = input("Enter Username:")
    for row in file:
        if row[0] == user:
            print("Username found:", user)
            UserFound = [row[0], row[2]]
            pass_check(UserFound)
            break
        elif row[0] != user:
            print("This user has not been found, please create an account!")
            username = input("Username:")
            print(username)
            break


def pass_check(UserFound):
    user = input("Enter Password:")
    if UserFound[1] == user:
        print("Password Matched, You Are Now Logged In")
        LoggedIn = True
    else:
        print("This password did not match")
        LoggedIn = False


login()
