import random


def create_account():
    print("Please fill in the following details")
    name = input("Full name: ")
    phone_number = input("Phone number: ")
    email = input("Email: ")
    pin = None
    account_type = None

    trial = 3

    while trial > 0:
        pin = input("pin: ")

        if len(pin) != 4:
            trial -= 1
            print("pin must be 4 characters")
            pin = None
            continue
        else:
            trial = 3

        account_type_display = {1: "savings", 2: "current", 3: "credit"}
        account_type_option = ["savings", "current", "credit"]

        print(account_type_display)
        selected_account_type = input("kindly select account type: ")

        if selected_account_type < 0 or selected_account_type > 3:
            trial -= 1
            print("You can only select between 1 - 3 for account type")
            continue

        account_type = account_type_option[selected_account_type]
        break

    account_number = random.randint(10**9, (10**10) - 1)

    user_data = {
        account_name: name,
        user_email: email,
        phone_number: phone_number,
        security_pin: pin,
        account_number: account_number,
        account_type: account_type,
        balance: 0,
    }

    return user_data
