import os
import pyfiglet

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
    print("***HI! THIS PROGRAM WILL CHECK YOUR BLOOD ALCOHOL CONTENT!***\n")
    input("Press enter to continue...\n")
    clear()


# user inputs:


def get_name():
    """
    Get the name of the user
    """
    input_name = str(input("Please enter your name:\n"))
    return input_name


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


def legal_limit():
    """
    Function defines legal limit of BAC based on licence type
    """
    limit = 0
    if licence == "P":
        limit = 0.02
    elif licence == "F":
        limit = 0.05

    return limit


def fluid_fraction_of_body():
    """
    Function defines fluid fraction of body based on gender
    """
    fluid_fraction_of_body = 0
    if gender == "M":
        fluid_fraction_of_body = 0.58
    elif gender == "F":
        fluid_fraction_of_body = 0.49
    
    return fluid_fraction_of_body


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


def bac_calculation():
    """
    BAC formula calculation
    """
    bac_formula = ((FRACTIONOFFLUID * drinks * milliliters * percentage * GRAVITYOFALCOHOL) / \
        (weight * users_fluid_fraction * 1000)) - (METABOLISM * ingestion)
    return bac_formula


welcome_screen()
name = get_name()
licence = letter_choice("Please enter your licence type (P for provisional and F for full):\n", "P", "F")
legal_limit = legal_limit()
gender = letter_choice("Enter your gender (M for male and F for female):\n", "M", "F")
users_fluid_fraction = fluid_fraction_of_body()
weight = number_validation("Please enter your weight in KG:\n")
drinks = number_validation("How many drinks you took?\n")
milliliters = number_validation("Number of milliliters per drink?\n")
percentage = number_validation("How strong they were? Input percentage of alcohol (do not use % sign):\n")
ingestion = number_validation("How many hours ago you have had a last drink?:\n")
bac = bac_calculation()

# number of drink check
if drinks <= 0:
    print("You are totally sober! Well done!")
else:
    print("Ok, lets see how drunk you are...")

# FINAL OUTPUT

print("*"*22)
print("* FINAL CALCULATION: *")
print("*"*80)
print("Name:", name)
print("Licence type:", licence)
print("Weight:", weight)
print("Hours from last drink:", ingestion)
print("Blood alcohol content:", bac.__round__(3))
print("Your legal limit:", legal_limit)

if bac > legal_limit:
    print("Your blood alcohol content is over legal limit! You cannot drive!")
else:
    print("Your blood alcohol content is under legal limit! You can drive!")
print("*"*80)