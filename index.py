from create_account import create_account


print("Hello there, welcome to my first python bank!")

customer_operation = {
    1: "open account",
    2: "withdraw",
    3: "deposit",
    4: "buy airtime",
    5: "check balance",
    6: "exit",
}

# try:
# except TypeError as e:
#     input_error_msg = "string" if len(selected_operation) > 0 else "character"
#     print("expected a number but got a", input_error_msg)
print(customer_operation)
selected_operation = input("What would you like to do? ")

while selected_operation != 6:
    if selected_operation == 1:
        print('Entered here')
        print("Let's work through the process of getting you your account, shall we?")

        create_acc_response = create_account()
        print("New account: ", create_acc_response)
