import os
import pyfiglet


def clear():
    """
    Clear screen function
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_screen():
    clear()
    print(pyfiglet.figlet_format("B A C\nCALCULATOR"))
    print("***HI! THIS PROGRAM WILL CHECK YOUR BLOOD ALCOHOL CONTENT!***\n")
    input("Press enter to continue...")
    clear()


# user inputs:


def get_name():
    """
    Get the name of the user
    """
    input_name = str(input("Please enter your name: "))
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


def get_licence_type():
    """
    Get the correct licence type
    """
    while True:
        input_licence = input("Please enter your licence type (P for provisional and F for full): ")
        if two_options_validation("P", "F", input_licence):
            break
        
    input_licence = input_licence.capitalize()
    return input_licence


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


def get_gender_type():
    """
    Get the gender type of user
    """
    while True:
        input_gender = input("Enter your gender (M for male and F for female): ")
        if two_options_validation("M", "F", input_gender):
            break

    input_gender = input_gender.capitalize()
    return input_gender


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


welcome_screen()
name = get_name()
licence = get_licence_type()
legal_limit = legal_limit()
gender = get_gender_type()
fluid_fraction = fluid_fraction_of_body()
weight = float(input("Please enter your weight in KG: "))
drinks = int(input("How many drinks you took? "))
milliliters = int(input("Number of milliliters per drink? "))
percentage = float(input("How strong they were? Input percentage of alcohol: "))
ingestion = int(input("How many hours ago you have had a last drink? (please enter the full hours): "))

# constants:
FRACTIONOFFLUID = 0.806
GRAVITYOFALCOHOL = 0.79
METABOLISM = 0.012

# BAC formula calculation
BAC = ((FRACTIONOFFLUID * drinks * milliliters * percentage * GRAVITYOFALCOHOL) / \
      (weight * fluid_fraction * 1000)) - (METABOLISM * ingestion)

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
print("Blood alcohol content:", BAC.__round__(3))
print("Your legal limit:", legal_limit)

if BAC > legal_limit:
    print("Your blood alcohol content is over legal limit! You cannot drive!")
else:
    print("Your blood alcohol content is under legal limit! You can drive!")
print("*"*80)