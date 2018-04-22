# Ecommerce | Coffee Daily | Project 3 - Full Stack Web Development | Code Institute, Dublin Ireland, January-April 2018

## Overview

### General information
This is Dan Dumitrache's third project for Code Institure bootcamp, Dublin, Ireland January-April 2018. It is a fully functional ecommerce application written in Python and Django as a framework. 

Git repository can be seen at (https://github.com/saigonro/project3-stream3). Live version can be seen at (https://project3-stream3.herokuapp.com/).

### Navigation through the website
The website has two menus, one related to the user account and the shopping cart, and another one for navigating through the website pages.

### Technologies used
This website was created using the following technologies:
- HTML
- CSS + Bootstrap(v4.0) (http://getbootstrap.com/) for styling
- JavaScript (Bootstrap core JavaScript)
- jQuery (Bootstrap requirement) (https://jquery.com/)
- PostgreSQL Database (https://www.postgresql.org/)
- Django (https://www.djangoproject.com/)
- Pillow | Python Imaging Library
- Boto | Python Interface to Amazon Web Services
- Git & GitHub for version control
- Wireframes in PDF format created with Balsamiq (https://balsamiq.com/)
- Stripe | Online Payments (https://stripe.com/ie)
- AWS S3 for handling the static files
- Heroku for hosting the project's files
- See more technologies used for this application in the requirements.txt file

### Features
- Responsive (mobile first) layout
- The data is stored in a PostgreSQL database
- The project uses Django framework
- Existing users can login/logout
- New users can register
- A user has to be registered in order to buy a product
- Payments are handled by Stripe
- "View cart page" where the user can remove items from the cart
- Users can contact the website administrator via a contact form on the Contact page
- Google map integration on the contact page shows the exact location of the business
- Logged in users can review and rate a product

### Remaining Features to be Implemented
- Additional unittest tests to ensure a higher coverage

### Testing
- Tests written in unittest test framework
- All code used on the site has been tested to ensure everything is working as expected
- Site viewed and tested in the following browsers: Google Chrome, Opera, Microsoft Edge, Mozilla Firefox, and mobile browsers

### Viewing the code locally
To view this website locally you have to download the entire repository on your machine, install all the necesary dependencies listed in the requirements.txt file, and run the command `python3 manage.py runserver` in the terminal.

### Media and Icons
The project makes use of images for each product sold through the website. These images were downloaded from the internet. The images were edited to ensure they have the same aspect ratio using Adobe Photoshop CS5 and GIMP Image Manipulation software. All of the images were compressed and saved for web use.

The website's logo has been created by the author of this repository using Adobe Illustrator CS5 and it can be viewed at: (https://github.com/saigonro/project3-stream3/blob/master/home/static/home/images/logo3.png)

### Colours
The website uses the following colour pallette:
- #6E7587 for background of the HTML page and hover links
- #806641 for text colour, links colour and buttons background
- #AE956D for background of the `container` and `card` classes 

### Wireframes
The wireframes for this project are located in the wireframe folder in the root of the project. They were created using Balsamiq software and are saved in PDF format.
