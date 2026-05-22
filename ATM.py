accounts = {
  "name": "Jagdish",
  "pin": "1994",
  "balance": 5000,
  "transaction": []
}
def check_pin():
  pin_code = input("Enter Pin:")
  if pin_code.isdigit() and len(pin_code) == 4:
    return pin_code
    
def show_menu():
  print(f"Welcome!{accounts['name']}\n")
  print("Withdraw: press 1")
  print("Exit: press 2 \n")
  while True:
    option = int(input("Choose Option: "))
    if 1 <= option <= 2:
      return option
    else:
      print("Invalid selection: Try again.")
  
def withdraw():
  withdraw_amount = int(input("Enter amount: "))
  if accounts["balance"] >= withdraw_amount:
    print(f"Take you ${withdraw_amount} cash.")
    accounts["balance"] -= withdraw_amount
    print(f"Your new balance is $ {accounts['balance']}")
    accounts["transaction"].append({
      "type":"withdraw",
      "amount":withdraw_amount})
  else:
    print(f"Insufficent fund, Your current balance is: ${accounts['balance']}")

pincode = check_pin()
if pincode == accounts["pin"]:
  while True:
    option = show_menu()
    if option == 1:
      withdraw()
    elif option == 2:
      print("Thank You! Good Bye!")
      break
    
else:
  print("Wrong PIN")