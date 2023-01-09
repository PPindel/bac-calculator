# imports:
import os
import pyfiglet
import sys, time

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
    print("***AND ANSWER THE QUESTION - CAN YOU LEGALLY DRIVE?***")
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
    print("This program is not accurate enough to calculate the exact blood alcohol")
    print("content in your body. The obtained result is averaged and does not take")
    print("into account many individual preferences.\n")
    print("Also, please remember that the best practice is to never drink and drive.\n")
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
                f"Wrong data - you entered {user_choice}. Please use {a} or {b} ONLY!"
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
    input_name = str(input("Please enter your name:\n"))
    clear()
    hello = f"Hi {input_name}, I need to ask you few questions to calculate your BAC...\n"
    slow_print(hello)
    return input_name


def letter_choice(message_to_display, first_option, second_option):
    """
    Get the correct alfabetical value from user
    (Licence type and gender type in this program so far...)
    """
    while True:
        users_letter = input(message_to_display)
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


def drinks_checker(drinks_number):
    """
    Number of drinks check
    """
    if drinks_number <= 0:
        print("You are totally sober! Well done!")
        quit()


def bac_calculation(user_drinks, user_milliliters, user_percentage, user_weight, the_users_fluid_fraction, user_ingestion):
    """
    BAC formula calculation
    """
    bac_result = ((FRACTIONOFFLUID * user_drinks * user_milliliters * user_percentage * GRAVITYOFALCOHOL) / \
        (user_weight * the_users_fluid_fraction * 1000)) - (METABOLISM * user_ingestion)
    return bac_result


def final_output(user_name, user_licence, user_weight, user_ingestion, the_bac, the_legal_limit):
    """
    Final output
    """
    sys.stdout.write("CALCULATING")
    sys.stdout.flush()
    slow_print("." * 60)
    time.sleep(1)
    clear()
    print("FINAL BAC CALCULATION:")
    time.sleep(0.5)
    print("*" * 80)
    time.sleep(0.5)
    print("* Name:", user_name)
    print("* Licence type:", user_licence)
    print("* Weight:", user_weight)
    print("* Hours from last drink:", user_ingestion)
    print("* Blood alcohol content:", the_bac.__round__(3))
    print("* Your legal limit:", the_legal_limit)

    if the_bac > the_legal_limit:
        print("* Your blood alcohol content is over legal limit! You cannot drive!")
    else:
        print("* Your blood alcohol content is under legal limit! You can drive!")

    print("*" * 80)


def main():
    """
    Main function - runs all program functions
    """
    welcome_screen()
    important_notice()
    name = get_name()
    licence = letter_choice("Please enter your licence type (P for provisional and F for full):\n", "P", "F")
    legal_limit = legal_limit_check(licence)
    gender = letter_choice("Enter your gender (M for male and F for female):\n", "M", "F")
    users_fluid_fraction = fluid_fraction_of_body(gender)
    weight = number_validation("Please enter your weight in KG (do not worry, we don't store this data):\n")
    drinks = number_validation("How many drinks you took?\n")
    drinks_checker(drinks)
    milliliters = number_validation("Number of milliliters per drink?\n")
    percentage = number_validation("How strong they were? Input percentage of alcohol (do not use % sign):\n")
    ingestion = number_validation("How many hours ago you have had a last drink?:\n")
    bac = bac_calculation(drinks, milliliters, percentage, weight, users_fluid_fraction, ingestion)
    final_output(name, licence, weight, ingestion, bac, legal_limit)


main()
