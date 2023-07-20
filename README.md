NFL BET MASTER
--------------
Description 
--------------
Welcome to NFL Bet Master, a Django web app built with Python that allows users to view and bet on Superbowl games! NFL Bet Master provides real-time information on past, current, and upcoming games, allowing users to place bets and view their betting history. This README will guide you through the installation process and explain the features and functionalities of the application.

Getting Started - Installation and runnning the app 
--------------------------------------------------
Getting started prerequisites before running NFL Bet Master, make sure you have the following installed on your system:

Python version 3.11.4 and Django version 4.2.2 

Clone the GitHub repository:
First, you must clone the GitHub repository to your local machine. To do this, open your shell and copy this code : git clone https://github.com/RKcodage/ecf_project.git.

Install dependencies:
Then, enter the project directory and copy this code : pip install -r requirements.txt 

Running the app and start the Django development server:
Enter the following command : python manage.py runserver or python3 manage.py runserver (depending on your Python version installed).

To access the app:
Open your browser and go to http://127.0.0.1:8000/ to access the NFL Bet Master web app. 

App usage 
---------
The Home page displays a brief description of the event and three sections of NFL games like this:
1. Past games :shows a list of recently completed games.
2. Current games : displays games that are currently in progress.
3. Upcoming games : lists games that are yet to start.

The Bets page to access the bets, users must be registered and logged. Once logged in, users can view and place bets on upcoming games. Users can also edit or cancel their existing bets. The bets page shows also three sections: 
1. Past games : displays past games for which users have already placed bets.
2. Current games : shows current games for which users can still place bets.
3. Upcoming games : lists upcoming games available for betting.

User Registration and Activation:
To register as a user, click on the "Register" link at the top-right corner of the page. Fill in the required information, and an activation email will be sent to your registered email address. Click the activation link to activate your account and start placing bets.

Profile page:
Once you're logged, you can access to your Profile to see your personal informations. You have the possibility to updating them by clicking the update button at the bottom. Just below you can show your bets history. 





