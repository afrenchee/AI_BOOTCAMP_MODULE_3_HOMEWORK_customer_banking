# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

import os, sys
windows_is_the_OS = False # This variable is set by the main programmer to ensure that Terminal / Command Prompt commands are correctly executed in clear_screen() and end_program()



def clear_screen(): # You best be usin a terminal or powershell for this code!!!
    if windows_is_the_OS:
        os.system('cls')
    else:
        os.system('clear')



def print_invalid_input(invalid_input):
    print(f"\n{invalid_input} is not a valid input you silly goose!!!\n")



def end_program():
    if windows_is_the_OS:
        os.system('dir')
    else:
        os.system('pwd')
        os.system('ls')
    print("")
    sys.exit()



# Define the main function
def main():
    """This function prompts the user to enter
        - the savings and
        - cd account balance,
        - interest rate,
        - and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    clear_screen()
    print("Welcome to PRETEND INTERNATIONAL BANK!\n")
    while True:
        user_input_balance = input("Please enter an integer USD balance number for your pretend savings account calculator extrordinare!!! $")
        if user_input_balance.isdigit():
            clear_screen()
            break
        else:
            print_invalid_input(user_input_balance)
    print("Next step!\n")
    while True:
        user_input_interest = input("Please enter an integer for the yearly interest rate percent for your pretend savings account calculator extrordinare!!!: ")
        if user_input_interest.isdigit():
            clear_screen()
            break
        else:
            print_invalid_input(user_input_interest)
    print("Almost done!\n")
    while True:
        user_input_months = input("Please enter an integer for the number of months invested in your pretend savings account calculator extrordinare!!!: ")
        if user_input_months.isdigit():
            clear_screen()
            break
        else:
            print_invalid_input(user_input_months)
    # Call the create_savings_account function and pass the variables from the user.
    updated_balance, interest_earned = create_savings_account(user_input_balance, user_input_interest, user_input_months)

    # Print out the interest ecarned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    clear_screen()
    print("\nWell done User! Now it's time to repeate everything with the CD stuff!")

    print(f"Interest earned: ${interest_earned}")
    print(f"Updated savings account balance: ${updated_balance}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    # Call the create_cd_account function and pass the variables from the user.
    #updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    while True:
        user_input_balance = input("Please enter an integer USD balance number for your pretend CD account calculator extrordinare!!! $")
        if user_input_balance.isdigit():
            clear_screen()
            break
        else:
            print_invalid_input(user_input_balance)
    print("Next step!\n")
    while True:
        user_input_interest = input("Please enter an integer for the interest rate percent for your pretend CD account calculator extrordinare!!!: ")
        if user_input_interest.isdigit():
            clear_screen()
            break
        else:
            print_invalid_input(user_input_interest)
    print("Almost done!\n")
    while True:
        user_input_months = input("Please enter an integer for the number of months invested in your pretend CD account calculator extrordinare!!!: ")
        if user_input_months.isdigit():
            clear_screen()
            break
        else:
            print_invalid_input(user_input_months)
    updated_balance, interest_earned = create_cd_account(user_input_balance, user_input_interest, user_input_months)

    print("\nWell done User! Here are your CD results\n")

    print(f"Interest earned: ${interest_earned}")
    print(f"Updated savings account balance: ${updated_balance}\n")

    end_program()





if __name__ == "__main__":
    # Call the main function.
    main()



