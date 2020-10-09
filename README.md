Welcome to **Gynnie** if you are a **gin lover** :heart_eyes: like myself, and not just the basic stuff, **explore** the variety using this website and make sure to add your **own** to your personal list. :cocktail: You can edit and delete when nesserary.
You can take a look at the live web site here

## Contents
* UX 👍
  * Project Goals
  * Target Audience Goals
  * Site Owner Goals
  * User Stories
  * User Requirements and Expectations
* Design Choices :notebook_with_decorative_cover:
  * Fonts
  * Icons
  * Colours
  * Styling
  * Images :city_sunrise:
  * Backgrounds
* Planning :pencil2:
* Wireframes :wrench:
  * Website Layout
  * Database Design
* Features
  * Current Features
  * Account Creation FlowChart
  * Future Features
  * Data Base Design
* Features
 * Current Features
 * Future Features 
* Technologies Used :computer:
* Planning + Testing: :clipboard:
* Bugs :bug:
* Deployment :rocket:
  * Deploying to Heroku
  * How to locally run the project

## User Experience 👍
## Project Goals:
The goal of this project is to showcase various types of **Gin Cocktails**. The users who access to website will be able to create a list of there own by adding cocktails. This website is aimed for people over the age of 18 only! :underage:

## Target Audience Goals:
* Create an account and build a list to keep track of the all the cocktails they have tested and enjoyed and to add their own.
* To be able to find out information about various gin cocktail beverages.
* A visually appealing, fresh and inviting design.
* An option to send a messege.
* To be able to view the information on the website on Desktop, Tablet and mobile devices with ease.
## Site Owner Goals:
* Generate increased interest for various branded gin/cocktails.
* Recieve messages from the users to interact with.
* Attract different branded beverages to feature on the website.
## User Stories:
**Mike** says: "Im looking for a page that not only works on my computer but also on my phone so that i can access it when im out and about exploring cities."
...**Katie**  says: "I've wanted to find a website that provides me with a list of gin based cocktails and all the info about them, it would be nice to be able to store these drinks on a list of some sort so I can keep track of which ones I've had!"...
...**Billie** says: "When I search for Gin online im often bombarded with marketing promotions and offers, I want a clean elegant website that offers me the information i need when I need it"

## User Requirements and Expectations:
### Requirements:
1. Interact with a visually appealing website.
2. Navigate the website with ease & with fast load times.
3. Extract information on various gin cocktails.
4. Information on the website to be laid out in a clear and effective way.
5. Construct a list of cocktails to try, or to remember.
### Expectations:
1. The website protects the users information.
2. The users can interact with the elements visible on the page.
3. The website loads with sufficient speed.
4. The content on the website renders correctly on desktop, mobile and tablet.
5. The users feel informed and satisfied with the informaton available.
## Design Choices: 🎨
The design of this website had to be colourful and fresh like the many Gin's and cocktails created all over the world. Keeping a summery feel.

### Fonts:
I chose to use the 'Poppins' font for the content on the website, it provides clear layout for the content on the website and easy to read. I really like it.

