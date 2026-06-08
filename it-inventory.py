devices = [
    {"name": "PC-01", "type": "Laptop", "status": "Online", "age": 2},
    {"name": "PC-02", "type": "Desktop", "status": "Offline", "age": 5},
    {"name": "SRV-01", "type": "Server", "status": "Online", "age": 7},
    {"name": "PC-03", "type": "Laptop", "status": "Online", "age": 4},
    {"name": "SRV-02", "type": "Server", "status": "Offline", "age": 8}
]
def show_menu():
  draw_lines()
  print("1. Show all devices\n2. Search by type\n3. Show offline devices\n4. Show online devices\n5. Count devices by type\n6. Exit")
def draw_lines():
  i = 1
  while i <= 2:
    print("-"*50)
    i+=1
def header(title):
    draw_lines()
    print(title)
    draw_lines()
    
def display_devices():
  for device in devices:
    print(f"Name: {device["name"]} | Type:{device["type"]} | Status: {device["status"]} | Age : {device["age"]}")

def device_type():
  user_input = input("Search by device type:")
  user_input = user_input.strip().capitalize()
  found = False
  count = 0
  for device in devices:
    if user_input in device["type"]:
      print(f"Name: {device["name"]} | Type:{device["type"]} | Status: {device["status"]} | Age : {device["age"]}.")
      found = True
      count += 1
  print(f"Available devices:{count}")
  

def offline_devices():
  for device in devices:
    if "Offline" == device["status"]:
      print(f"Name: {device["name"]} | Type:{device["type"]} | Status: {device["status"]} | Age : {device["age"]}")
      
def online_devices():
  for device in devices:
    if "Online" in device["status"]:
      print(f"Name: {device["name"]} | Type:{device["type"]} | Status: {device["status"]} | Age : {device["age"]}")
      
def device_counter():
  device_with_type = {}
  for device in devices:
    device_type = device["type"]
    if device_type in device_with_type:
      device_with_type[device_type] += 1
    else:
      device_with_type[device_type] = 1
      
  print(device_with_type)
      

while True:
    show_menu()

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        header("DISPLAY DEVICES")
        display_devices()

    elif choice == 2:
        header("SEARCH BY TYPE")
        device_type()

    elif choice == 3:
        header("OFFLINE DEVICES")
        offline_devices()
    elif choice == 4:
        header("OFFLINE DEVICES")
        offline_devices()
    elif choice == 5:
        header("DEVICES COUNT BY THEIR TYPES")
        device_counter()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Please choose a valid option.")