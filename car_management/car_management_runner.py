from car_management_sys import CarManager

print(f"----  WELCOME  ----\n Below is a list of our options")
for option in option_list:
    print(f'{option["option"]}: {option["description"]}')

user_input = int(input("Enter an option number: "))
CarManager.handle_option(user_input)