### Colours:
The colours I chose to use for this website are bright eye catching colours that will potentially increase the interaction levels on the website. You can see these [here](https://github.com/Taitdanielle/Gynnie/blob/master/wireframes/colours.png)


### Images:
The images I have chosen to use on the website were selected to invite people into the website by looking fresh,appeling and bright.

### Background Images:
The background images I have used on the website were also selected to provide an instant context to the web page, the user knows what the theme of the page.

### Wireframes: :wrench:
I designed the wireframes for this project using Balsamic, this software allowed me to easily construct a wireframe for multiple devices, and for all the pages and features I wanted to include on the project. Having these were useful to provide me with a layout of sorts to follow when writing the code for the website, having the design choices initially mapped out helped greatly with the process alltogether.

View the **wireframes** for this project [here](https://github.com/Taitdanielle/Gynnie/tree/master/wireframes).

**Account Creation Flowchart**:
The account creation flowchart allowed me to understand the required logic in order to handle the creation and management of letting users create accounts on the website, this flowchart can be veiwed [here](https://github.com/Taitdanielle/Gynnie/blob/master/wireframes/flowchart/Flowchart-Gynnie.png).

**Database Design:**
Utilising the NoSQL features that MongoDB provides I was able to map out the following collections.

**Data Storage Types:**
The types of data that are stored in the MongoDB database.

* ObjectID
* String
* Boolean
* Object
* Array
* Binary
 
***Cocktail Collection:***

| Title           | Key in Collection | Data Type |
| --------------- |:-----------------:| ---------:|
| drink id        |        _id        |    OjectId |
| Cocktail Name   |   cocktail_name   |    String |
| Description     |    description    |    String |
| Ingredients     |    ingredients    |    String |
| How To          |      how_to       |    String |
| Image           |       image       |    String |
| Cocktail Author |  cocktail_author  |    string |

***User Collection***

| Title    | Key in Collection | Data Type |
| -------- | ----------------- | --------- |
| UserID   | _id               | ObjectID  |
| Username | username          | string    |
| Password | password          | Binary    |

### Features that have been developed:
* Register an account form, Sign-in & Sign-out.
* Users are able to add own cocktail.
* Users are able to edit cocktail they have already added.
* Users are able to remove said cocktail they have added.
* Users are able to create there own list of there own cocktails.

## Future Features::bulb:
* A more advanced product information section, including maps leading users to the closest places where they can taste the cocktails or make their own.
* Favorites option added to cocktails so users can add cocktails from the website to there own lists.
* An option to purchase the products users can see on the website.
* An option for users to subscribe to a e-mailing list to keep up to date with the latest from Gynnie.
* Users to search the range of cocktails with one word.
# Technologies Used: 👨‍💻
## Languages:
HTML
CSS
JavaScript
JSON
Python
## Tools & Libraries:
jQuery
Git
Bootstrap
Font-Awesome
TinyPng (image compression)
MongoDB Atlas
PyMongo
Flask
Jinja
Cloudinary 
# Planning: + Testing: ✏️ 🔌
## Planning:
Planning for this project took a significant amount of a time as to not skip over any detail, when using new languages I would argue that planning is THE most important aspect so that you don't miss something down the line.

## Testing:
This project naturally will need alot of testing due to the scope of the website, therefore my testing plan and documentation had to be very detailed with high levels of scrutiny. Due to the way the website was built I could perform and deploy tests in an organised fashion, page by page, feature by feature.

### Feature Testing 🎡:

**Create an account -**

**Plan 📝:** In order to meet the criteria of the project goals I needed to implement a way in that users on the website could create an account on the website that would then allow them to perform actions that manipulates or creates records within the collections in the MongDB. I needed to research the best ways to handle this feature in terms of making it easy for users to create an account and also properly hash the password when it is stored into the database.

**Implementation 🏭:** Firstly importing session and bcrypt was required in order to efficiently handle the request. The code checks first that the passwords entered match so that the user does not make any typo mistake, after that the code checks to see if the username entered already exists in the database, using flash here to alert the user to any mistakes or issues they encounter when creating an account. Upon passing the prior tests the new user is passed into the users.collection as an object with the ‘name’ field and hashed password thanks to bcrypt. Then the code initiates the ‘session’ for the user signing them in.

**Test 🧪:** To test this feature I had to create a few temporary accounts in order to test that the registration worked as intended, checking what values were passed & stored in the database.

**Result 🏆:** The test passed as the created test user accounts stored in the database with encrypted passwords and the user was signed into session.

**Verdict ✅:** This test has passed based on the above criteria and notes.

**Sign into account -**

**Plan 📝:** I needed to build a page and function that allowed the users to sign in to their account that they made so they can access the information stored in their list, and also have access to view all of the cocktail and information listed on Gynnie.

**Implementation 🏭:** The code checks that the information from the request matches the information that is stored in the users collection, and if it does the session is made with the user, otherwise a flash is triggered letting the user know that there was an in issue with his/hers account details.

**Test 🧪:** To test the sign in feature I first made a test account with username test123 and password test123 and attempted to sign in using this page.

**Result 🏆:** The test passed as the session was made and i was signed into the account ‘test123’ i double checked this by checking the session cookie in dev-tools.

**Verdict ✅:** This test has passed based on the above criteria and Notes.

**Sign out of account -**

**Plan 📝:** There also needed to be a sign-out feature for the users so that they could sign out of their account if they so wished.

**Implementation 🏭:** Creating a route and method for the sign-out functionality was relatively simple, using session.clear clears the active session.

**Test 🧪:** Testing this feature was simple, all i had to do was sign into the previously created account and click the sign-out button in the navigation.

**Result 🏆:** The test passed as the session was cleared out and the user was no longer signed in.

**Verdict ✅:** This test has passed based on the above criteria and notes.

**My Cocktail page -**

**Plan 📝:** I wanted to create a page in which users could view all of the cocktails they, creating a one stop place for them to check if they are out. I needed to make this page access the data of each beer using the objectID store in the favourites array of the current user.

**Implementation 🏭:** To implement this feature i looped over each id in the current users array, and then passed this data to the template where the cocktal in the users array were generated.

**Test 🧪:** Testing this feature was relatively simple, once the objectID was in the array of the current user when they added a cocktail, the cocktaiil should appear on the my list page.

**Result 🏆:** The cocktail appeared on the my cocktail page individually which shows how only the selected objectID was passed into the array of the current user. 

**Verdict ✅:** This test half passed based on the above criteria but Later I came to realise that when a cocktail was being added by a user it was also being added to the all cocktail page. I unfortunetly ran out of time before I could fix this

**Writing, Reading, Updating and Deleting a of a Cocktail -**

**Plan 📝:**  This feature is largely the main focus in terms of demonstrating CRUD functionality that is user facing, I knew I would need to figure out an intuitive way that users could a cocktail of there own and only interact, as in update and delete, the ones that they had made.

**Implementation 🏭:** Once I had setup the cocktails collection with the MongoDB database, I could start to contsruct the relevant code that would allow my users to interact with adding a cocktail, creating 4 routes for each step within the CRUD operation allowed me to neatly structure this feature.

**Test 🧪:** Performing each step of CRUD on the adding cocktail tool and checking the database to see if the changes we're being made correctly.

**Result 🏆:** The intended changes were made and the database was updated accordingly.

**Outcome** :ballot_box_with_check:: This test has passed based on the above criteria and notes.

**All Cocktail page -**

**Plan 📝:** I needed to create a page in which all the cocktails in the cocktail collection could be rendered, this would be done on the all-cocktails page.

**Implementation 🏭:** Implementing this page + feature was relatively simple, I made the connection to the collection on the route and made the data available for the template, then I created a loop using Jinja and each cocktail rendered correctly.

**Test 🧪:** To test if this feature worked i accessed the all-cocktails page and determined whether all the data was rendered correctly.

**Result 🏆:** The data was rendered correctly and all the cocktails in the collection were pulled out.

**Outcome :ballot_box_with_check::** This test has passed based on the above criteria and notes.

# Bugs :bug:

**Bugs During Development:**
During development of this project, I face a few puzzling bugs that proved to be somewhat challenging, being new to Flask, Python etc means that it took me somewhat longer to find soltuions and fixes.

Case Sensitive Confusion:

**Bug :bug::**

The code that handles the creation and and registration of the user accounts on Gynnie captures the inputted data and then transforms that into lowercase to then store into the database, the code that checks to see what current user was in session was throwing errors because it WAS looking for a case sensitive value.

**Fix 🔧:**

Altered the code so that it is no longer case sensitive when determining which user is currently active or in session on the website.

**Outcome :ballot_box_with_check::**

This bug was debugged, dealt with and moved on from.

## Deployment :rocket:
Gynnie:cocktail: was developed on Gitpod, using git and GitHub to host the repository.

Cloning ***Gynnie*** :cocktail: from ***GitHub:***
Ensure you have the following installed:

PIP
Python 3
Git

Make sure you have an account at [MongoDB](https://www.mongodb.com/) in order to construct the database.

***WARNING*** You may need to follow a different guide based on the OS you are using.

1: Clone the **Gynnie:cocktail:** repository by either downloading from here, or if you have Git installed typing the following command into your terminal.
```
git clone https://github.com/Taitdanielle/Gynnie
```
2: Navigate to this folder in your terminal.
3: Enter the following command into your terminal.
```
python3 -m .venv venv
```
4: Initilaize the environment by using the following command.
```
.venv\bin\activate
``` 
5: Install the relevant requirements & dependancies from the requirements.txt file.
```
pip3 -r requirements.txt
```
6: In your IDE now create a file where you can store your SECRET_KEY and your MONGO_URI, follow the schema structure located in data/schemas to properly setup the Mongo Collections. 3
7: Run the application using flask run 
or
```
Python3 app.py in the terminal
```
## Deploying Gynnie :cocktail: to Heroku:
1: Create a requirements.txt file using the following command.
pip3 freeze > requirements.txt
2: Create a Procfile with the following command.
echo web: python3 app.py > Procfile
3: Push these newly created files to your repository.
4: Create a new app for this project on the Heroku Dashboard.
5: Select your deployment method by clicking on the deployment method button and select GitHub.
6: On the dashboard, set the following config variables:
Key	Value
IP	0.0.0.0
PORT	5000
MONGO_URI	mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
SECRET_KEY	"your_secret_key"
7: Click the deploy button on the Heroku dashboard.
8: The site has been deployed the Heroku.

# Credits :credit_card:

* [Igor Basuga](https://github.com/bravoalpha79) For helping me uderstand enviroment variables a lot better
* [Fran](https://github.com/fdeboo) for putting up with my late night meltdowns
* [Coolors](https://coolors.co/)
* Unicorn Revealer
* Student Care
## Disclaimer :loudspeaker:
This website was built for educational purposes only.