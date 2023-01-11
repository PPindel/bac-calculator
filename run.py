# imports:
import os
import pyfiglet
import time
import sys
from datetime import datetime

# constants:
FRACTIONOFFLUID = 0.806
GRAVITYOFALCOHOL = 0.79
METABOLISM = 0.012


def clear():
    """
    Clear screen function
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_screen():
    """
    First function in the program, welcomes the user
    """
    clear()
    print(pyfiglet.figlet_format("B A C\nCALCULATOR"))
    time.sleep(1)
    print("***HI! THIS PROGRAM WILL CHECK YOUR BLOOD ALCOHOL CONTENT!***\n")
    print("***AND ANSWER THE QUESTION - CAN YOU LEGALLY DRIVE IN IRELAND?***")
    print("***BASED ON YOUR DRIVING LICENCE TYPE***")
    sys.stdout.write("LOADING THE PROGRAM")
    sys.stdout.flush()
    slow_print("...........................................")
    time.sleep(2)
    clear()


def important_notice():
    """
    Notice for user
    """
    clear()
    print("IMPORTANT NOTICE!")
    print("This program is not accurate enough to calculate the exact blood alcohol")  # noqa E501
    print("content in your body. The obtained result is averaged and does not take")  # noqa E501
    print("into account many individual preferences.\n")
    print("Also, please remember that the best practice is to never drink and drive.\n")  # noqa E501
    input("Press enter to continue...")
    clear()


def slow_print(text):
    """
    Slow printing text function
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.02)


def two_options_validation(a, b, user_choice):
    """
    Function is checking if user selected one of two correct options
    """
    try:
        user_choice = user_choice.capitalize()
        if user_choice != a and user_choice != b:
            raise ValueError(
                f"Wrong data - you entered {user_choice}. Please use {a} or {b} ONLY!"  # noqa E501
            )
    except ValueError as e:
        print(f"ERROR {e}")
        return False

    return True


# user inputs:


def get_name():
    """
    Get the name of the user
    """
    input_name = str(input("Please enter your name (use only letters, no spaces between):\n"))  # noqa E501
    input_name = input_name.strip()

    while not input_name.isalpha():
        print("Invalid name! Please use letters only!")
        input_name = str(input("Please enter your name (use only letters, no spaces between):\n"))  # noqa E501
        input_name = input_name.strip()

    clear()
    hello = f"Hi {input_name}, I need to ask you few questions to calculate your BAC...\n"  # noqa E501
    slow_print(hello)
    return input_name


def letter_choice(message_to_display, first_option, second_option):
    """
    Get the correct alfabetical value from user
    (Licence type and gender type in this program so far...)
    """
    while True:
        users_letter = input(message_to_display)
        users_letter = users_letter.strip()
        if two_options_validation(first_option, second_option, users_letter):
            break

    users_letter = users_letter.capitalize()
    return users_letter


def legal_limit_check(licence_type):
    """
    Function defines legal limit of BAC based on licence type
    """
    limit = 0
    if licence_type == "P":
        limit = 0.02
    elif licence_type == "F":
        limit = 0.05

    return limit


def fluid_fraction_of_body(gender_type):
    """
    Function defines fluid fraction of body based on gender
    """
    if gender_type == "M":
        fluid_fraction_of_user = 0.58
    elif gender_type == "F":
        fluid_fraction_of_user = 0.49

    return fluid_fraction_of_user


def number_validation(message_for_user):
    """
    Get amount of drinks taken
    """
    while True:
        try:
            users_number = float((input(message_for_user)))
            break
        except ValueError:
            print("Invalid value! Please use a numbers only!")
    return users_number


def calculate_again(yes_or_no):
    """
    Checks if user answered yes or no
    """
    if yes_or_no == "Y":
        main()
    else:
        quit()


