# BAC CALCULATOR
The BAC calculator is an easy-to-use tool to check your approximate level of blood alcohol content based on your physical condition and alcohol consumed.

![image](https://user-images.githubusercontent.com/114284732/213199450-c455f8ef-26d0-4abc-abf6-de8cf19893b9.png)

Program in action (please use the full screen for better quality):

https://user-images.githubusercontent.com/114284732/213212675-34349d57-329d-4501-8e51-d8241b100b53.mp4


## Live Site

https://bac-calculator.herokuapp.com/


## Repository

https://github.com/PPindel/bac-calculator


## Author

Przemyslaw Pindel


## Table of Contents
- [BAC CALCULATOR](#bac-calculator)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Author](#author)
  - [Table of Contents](#table-of-contents)
  - [How To Use](#how-to-use)
  - [Features](#features)
  - [Flow Chart](#flow-chart)
  - [Data Model/ Classes](#data-model-classes)
  - [Libraries used](#libraries-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)


## How To Use

At first, the user is asked to input a name and provide details like driving license type, gender, weight, alcohol consumed, and elapsed time since the last drink. Afterward, the program calculates the approximate level of blood alcohol content and compares the result with the legal limit of BAC for the user to determine if the user can legally drive in Ireland. After the calculation is done, the user has the option to save the result in the database and can read the last three entries saved.


## Features

### Implemented features

- Logo in "welcome screen" and "thank you screen" stylized by pyfiglet

![image](https://user-images.githubusercontent.com/114284732/213209929-b8650f3d-2a7d-4213-90da-283f852977e8.png)

- Loading animations to create an illusion of an advanced project and function to clear the terminal so everything looks nice and clear
  (please use the full screen for better quality)

https://user-images.githubusercontent.com/114284732/213211886-7e7a4867-eb4a-429e-898b-91bb016690bd.mp4

- The program has implemented complex input handling to avoid errors and give a user some tips and commentary about the input (sometimes funny :))

![image](https://user-images.githubusercontent.com/114284732/213208625-44227cba-847c-4610-8b77-9efeca083008.png)

- The user has the option to save his result and compare it with the last entries from other users.

![image](https://user-images.githubusercontent.com/114284732/213209186-1c2ac69e-93cf-4372-b988-0d6fdc8c39bb.png)

- Connected excell spreadsheet to store users' data

![image](https://user-images.githubusercontent.com/114284732/213217591-f3419b3e-1b34-43d2-924e-f7a9757593a8.png)

- Data from a spreadsheet formatted with pandas output

![image](https://user-images.githubusercontent.com/114284732/213218674-d77ce3a4-f19b-4a9b-a895-2f84b3f95e1c.png)

### Future Features

The plan for future features is to add an option to select more drinks with different content of alcohol


## Flow Chart

![image](https://user-images.githubusercontent.com/114284732/213254120-cb17d2bc-8dfd-4271-8b58-0700b6960be2.png)


## Data Model/ Classes

![image](https://user-images.githubusercontent.com/114284732/213254500-32fea4b2-8a7c-4cd4-93f7-962d905201f6.png)

![image](https://user-images.githubusercontent.com/114284732/213254552-9918602a-cdc4-4038-ac29-4fb402d8918d.png)


## Libraries used

- os and sys - clear screen function
- pyfiglet - ascii art (BAC Calculator logo)
- datetime - for time and date stamp
- gspread - for google spreadsheets
- colorama - for better ux
- pandas - for better output formatting


## Testing

### Validation Testing

The program was validated at https://pep8ci.herokuapp.com/ and no errors were found.
There were a few lines that were too long so # noqa was added to suppress errors where line breaks would have made the code harder to read.

![image](https://user-images.githubusercontent.com/114284732/213302003-a68cf1d3-120c-4297-b6d3-3f8bf0c3a3d9.png)


### User Testing

My friends helped me a lot with testing BAC Calculator and no bugs or errors were reported. 29 entries was saved in Google spreadsheet (probably half of this was done by myself). I even compared the result given by my program with real breathalyser, and the result was impressively close.

![image](https://user-images.githubusercontent.com/114284732/213537574-a9a7def5-69cd-4eb2-bf21-ca82c4da9496.png)


### Manual Testing

The program is secured by input validation and error catchers to prevent data type issues or calculation problems (for example division by zero error).
- **Disclaimer**
  - user enters a sapace, special characters, numbers, and letters - stay on screen
  - user hits enter button - user goes to the next screen
- **Name Entry**
  - user enters nothing - see Invalid name! Please use letters only! in red and re-prompt
  - user enters full name with space - see red error message and re-prompt
  - user enters any number or special sign - see red error message and re-prompt
  - user enters alpha characters only - goes to next prompt, via animated print out
- **License Type Prompt**
  - user enters unacceptable input: sees "Wrong data - you entered {X}. Please use P or F ONLY!"
  - user enters spaces + lower case f + trailing spaces: user goes to next prompt (the input is formatted by the function)
- **Gender Prompt**
  - the same rules as above are applied to gender selection prompt
  - correct input leads to the next screen
- **Weight Prompt**
  - the program accepts only numerical value between 20 and 635
  - if user enters unacceptable input: sees red error message and re-prompt
  - secret feature: input weight over 635 kg suggests to user contacting Guinness World Records (as the current world record for human is 635 kg)
  - correct input leads to the next screen
- **Drinks Number Prompt**
  - the program accepts only numerical value between 0 and 100
  - if 0 is entered by the user, program ends (as there is nothing to calculate) and user sees appropriate message
  - if user enters unacceptable input: sees red error message and re-prompt
  - correct input leads to the next screen
- **Drinks Volume Prompt**
  - the program accepts only numerical value between 1 and 5000
  - if user enters unacceptable input: sees red error message and re-prompt
  - secret feature: if number of drinks multiplied by volume gives result over 5000 ml, user gets yellow warning: "Please remember - drinking so much of any liquid is not healthy..."
  - correct input leads to the next screen
- **Percentage Prompt**
  - the program accepts only numerical value higher than 0 and the max is 100
  - if user enters unacceptable input: sees red error message and re-prompt
  - correct input leads to the next screen
- **Time prompt**
  - the program accepts only numerical value between 0 and 48
  - if user enters unacceptable input: sees red error message and re-prompt
  - secret feature: input over 48 give yellow message to the user "I really suggest to contact a doctor." (as any intoxication longer than two days might be lethal...)
  - correct input leads to the next screen, via animated print out
- **Final Output**
  - if all inputs were correct, user can see the final calculation with the result
  - as next, user has an option to save the result in database (Y or N - same input validation as in License Prompt)
  - then user can see last 3 results saved in database (Y or N - same input validation as in License Prompt)
  - the last question asks user to calculate again (Y or N - same input validation as in License Prompt)
  - Y restarts the program, N ends the program and the thank you message is displayed

The video below presents the input validation for each step:
(please use the full screen for better quality)

https://user-images.githubusercontent.com/114284732/213303925-504fc490-c510-4396-b75b-2635858560bb.mp4


### Defect Tracking

- problem with division by zero when user entered 0 value as weight - discovered on 10.01.2023 and fixed on 10.01.2023
- too long output in print statement on line 441 - discovered on 18.01.2023 and fixed on 18.01.2023


### Defects of Note

In the beginning a lot of bad users' input were causing problems. The biggest challenge was to create effective tool to prevent the user from inputting bad data and secure the program.


### Outstanding Defects

No outstanding bugs known


# Deployment

## Prerequisites

### Google API

BAC calculator is connected with Google API.

File details:
- Document name:  bac_calculator_data
- Columns A-C row 1: user, bac result, time stamp
- Next rows contains saved results
- Sheet Name: bac

![image](https://user-images.githubusercontent.com/114284732/213544905-a8751909-04bd-419d-8e2b-333088c32fa9.png)

To set this up we need to:

1. install required libraries in our Python environment (pip3 install gspread google-auth) then import downloaded packages and specify the scope
2. create an excell file on our Google account
3. go to Google Cloud Platform
4. select the New Project
5. go to project created, select API & Services from the side menu, and library
6. we must enable 2 APIs - Google Drive and Google Sheets
7. to enable Google Drive API we need to create credentials
8. click Create Credentials
9. from the "Which API are you using?" dropdown menu, choose Google Drive API
10. for the "What data will you be accessing?" question, select Application Data
11. for the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, select No, I'm not using them
12. click Next
13. enter a Service Account name, you can call it anything you like - I will call mine "LoveSandwiches" - then click Create
14. in the Role Dropdown box choose Basic > Editor then press Continue
15. these options can be left blank, click Done
16. on the next page, click on the Service Account that has been created
17. on the next page, click on the Keys tab
18. click on the Add Key dropdown and select Create New Key
19. select JSON and then click Create. This will trigger the json file with your API credentials in it to download to your machine. We must copy this file to our GitPod library and also will need this to deploy our project to Heroku

### Gitpod

1. to run the program in GitPod we need to copy creds.json file:

![image](https://user-images.githubusercontent.com/114284732/213476935-7abc1698-d578-432b-8da8-28388c27e170.png)

2. install all libraries from requirements.txt (pip3 install -r requirements.txt)

![image](https://user-images.githubusercontent.com/114284732/213477292-7ecd8c43-d3ad-4b4a-8091-3b891612afc1.png)

3. run command "python3 run.py" in terminal


### Heroku

1. Fork the repository
   Make a fork so you have a copy of the repository in your own git hub account:
   https://github.com/PPindel/bac-calculator
   Instructions how to fork can be found here:
   https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository

2. Log into Heroku and create new app (the name of the app must be unique):

![image](https://user-images.githubusercontent.com/114284732/213482351-4b89aa2f-5c07-4369-903b-64dba4f3dd95.png)

3.  On the settings tab you have to address two things:
A. **Config Vars**
  Add to vars: CRED and as value cres.json content, and second var PORT and 8000 as value
  
  ![image](https://user-images.githubusercontent.com/114284732/213483562-ba484e7e-e3b0-46d7-b2f2-739b08bd2f0a.png)

B. **Build Packs**
  In build packs add Python and Node JS
  
  ![image](https://user-images.githubusercontent.com/114284732/213483833-2822f9c4-4199-42e3-8a33-9f8322fcb253.png)

4. Deploy tab
A. Connect Heroku app with GitHub and select the correct repository:

![image](https://user-images.githubusercontent.com/114284732/213482680-dc948d5c-36e0-4bc1-869c-7841e70a92d9.png)

B. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/114284732/213485372-9771e133-c2d5-4403-831f-3127bf20dcb2.png)


## Credits

- Art O'Coileain from TU Dublin Tallaght - BAC formula and project idea
- https://www.geeksforgeeks.org/ - how to use pyfiglet and colorama
- https://pypi.org - how to use pandas library
- https://stackoverflow.com/ - code solutions
- https://www.w3schools.com/ - code solutions
- [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
- The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content
 - Code Institute - Love Sandwiches project (Google API connection instructions)


### Acknowledgments

Big thanks to Malia Havlicek - Code Institute mentor for her ideas and support in this project! Also, I would like to thank all my friends for live testing the program!

https://pep8ci.herokuapp.com/ - code validation tool
