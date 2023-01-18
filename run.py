# imports:
import os
import pyfiglet
import time
import sys
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from colorama import Fore
from datetime import datetime

# constants:
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("bac_calculator_data")

FRACTIONOFFLUID = 0.806
GRAVITYOFALCOHOL = 0.79
METABOLISM = 0.012


class BAC:
    """
    Data model to track Blood Alcohol Content based on user inputs

    ...

    Attributes
    ----------
    user : str
        name of the user
    license_type : str
        single character representing license type
        P = provisional
        F = full
    limit : decimal
        maximum bac to legally drive in Ireland based on license type
        0.02 for provisional license
        0.05 for full license
    gender : str
        single character representing gender
        M = Male
        F = Female
    fluid_fraction_of_user : decimal
        fluid fraction of body based on gender type
        Male = 0.58
        Female = 0.49
    weight : decimal
        decimal representing weight in KG
        20 - 635
    users_drinks : decimal
        number of drinks consumed by the user
        0 - 100
    volume_of_drink : decimal
        volume per single drink in ml
        1 - 5000
    drinks_percentage : decimal
        alcoholic content of drinks
        0 - 100
    users_hours : decimal
        hours since the last drink was consumed
        0- 48
    bac_result : decimal
        calculated BAC based on user input
    time_stamp : datetime
        time of data collection

    Methods
    -------
    legal_limit_check()
        defines the legal limit of bac for the user
    fluid_fraction_of_body()
        defines the fluid fraction of user's body
    weight_check()
        validates the weight of the user
    get_drinks()
        validates amount of drinks comsumed by the user
    get_volume()
        validates the volume of alcohol consumed by the user
    get_percentage()
        validates the alcoholic content of drinks
    get_hours()
        validates time since last drink consumed
    bac_calculation()
        calculates the bac of the user
    final_output()
        prints calculations and user's data
    """

    def __init__(self, user, license_type, gender):
        self.user = user
        self.license_type = license_type
        self.limit = 0
        self.gender = gender
        self.fluid_fraction_of_user = 0
        self.weight = 0
        self.users_drinks = 0
        self.volume_of_drink = 0
        self.drinks_percentage = 0
        self.users_hours = 0
        self.bac_result = 0
        self.time_stamp = 0

    def legal_limit_check(self):
        """
        Function defines the legal limit of BAC based on the license type
        """
        if self.license_type == "P":
            self.limit = 0.02
        elif self.license_type == "F":
            self.limit = 0.05

    def fluid_fraction_of_body(self):
        """
        Function defines the fluid fraction of the body based on gender
        """
        if self.gender == "M":
            self.fluid_fraction_of_user = 0.58
        elif self.gender == "F":
            self.fluid_fraction_of_user = 0.49

    def weight_check(self):
        """
        Checking if the weight is above 0 to avoid the divide by 0 error
        """
        while True:
            self.weight = number_validation("Please enter your weight in KG:\n")  # noqa E501
            if self.weight < 20:
                print(Fore.RED + "Your weight must be at least 20kg to proceed." + Fore.WHITE)  # noqa E501
            elif self.weight > 635:
                print(Fore.RED + "The heaviest person ever lived had 635kg..." + Fore.WHITE)  # noqa E501
                print(Fore.YELLOW + "You should contact the Guinness World Records!" + Fore.WHITE)  # noqa E501
            else:
                break

    def get_drinks(self):
        """
        Gets the number of drinks
        """
        while True:
            self.users_drinks = number_validation("How many drinks did you take?\n")  # noqa E501
            if self.users_drinks == 0:
                print(Fore.GREEN + "No drinks no problem! Well done!" + Fore.WHITE)  # noqa E501
                check_again = letter_choice(
                    "Would you like to calculate again? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
                calculate_again(check_again)
            elif self.users_drinks < 0:
                print(Fore.RED + "The number of drinks cannot be negative!" + Fore.WHITE)  # noqa E501
            elif self.users_drinks > 100:
                print(Fore.RED + "Sorry, that's way too much to calculate." + Fore.WHITE)  # noqa E501
            else:
                break
        if self.users_drinks > 50:
            print(Fore.YELLOW + "That's quite a lot..." + Fore.WHITE)

    def get_volume(self):
        """
        Gets the size of the drinks in mililiters
        """
        while True:
            self.volume_of_drink = number_validation("A number of milliliters per drink?\n")  # noqa E501
            if self.volume_of_drink < 1:
                print(Fore.RED + "Sorry, 1ml is the minimum value to start the calculation." + Fore.WHITE)  # noqa E501
            elif self.volume_of_drink > 5000:
                print(Fore.RED + "Sorry, that's way too much to calculate." + Fore.WHITE)  # noqa E501
            else:
                break
        if self.users_drinks * self.volume_of_drink > 5000:
            print(Fore.YELLOW + "Please remember - drinking so much of any liquid is not healthy..." + Fore.WHITE)  # noqa E501

    def get_percentage(self):
        """
        Gets alcohol content of drinks taken
        """
        while True:
            self.drinks_percentage = number_validation("How strong they were? Input percentage of alcohol (do not use % sign):\n")  # noqa E501)
            if 0 < self.drinks_percentage <= 100:
                break
            elif self.drinks_percentage == 0:
                print(Fore.GREEN + "No percentage no problem! Well done!" + Fore.WHITE)  # noqa E501)
            if 0 < self.drinks_percentage <= 100:
                check_again = letter_choice(
                "Would you like to calculate again? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
                calculate_again(check_again)
            else:
                print(Fore.RED + "This value must be above 0 and less than 100" + Fore.WHITE)  # noqa E501

    def get_hours(self):
        """
        Gets number of hours since last drink was consumed
        """
        while True:
            self.users_hours = number_validation("How many hours ago you have had a last drink?:\n")  # noqa E501
            if self.users_hours < 0:
                print(Fore.RED + "I can't allocate the negative value on a timeline..." + Fore.WHITE)  # noqa E501
            elif self.users_hours > 48:
                print(Fore.RED + "If you still feel the effects of intoxication after 2 days..." + Fore.WHITE)  # noqa E501
                print(Fore.YELLOW + "I really suggest to contact a doctor." + Fore.WHITE)  # noqa E501
            else:
                break

    def bac_calculation(self):
        """
        BAC formula calculation
        """
        self.bac_result = ((FRACTIONOFFLUID * self.users_drinks * self.volume_of_drink * self.drinks_percentage * GRAVITYOFALCOHOL) /  # noqa E501
                    (self.weight * self.fluid_fraction_of_user * 1000)) - (METABOLISM * self.users_hours)  # noqa E501

        if self.bac_result < 0:
            self.bac_result = 0

    def final_output(self):
        """
        Final output
        """
        sys.stdout.write("CALCULATING")
        sys.stdout.flush()
        slow_print("." * 60)
        time.sleep(1)
        clear()
        print(Fore.YELLOW + "FINAL BAC CALCULATION:" + Fore.WHITE)
        self.time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(Fore.GREEN + self.time_stamp + Fore.WHITE)  # noqa E501
        time.sleep(0.5)
        print(Fore.BLUE + "*" * 80 + Fore.WHITE)
        time.sleep(0.5)
        print(f"* Name: {self.user}")

        if self.license_type == "F":
            print("* License type: Full")
        else:
            print("* License type: Provisional")

        print(f"* Weight: {self.weight.__round__(3)} kg")
        print(f"* Consumed {((self.users_drinks * self.volume_of_drink) / 1000).__round__(3)} litre of {self.drinks_percentage.__round__(3)}% alcohol")  # noqa E501
        print(f"* Hours from last drink: {self.users_hours.__round__(3)}")
        print(f"* Blood alcohol content: {self.bac_result.__round__(3)}")

        if self.bac_result > 0.4:
            print(Fore.RED + "BAC VALUE OVER 0.4 IS POTENTIALLY FATAL!!!" + Fore.WHITE)  # noqa E501

        print(f"* Your legal limit: {self.limit}")

        if self.bac_result > self.limit:
            print("* " + Fore.RED + "Your blood alcohol content is over the legal limit! You cannot drive!" + Fore.WHITE)  # noqa E501
        else:
            print("* " + Fore.GREEN + "Your blood alcohol content is under the legal limit! You can drive!" + Fore.WHITE)  # noqa E501

        print(Fore.BLUE + "*" * 80 + Fore.WHITE)


def clear():
    """
    Clear screen function
    """
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text):
    """
    Slow printing text function
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.02)


def welcome_screen():
    """
    The first function in the program which welcomes the user
    """
    clear()
    print(Fore.LIGHTCYAN_EX)
    print(pyfiglet.figlet_format("B A C\nCALCULATOR"))
    time.sleep(1)
    print(Fore.GREEN + "***HI! THIS PROGRAM WILL CHECK YOUR BLOOD ALCOHOL CONTENT!***\n" + Fore.WHITE)  # noqa E501
    print("***AND ANSWER THE QUESTION - CAN YOU LEGALLY DRIVE IN IRELAND?***\n")  # noqa E501
    print(Fore.LIGHTRED_EX + "***BASED ON YOUR DRIVING LICENSE TYPE***\n")  # noqa E501
    sys.stdout.write(Fore.YELLOW + "LOADING THE PROGRAM")
    sys.stdout.flush()
    slow_print("..........................................." + Fore.WHITE)
    time.sleep(3)
    clear()


def thank_you():
    """
    The function thanks user for using the program
    """
    clear()
    print(Fore.LIGHTCYAN_EX)
    print(pyfiglet.figlet_format("B A C\nCALCULATOR"))
    print(Fore.YELLOW)
    slow_print("THANK YOU FOR USING BAC CALCULATOR!\n")
    slow_print("COME BACK AGAIN!\n\n\n")
    print(Fore.LIGHTRED_EX + "Click the orange button above the terminal to restart the program." + Fore.WHITE)  # noqa E501


def important_notice():
    """
    Notice for user
    """
    clear()
    print(Fore.RED + "IMPORTANT NOTICE!" + Fore.YELLOW)
    print("\nThis program is not accurate enough to calculate the exact blood alcohol")  # noqa E501
    print("content in your body. The obtained result is averaged and does not take")  # noqa E501
    print("into account many individual preferences.\n")
    print("Also, please remember that the best practice is to never drink and drive.\n" + Fore.GREEN)  # noqa E501
    input("Press enter to continue..." + Fore.WHITE)
    clear()


def two_options_validation(a, b, user_choice):
    """
    The function is checking if the user has selected the correct option
    """
    try:
        user_choice = user_choice.capitalize()
        if user_choice != a and user_choice != b:
            raise ValueError(
                Fore.RED + f"Wrong data - you entered {user_choice}. Please use {a} or {b} ONLY!" + Fore.WHITE  # noqa E501
            )
    except ValueError as e:
        print(f"ERROR {e}")
        return False

    return True


def get_name():
    """
    Get the name of the user
    """
    while True:
        input_name = str(input("Please enter your name (use only letters, no spaces between):\n"))  # noqa E501
        input_name = input_name.strip()
        if len(input_name) > 20:
            print(Fore.RED + "Sorry, your name is too long. Please use any other name up to 20 letters." + Fore.WHITE)  # noqa E501
        else:
            break

    while not input_name.isalpha():
        print(Fore.RED + "Invalid name! Please use letters only!" + Fore.WHITE)
        input_name = str(input("Please enter your name (use only letters, no spaces between):\n"))  # noqa E501
        input_name = input_name.strip()

    clear()
    input_name = input_name.capitalize()
    hello = f"Hi {input_name}, I need to ask you few questions to calculate your BAC.\n"  # noqa E501
    slow_print(hello)
    return input_name


def letter_choice(message_to_display, first_option, second_option):
    """
    Get the correct alfabetical value from the user
    (License type and gender type in this program so far...)
    """
    while True:
        users_letter = input(message_to_display)
        users_letter = users_letter.strip()
        if two_options_validation(first_option, second_option, users_letter):
            break

    users_letter = users_letter.capitalize()
    return users_letter


def number_validation(message_for_user):
    """
    Get the amount of the drinks taken
    """
    while True:
        try:
            users_number = float((input(message_for_user)))
            break
        except ValueError:
            print(Fore.RED + "Invalid value! Please use numbers only!" + Fore.WHITE)  # noqa E501
    users_number = users_number.__round__(3)
    return users_number


def calculate_again(yes_or_no):
    """
    Checks if the user answered yes or no
    """
    if yes_or_no == "Y":
        main()
    else:
        thank_you()
        quit()


def update_worksheet(data, worksheet):
    """
    Receives a list of values to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(Fore.YELLOW + "Adding your result to the records...")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(Fore. GREEN + "Updated successfully" + Fore.WHITE)


def main():
    """
    Main function - runs all program functions
    """
    welcome_screen()
    important_notice()
    name = get_name()
    the_license = letter_choice(
        "Please enter your license type (P for provisional and F for full):\n", "P", "F")  # noqa E501
    selected_gender = letter_choice(
        "Enter your gender (M for male and F for female):\n", "M", "F")

    bac_user = BAC(name, the_license, selected_gender)
    bac_user.legal_limit_check()
    bac_user.fluid_fraction_of_body()
    bac_user.weight_check()
    bac_user.get_drinks()
    bac_user.get_volume()
    bac_user.get_percentage()
    bac_user.get_hours()
    bac_user.bac_calculation()
    bac_user.final_output()

    save_the_result = letter_choice("Do you wish to save your result in our database? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
    if save_the_result == "Y":
        the_result = [bac_user.user, bac_user.bac_result.__round__(3), bac_user.time_stamp]  # noqa E501
        update_worksheet(the_result, "bac")

    view_results = letter_choice("\nWould you like to check the last 3 saved results? Type Y for yes or N for no: ", "Y", "N")  # noqa E501
    if view_results == "Y":
        records = SHEET.worksheet("bac").get_all_values()
        df = pd.DataFrame(
            {
                "Name": [
                    records[-3][0],
                    records[-2][0],
                    records[-1][0]
                ],
                "BAC": [
                    records[-3][1],
                    records[-2][1],
                    records[-1][1]
                ],
                "Date and time": [
                    records[-3][2],
                    records[-2][2],
                    records[-1][2]
                ]
            }
        )
        print(Fore.LIGHTBLUE_EX)
        print(df)
        print(Fore.WHITE)

    check_again = letter_choice(
        "Would you like to calculate again? Enter Y for yes or N for no: ", "Y", "N")  # noqa E501
    calculate_again(check_again)


main()