def drinks_checker(drinks_number):
    """
    Number of drinks check
    """
    if drinks_number == 0:
        print("No drinks no problem! Well done!")
        check_again = letter_choice(
            "Would you like to calculate again? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
        calculate_again(check_again)


def weight_check():
    """
    Checking if weight is above 0 to avoid divide by 0 error
    """
    while True:
        users_weight = number_validation("Please enter your weight in KG:\n")
        if users_weight < 1:
            print("You weight cannot be 0 or less!")
        elif users_weight > 635:
            print("The heaviest person ever alived had 635kg...")
            print("You should contact Guinness World Records!")
        else:
            break
    return users_weight


def get_drinks():
    """
    Gets number of drinks
    """
    while True:
        users_drinks = number_validation("How many drinks you took?\n")
        if users_drinks < 0:
            print("Number of drinks cannot be negative!")
        else:
            break
    return users_drinks


def get_volume(amount):
    """
    Gets size of the drinks in mililiters
    """
    while True:
        volume_of_drink = number_validation("Number of milliliters per drink?\n")  # noqa E501
        if volume_of_drink < 1:
            print("This value must be above 0!")
        else:
            break
    if amount * volume_of_drink > 5000:
        print("Please remember - drinking so much of any liquid is not healthy...")  # noqa E501
    return volume_of_drink


def get_percentage():
    """
    Gets alcohol content of drinks taken
    """
    while True:
        drinks_percentage = number_validation("How strong they were? Input percentage of alcohol (do not use % sign):\n")  # noqa E501)
        if 0 < drinks_percentage <= 100:
            break
        elif drinks_percentage == 0:
            print("No percentage no problem! Well done!")
            check_again = letter_choice(
            "Would you like to calculate again? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
            calculate_again(check_again)
        else:
            print("This value must be above 0 and less than 100")
    return drinks_percentage


def bac_calculation(user_drinks, user_milliliters, user_percentage, user_weight, the_users_fluid_fraction, user_ingestion):  # noqa E501
    """
    BAC formula calculation
    """
    bac_result = ((FRACTIONOFFLUID * user_drinks * user_milliliters * user_percentage * GRAVITYOFALCOHOL) /  # noqa E501
                  (user_weight * the_users_fluid_fraction * 1000)) - (METABOLISM * user_ingestion)  # noqa E501
    return bac_result


def final_output(user_name, user_licence, user_weight, user_ingestion, the_bac, the_legal_limit):  # noqa E501
    """
    Final output
    """
    sys.stdout.write("CALCULATING")
    sys.stdout.flush()
    slow_print("." * 60)
    time.sleep(1)
    clear()
    print("FINAL BAC CALCULATION:")
    time_stamp = datetime.now()
    print(time_stamp.strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep(0.5)
    print("*" * 80)
    time.sleep(0.5)
    print("*")
    print(f"* Name: {user_name}")

    if user_licence == "F":
        print("* Licence type: Full")
    else:
        print("* Licence type: Provisional")

    print(f"* Weight: {user_weight} kg")
    print(f"* Hours from last drink: {user_ingestion}")
    print(f"* Blood alcohol content: {the_bac.__round__(3)}")
    print(f"* Your legal limit: {the_legal_limit}")

    if the_bac > the_legal_limit:
        print("* Your blood alcohol content is over legal limit! You cannot drive!\n*")  # noqa E501
    else:
        print("* Your blood alcohol content is under legal limit! You can drive!\n*")  # noqa E501

    print("*" * 80)


def main():
    """
    Main function - runs all program functions
    """
    welcome_screen()
    important_notice()
    name = get_name()
    licence = letter_choice(
        "Please enter your licence type (P for provisional and F for full):\n", "P", "F")  # noqa E501
    legal_limit = legal_limit_check(licence)
    gender = letter_choice(
        "Enter your gender (M for male and F for female):\n", "M", "F")
    users_fluid_fraction = fluid_fraction_of_body(gender)
    weight = weight_check()
    drinks = get_drinks()
    drinks_checker(drinks)
    milliliters = get_volume(drinks)
    percentage = get_percentage()
    ingestion = number_validation(
        "How many hours ago you have had a last drink?:\n")
    bac = bac_calculation(drinks, milliliters, percentage,
                          weight, users_fluid_fraction, ingestion)
    final_output(name, licence, weight, ingestion, bac, legal_limit)
    check_again = letter_choice(
        "Would you like to calculate again? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
    calculate_again(check_again)


main()
