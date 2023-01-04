# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os


def clear():
    """
    Clear screen function
    """
    os.system("cls" if os.name == "nt" else "clear")


print("***HI! THIS PROGRAM WILL CHECK YOUR BLOOD ALCOHOL CONTENT!***\n")
input("Press enter to continue...")
clear()

# user inputs:


def get_name():
    """
    Get the name of the user
    """
    name = str(input("Please enter your name: "))
    return name


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
        licence = input("Please enter your licence type (P for provisional and F for full): ")
        if two_options_validation("P", "F", licence):
            break
        
    licence = licence.capitalize()
    return licence


def get_gender_type():
    """
    Get the gender type of user
    """
    while True:
        gender = input("Please enter your gender (M for male and F for female): ")
        if two_options_validation("M", "F", gender):
            break

    gender = gender.capitalize()
    return gender


name = get_name()
licence = get_licence_type()
gender = get_gender_type()
weight = float(input("Please enter your weight in KG: "))
drinks = int(input("How many drinks you took? "))
milliliters = int(input("Number of milliliters per drink? "))
percentage = float(input("How strong they were? Input percentage of alcohol: "))
ingestion = int(input("How many hours ago you have had a last drink? (please enter the full hours): "))

# constants:
FRACTIONOFFLUID = 0.806
GRAVITYOFALCOHOL = 0.79
METABOLISM = 0.012

# variables
fluidFractionOfBody = 0
legalLimit = 0

# a gender check:
if gender == "M":
    fluidFractionOfBody = 0.58
elif gender == "F":
    fluidFractionOfBody = 0.49
else:
    print("ERROR! WRONG GENDER!")

# BAC formula calculation
BAC = ((FRACTIONOFFLUID * drinks * milliliters * percentage * GRAVITYOFALCOHOL) / \
      (weight * fluidFractionOfBody * 1000)) - (METABOLISM * ingestion)

# number of drink check
if drinks <= 0:
    print("You are totally sober! Well done!")
else:
    print("Ok, lets see how drunk you are...")

# legal limit check
if licence == "P":
    legalLimit = 0.02
elif licence == "F":
    legalLimit = 0.05
else:
    print("ERROR! WRONG TYPE OF LICENCE!")

# FINAL OUTPUT

print("*"*22)
print("* FINAL CALCULATION: *")
print("*"*65)
print("Name:", name)
print("Licence type:", licence)
print("Weight:",weight)
print("Hours from last drink:",ingestion)
print("Blood alcohol content:", BAC.__round__(3))
print("Your legal limit:", legalLimit)

if BAC > legalLimit:
    print("Your blood alcohol content is over legal limit! You cannot drive!")
else:
    print("Your blood alcohol content is under legal limit! You can drive!")
print("*"*65)