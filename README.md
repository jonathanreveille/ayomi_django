## Ayomi Technical Test

In this project :
- Django Framework version 3.2
- Python 3.8
- Bootstrap for html templates
- Oriented Object Programming
- Docker and Docker-compose


The aim of the project is to develop a Django app where :
- a user can create an account
- a user can log himself
- a user can log out
- a user can change his email address from his profile page
- a modal should appear when we click on 'Update information' button


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
- Open your browser and go to : **localhost:8000/**
- Go to localhost:8000 on your favorite browser


#### Environment variables
You need to create a .env file at the root of the project and complete the environment variables that are required in global settings.
You should put your own values for the following environment variables :
* DB_NAME="zzzz"
* DB_USER="yyyy"
* DB_PASS="xxxx"


## Launch with docker-compose for local development
If you use Docker, there is a dockerfile and also a  docker-compose file that
is configured at the root of the project. Make sure you create the database
with your own credentials.

You will need to create a file named 'local_settings.py' in the directory core.
It will help you to have another DATABASE setting for your container, without polluting your django settings.
You should then  add this piece of code to connect your database for your docker-compose :

````python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "ayomi",
        'HOST': 'db',
        'PORT': 5432,
        'USER': "ayomi",
        'PASSWORD': "ayomi"
    }
}
````
Don't forget in the shell of the web container to do : ```python manage.py migrate```
You may now go to : **0.0.0.0:8000/**
