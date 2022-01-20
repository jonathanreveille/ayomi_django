## Ayomi Technical Test

In this project :
- Django Framework version 3.2
- Python 3.8
- Oriented Object Programming
- Docker

The aim of the project is to develop a Django app where :
- a user can log himself
- can change his personal data
- can change his email adress without the page reloading
- ...

#### To start the project locally : (TO COMPLETE LATER)

Activate virtual environment
Create your virtual env (Windows Machine):
- ```py -m venv env --system-site-packages```
- ```env\Scripts\Activate```
- ```pip install -r requirements.txt```

## Launch the project locally
- ```cd src/```
- ```python manage.py makemigrations ```
- ```python manage.py migrate ```
- ```python manage.py runserver```
- Go to localhost:8000 on your favorite browser

#### Tests
All the tests are under the directory tests of the project
1) To start the test : pytest
2) To have coverage with missing lines : coverage report -m

## Launch with docker-compose for local development
If you use Docker and containers, there is a docker-compose file that
is configured at the root of the project. Make sure you create the database
with your own credentials.

#### Important
You need to create a .env file at the root of the project and complete the environment variables that are required in global settings
