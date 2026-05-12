SECRET_PASSWORD = "1994"

def check_pwd():
    while True:
        password = input("Enter Password: ")
        if password.isdigit():
            return password
        else:
            print("Please Enter Digit")

def show_menu():
    print("Check Balance press: 1\n")
    print("WIthdraw Press: 2")
    print("Deposit Press: 3")
    print("Exit Press: 4")

def select_option(prompt):
    try:
        option = int(input(prompt))
        if 1 <= option <= 4:
            return option
        else:
            print("Enter Valid Option")
    except ValueError:
        print("Enter Valid Option")

attempt = 5
while attempt > 0:
    attempt -= 1
    if SECRET_PASSWORD == check_pwd():
        print("Welcome\n")
        show_menu()

    else:
        print("Incorrect Password!! Try again")
else:
    print("Too many Attempts, You're Locked Out")

