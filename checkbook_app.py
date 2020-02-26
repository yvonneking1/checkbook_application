with open("transactions.txt", "r") as f:
    balances = f.readlines()

#global variables - putting at beginning to ensure helper functions and print statements run

balance_transactions_list = balances

greeting = "*~ Wilkommen, welcome to your terminal checkbook ~*"

border = "*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"

menu_header = "Options availabe:"

menu_options = "1.view account balance\n2. make a deposit\n3.make a withdrawel\n4. eixit the application"

input_message = "Please make your selection"

goodbye = "Aufwiedersehen! Have a wonderful day!"

transactions_file = "transactions.txt"

#app greeting statements
print("\n")
print(border)
print(greeting)
print(border)
print("\n")
print(menu_header)
print(menu_options)
print("\n")

#helper functions
def remove_new_line_characters(some_list = balance_transactions_list):
    new_list = []
    for item in some_list:
        new_list.append(item.replace("\n", ""))
    return new_list

def convert_item_to_float(some_list = balance_transactions_list):
    new_list = []
    for item in some_list:
        new_list.append(float(item))
    return new_list

def sum_of_all_transactions(some_list = balance_transactions_list):
    return sum(convert_item_to_float((remove_new_line_characters(some_list))))

def view_account_balance(some_list = balance_transactions_list):
    return sum_of_all_transactions(some_list)

def add_a_deposit_to_file(amount):
    with open("transactions.txt", "a") as f:
        f.write(amount)

def add_a_withdrawel_to_file(amount):
    with open("transactions.txt", "a") as f:
        f.write(amount)



while True:
    user_input_for_menu_selection = input("How would you like to proceed?")
    user_input_for_menu_selection = int(user_input_for_menu_selection)
    if user_input_for_menu_selection == 1:
        print("Your current balance is $", str(view_account_balance()))
        print("\n")
        print(menu_header)
        print(menu_options)
        print("\n")
    elif user_input_for_menu_selection == 2:
        deposit_amount = input("How much would you like to deposit?")
        add_a_deposit_to_file(deposit_amount + "\n")
        print("Your new blance is $", str(view_account_balance() + float(deposit_amount)))
    else:
        print("\n")
        print(goodbye)
        print("\n")
        print(border)
        break