# shelf_Assignment

Flak API
The Flask aims to keep the core simple but extensible.

Dependencies

Python  - Programming language
Flask   - The Framework used
Pip     - Dependency Management
RESTful - REST docs


Virtual Environments:

$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ venv\Scripts\activate
$ pip install Flask

Install all project dependencies using:

$pip install -r requirements.txt

Running:

$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ python -m flask run

Running using manager:

python manage.py runserver

Using postman we are sending the inputs in the form of Application-json format
meanwhile --Raw ->Json
After that we already configured both postman and application through the API endpoints
It will receive request of the inputs from postman and sending the response to the postman
If the request data is incorrect it will raise Error otherwise it will send response status with codes..

Contributing:
This API was developed based on:

Flask documentation

REST APIs with Flask and Python