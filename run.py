# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("***HI! THIS PROGRAM WILL CHECK YOUR BLOOD ALCOHOL CONTENT!***")

# user inputs:


def get_name():
    """
    Get the name of the user
    """
    name = str(input("Please enter your name: "))
    return name


def get_licence_type():
    """
    Get the correct licence type
    """
    licence = str(input("Please enter your licence type (F for full and P for provisional): "))
    licence = licence.capitalize()

    while licence != ("P" or "F"):
        licence = str(input("Wrong data input. Please use F or P only: "))
        licence = licence.capitalize()

    return licence

name = get_name()
licence = get_licence_type()
gender = input("Please enter your gender (M for male and F for female): ")
weight = float(input("Please enter your weight in KG: "))
drinks = int(input("How many drinks you took? "))
milliliters = int(input("Number of milliliters per drink? "))
percentage = float(input("How strong they were? Input percentage of alcohol: "))
ingestion = int(input("How many hours ago you have had a last drink? (please enter the full hours): "))

# constants:
fractionOfFluid = 0.806
gravityOfAlcohol = 0.79
metabolism = 0.012
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
BAC = ((fractionOfFluid * drinks * milliliters * percentage * gravityOfAlcohol) / \
      (weight * fluidFractionOfBody * 1000)) - (metabolism * ingestion)

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