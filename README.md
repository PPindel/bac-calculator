# OVERVIEW

This template was made as a guide to ensure you cover assessment criteria in your third milestone write up. It is specific to the **PORTFOLIO 3: Python Essentials** project. It was based off the [battleship readme](https://codeinstitute.s3.amazonaws.com/CSSEssentials/p3-readme.png) with a few additions to help elevate you to possible distinction status.


Sections marked as 🚨**Required**  and 🚀 **merit & beyond**

**Please note** that project assessment criteria changes more often than these guides are updated so double-check the submission criteria before assuming the  🚨**Required**  is all you have to do to pass.

## Helpful tools

### Debugging Your run.py in gitpod
With a single file importing others, gitpod lets you set breakpoints where you then can look at variables and try out syntax.

https://user-images.githubusercontent.com/23039742/212526268-ec02736e-e199-4c63-92b0-96b219f24abc.mp4


### Screenshots and Videos
**Here’s a great video on how to add videos to your readme! no need to convert to gifs!!**

https://www.youtube.com/watch?v=G3Cytlicv8Y

> 1. record a video via slack
> 2. download it
> 3. in github, edit your readme via the pencil icon
> 4. type a place holder word and highlight it
> 5. drag and drop mp4 file over that text
> 6. scroll down to the commit area
> 7. update the default commit message
> 8. click the green button
> 9. ```git pull``` changes to your gitpod workspace

**You can do the steps 3-9 for the image/screenshot uploads too!**

### Cheatsheets and Auto Generation Tools

Markdown's not all that easy so sometimes you may want to use some tools to make tables. 

- [Markdown Cheatsheet](https://guides.github.com/features/mastering-markdown/)
- [markdown table generator](https://www.tablesgenerator.com/markdown_tables) - used to help with documentation table formatting
- [mardown table of contents generator](https://luciopaiva.com/markdown-toc/) - used to create table of contents (be weary it does have some bugs if you have dashes or trailing spaces in your headers)
- [readme.so](https://readme.so/) - if you don't want to learn markdown, this tool might help you

# Table of Contents
🚀 **merit & beyond**

Copy your readme to https://luciopaiva.com/markdown-toc/ to make a table of contents.  This will help assessors to see the structure of your readme. Just test it out ast this tool isn't perfect. It tends to mess up with special characters like dashes.


- [PROJECT NAME](#project-name)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Author](#author)
  - [Table of Contents](#table-of-contents)
  - [How To Play/Use](#how-to-playuse)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Flow Chart](#flow-chart)
  - [Data Model/ Classes](#data-model-classes)
    - [Class X](#class-x)
  - [Libraries used](#libraries-used)
  - [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Manual Testing](#manual-testing)
    - [Defect Tracking](#defect-tracking)
    - [Defects of Note](#defects-of-note)
    - [Outstanding Defects](#outstanding-defects)
    - [Commenting Code](#commenting-code)
  - [Deployment](#deployment)
    - [Requirements](#requirements)
    - [Gitpod](#gitpod)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)
    


====================================== The Sections you Fill in are below ==============================

# BAC CALCULATOR
The BAC calculator is an easy-to-use tool to check your approximate level of blood alcohol content based on your physical condition and alcohol consumed.

![image](https://user-images.githubusercontent.com/114284732/213199450-c455f8ef-26d0-4abc-abf6-de8cf19893b9.png)

Program in action:

https://user-images.githubusercontent.com/114284732/213212675-34349d57-329d-4501-8e51-d8241b100b53.mp4


## Live Site

https://bac-calculator.herokuapp.com/


## Repository

https://github.com/PPindel/bac-calculator


## Author

Przemyslaw Pindel


## Table of Contents
🚀 **merit & beyond**

Generate after readme is complete by copying and pasting your readme from this point & below into this tool:
- [mardown table of contents generator](https://ecotrust-canada.github.io/markdown-toc/)
**NOTE:** It does have some bugs if you have dashes or trailing spaces in your headers


## How To Use

At first, the user is asked to input a name and provide details like driving license type, gender, weight, alcohol consumed, and elapsed time since the last drink. Afterward, the program calculates the approximate level of blood alcohol content and compares the result with the legal limit of BAC for the user to determine if the user can legally drive in Ireland. After the calculation is done, the user has the option to save the result in the database and can read the last three entries saved.


## Features

### Implemented features

- Logo in "welcome screend" and "thank you screen" stylized by pyfiglet

![image](https://user-images.githubusercontent.com/114284732/213209929-b8650f3d-2a7d-4213-90da-283f852977e8.png)

- Loading animations to create an illusion of an advanced project and function to clear the terminal so everything looks nice and clear

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

![image](https://user-images.githubusercontent.com/114284732/213302003-a68cf1d3-120c-4297-b6d3-3f8bf0c3a3d9.png)


### Manual Testing

The program is secured by input validation and error catchers to prevent data type issues or calculation problems (for example division by zero error). The video below presents the input validation for each step:

https://user-images.githubusercontent.com/114284732/213303925-504fc490-c510-4396-b75b-2635858560bb.mp4


### Defect Tracking

- problem with division by zero when user entered 0 value as weight - discovered on 10.01.2023 and fixed on 10.01.2023
- too long output in print statement on line 441 - discovered on 18.01.2023 and fixed on 18.01.2023


### Defects of Note

In the beginning a lot of bad users' input were causing problems. The biggest challenge was to create effective tool to prevent the user from inputting bad data and secure the program.


### Outstanding Defects

No outstanding bugs known


## Deployment

### Requirements

### Google API

BAC calculator is connected with Google API.
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
🚨**Required** 

This section should describe the process you went through to deploy the project to Heroku. Include screenshots if you think they would make the process easier.

You may want to re-watch the [python essentials deployment video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=first) when writing up this section.


If you have project settings required for Heroku, provide a table of the keys and values.
Do not share your personal keys but either cut them out of the screen shot or say <YOUR_VALUE> and include links on how the user would obtain such values.

1. Fork the repository

Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)


2.  New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


3.  Settings
On the settings tab you have to address two things:
A. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


B. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


4. Deploy
A. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

B. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/23039742/132136241-9d76fabb-39f0-4696-bc5f-047398fdaf41.png) 


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


