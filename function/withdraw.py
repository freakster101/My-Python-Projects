# Question 1 greet_user()
def greet_user(name = "user"):
    print(f"Hello, {name}")
greet_user()
greet_user("HemKumar")

# Question 2 square_num()

def square_num(a):
    print(a * a)
square_num(5)

# Question 3 is_even()
def is_even(a):
    if a % 2 == 0:
        print(f"{a} is even")\
    else:
print(f"{a} is odd")
is_even(5)
is_even(10)

# Question 4 check_password()
def check_password(password):
    password = input("Enter password: ")
    if password == "python123":
        print("Access Granted")
        return password
    else:
        print("Access Denied")
check_password()

# Question 5 Withdraw()
def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(f"${amount} has been withdrawn \n")
        print(f"Your new balance is ${balance}")
        return balance
    else:
        print("Insufficient Balance")
withdraw(1000, 2000)
withdraw(1000, 100)

# Question 6 Multiple functions
def check_amount(amount):
    if amount % 50 == 0 and amount <= 1000:
        return amount
    else:
        print("Amount has to be in 50s and less than 1000")

def withdraw_amount(balance, amount):
    if 0 < amount <= balance:
        check_amount(amount)
        balance -= amount
        print(f"${amount} has been withdrawn \n")
        print(f"Your new balance is ${balance}")
        return balance
    else:
        print("Insufficient Balance")


#Question 7 calculator()
def calculator(a, b, operator):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        print(a / b)
# Confusion
calculator(1,2,"+")
calculator(5,2, "-")
calculator(10, 5, "*")
calculator(100, 20, "/")


# Question 8 Login()
password = "1994"
attempt = 1
def login(saved_password, entered_password, attempt ):
    while attempt <= 5:
        entered_password = input("Enter password")
        attempt += 1
        if saved_password == entered_password:
            print ("Access granted")
        else:
            print(f"incorrect password! Try again you have {attempt} attempts left")
    else:
        print("Too many attempts, you are locked out!!!")