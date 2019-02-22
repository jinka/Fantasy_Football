# Football-Notifier.com

# Table of contents
***
* [General Info](#General-Info)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Behaviour Driven Technologies](#Behaviour-Driven-Technologies)
* [Support](#Support)
* [Bugs](#Bugs)
* [Creator](#Creator)
* [License](#License)

## General info
---
Football-Notifier as the name sugests is a website which gives notifications on football updates to the user. A user is able to select their football intrests and recieve their desired updates through SMS and Email service.  

The application allows the user to:

* Sign in to the WebApp.

* Select their desired Football Intrests.

* Receive a email notification depending on their intrests.

* Receive a SMS notification depending on their intrests.


## Technologies
---
Project is created with:
* Python 3.6
* Prerequisites:   *Pip *SQLAlchemy *Bootstrap
* Flask
* HTML, CSS

## Setup
---
To run this project, please follow the following instructions.
-   Get access to the internet
-   Sign into your github pages. Set up would require access to github pages; the webpage uses an index file linked on github pages. This would require membership and access to the **jinka** repository.
-   Search for derriqo on the github pages and select the Football-Notifier repository.
-   Clone the repository.

### Cloning
---
* In your terminal:
        
        $ git clone https://github.com/jinka/Football-Notifier
        $ cd Football-Notifier

## Running the Application
---
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
---
* To run the tests for the application file:

        $ python3.6 manage.py test
        
## Behaviour Driven Development
---

**User Story**
As a user i want to be able to select desired football intrests, receive email and sms notifications .

| Input | Output | Behaviour |
| :---------------- | :---------------: | :--------------: |
|User Logs in or signs up  | Login and User Form displays  | Displays the Landing page a menu bar  |
|  | Welcome message is Sent to New User | New User Receives Email |
|| User Receives SMS notification depending on Intrest | User receives updates |
| User Signs out | User is directed back to Landing page |Leave Application |


## Support and contact details
---
For any inquiries, please reach out to 

## Bugs
---
None at the moment, but would love to hear your feedback!

## Creators
---

Created by **Dayud Muhamed Farah, Albert Carlos Omware, Derrick William and Anum Asif**. 
