SECRET_PASSWORD = "1994"
balance = 1000


def check_pwd():
    while True:
        password = input("Enter Password: ")
        if password.isdigit():
            return password
        else:
            print("Please enter digits only.")


def show_menu():
    print("\nCheck Balance Press: 1")
    print("Withdraw Press: 2")
    print("Deposit Press: 3")
    print("Exit Press: 4")


def select_option(prompt):
    try:
        option = int(input(prompt))
        if 1 <= option <= 4:
            return option
        else:
            print("Enter valid option.")
    except ValueError:
        print("Enter valid option.")


def check_balance():
    print(f"Your balance is ${balance}")


attempt = 5

while attempt > 0:
    attempt -= 1

    if SECRET_PASSWORD == check_pwd():
        print("Welcome")

        while True:
            show_menu()
            option = select_option("Choose option: ")

            if option == 1:
                check_balance()

            elif option == 2:
                print("Withdraw feature coming soon.")

            elif option == 3:
                print("Deposit feature coming soon.")

            elif option == 4:
                print("Goodbye.")
                break

        break

    else:
        print("Incorrect password! Try again.")

else:
    print("Too many attempts, you're locked out.")