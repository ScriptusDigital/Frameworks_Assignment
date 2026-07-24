# ProjectPilot
## Project Description
ProjectPilot is a Djando-based project management web application designed to help individuals and teams organise projects, maintain project information and communicated through an internal messaging system. 

Users cn register an account, maintain a personal profile, create and categorise projects, exhange messages with other users and monitor activity through a central dashboard. 

The project demonstrates core Django ideas including:
- PostgreSQL database integration
- Django models and migrations
- Authentication and password hashing
- Role-based authorization
- Function-based and class-based views
- CRUD operations 
- Django forms and validation
- Template inheritance
- Responsive Bootstrap styling and layout
- JavaScript form behaviour
- Email-based password recovery mechanism
- Automated testing with Django 'TestCase'

## Features

### User registration and authentication
Users can register with a username, email address and password. Passwords are securely hashed using Django's built-in authentication system rather than being stored as plain text. Users can log in and out, while protected views redirect unauthenticated visitors to the login page. 

### Project management funtion
Users can create, view, edit and delete projects. Each project stores
- Project name
- Description
- State data
- End date/Deadline
- Status
- Category
- Stakeholders
- Owner
- Creation date 

Form validation prohibits a project deadline from being set before the start date. 