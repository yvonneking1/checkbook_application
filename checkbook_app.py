
#global variables - putting at beginning to ensure helper functions and print statements run


greeting = "*~ Wilkommen, welcome to your terminal checkbook ~*"

border = "*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*"

small_border = "*~*~*~*~*~*~*~*~*"

menu_header = "Options availabe:"

menu_options = "1. View account balance\n2. Make a deposit\n3. Make a withdrawel\n4. Exit the application"

input_message = "Please make your selection"

goodbye = "Aufwiedersehen! Have a wonderful day!"

transactions_file = "transactions.txt"

#app greeting statement
print("\n")
print(border)
print(greeting)
print(border)
print("\n")
print(menu_header)
print(menu_options)
print("\n")

#helper functions
def remove_new_line_characters(some_list):
    new_list = []
    for item in some_list:
        new_list.append(item.replace("\n", ""))
    return new_list

def convert_item_to_float(some_list):
    new_list = []
    for item in some_list:
        new_list.append(float(item))
    return new_list

def sum_of_all_transactions():
    with open("transactions.txt", "r") as f:
        balances = f.readlines()
    return sum(convert_item_to_float((remove_new_line_characters(balances))))

def view_account_balance(some_list):
    return sum_of_all_transactions(some_list)

def add_a_deposit_to_file(amount):
    with open("transactions.txt", "a") as f:
        f.write(amount)

def add_a_withdrawel_to_file(amount):
    with open("transactions.txt", "a") as f:
        f.write(amount)

def convert_withdrawel_input_to_negative(amount):
    return -(float(amount))

while True:
    user_input_for_menu_selection = input("How would you like to proceed?")
    print("\n")
    if user_input_for_menu_selection not in ("1", "2", "3", "4"):
        print("Invalid input")
        user_input_for_menu_selection = input("How would you like to proceed?")

    user_input_for_menu_selection = int(user_input_for_menu_selection)
    
    
    if user_input_for_menu_selection == 1:
        print("Your current balance is $", str(sum_of_all_transactions()))
        print("\n")
        print(menu_header)
        print(menu_options)
        print("\n")
    
    elif user_input_for_menu_selection == 2:
        deposit_amount = input("How much would you like to deposit?")
        if deposit_amount.isnumeric():
            if int(deposit_amount) > 0:
                add_a_deposit_to_file(deposit_amount + "\n")
                print("\n")
                print("Your new blance is $", str(sum_of_all_transactions()))
                print("\n")
                print(small_border)
                print(menu_header)
                print("\n")
                print(menu_options)
                print("\n")

        else:
            print("\n")
            print("Invalid input")
            print("\n")
            print(small_border)
            print(menu_header)
            print("\n")
            print(menu_options)
            print("\n")
    
    elif user_input_for_menu_selection == 3:
        withdraw_amount = input("How much would you like to withdraw?")
        if withdraw_amount.isnumeric():
            if float(withdraw_amount) > sum_of_all_transactions():
                print("\n")
                print("Insuffiicient funds")
                print("\n")
                print(small_border)
                print(menu_header)
                print("\n")
                print(menu_options)
                print("\n")
            else:
                withdraw_amount = convert_withdrawel_input_to_negative(withdraw_amount)
                add_a_withdrawel_to_file(str(withdraw_amount) + "\n")
                print("\n")
                print("Your new balance is $", str(sum_of_all_transactions()))
                print("\n")
                print(small_border)
                print(menu_header)
                print("\n")
                print(menu_options)
                print("\n")
        else:
            print("\n")
            print("Invalid input")
            print("\n")
            print(small_border)
            print(menu_header)
            print("\n")
            print(menu_options)
            print("\n")
        
    else:
        print("\n")
        print(goodbye)
        print("\n")
        print(border)
        print("\n")
        break