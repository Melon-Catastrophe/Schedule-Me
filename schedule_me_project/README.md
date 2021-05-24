# Overview

The purpose of writing this code was to learn how to create a web app using Django. Web apps are powerful, and it is about time that I learned how to make one.

[Schedule Me Demo Video](https://youtu.be/LRVAKd8bIfA)

# Web Pages

- First is the home page. If you are not logged in, it will prompt you to log in and provide a link. Once the user is logged in, it will provide a link to the scheduler page.
    - On every page is the navigation bar. Every navigation bar contains links to the Home page and the About Page. If the user is not logged in, Login and Register links will also be displayed. If the user is logged in, Profile and Scheduler links are displayed.
- The About page displays information about the website.
- The Login page displays the necessary form to login.
- The Register page displays the necessary register to login.
- The Profile page will display the user's Username and Email. 
- The Scheduler page dynamically displays the user's schedule that they made. If they click on one of the day headers, then they will be led to a page that contains their schedule for only that day.
- The Create page allows a user to create an event for their schedule.
- The Update page allows a user to update their event.
- The Delete page allows a user to delete their event. 

# Development Environment and Dependencies

The development environment that I used was VSCodium. I used Python and Django to create this web application. I also needed to utilize Bootstrap, HTML, and CSS to get the website displaying properly. 

# Useful Websites

* [Django Official Tutorial](https://docs.djangoproject.com/en/3.2/intro/)
* [Corey Schafer's Django Tutorial](https://youtu.be/UmljXZIypDc)
* [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
* [W3Schools](https://www.w3schools.com/html/)

# Future Work

* I would like to make the visual style of Schedule Me a bit more consistent and make it look just a bit nicer.
* I would love to make it so that the field in the Event model took a time object as an input instead of a set of predetermined choices.