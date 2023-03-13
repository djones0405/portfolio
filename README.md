# myfirstwebapp
web app using Python3, Flask,  Jinja2, htmll


This is a simple Flask app that serves a single web page using the Jinja2 templating engine.
Installation

Before you can run this app, you will need to have Flask installed on your machine. You can install it using pip:

bash

pip install Flask

Usage

To start the app, navigate to the root directory of the project and run the following command:

bash

python app.py

This will start the Flask development server and make the app available at http://localhost:5000/.
Routes

The app has a single route:

    /: Renders the index.html template using Jinja2.

Templates

The app uses a single HTML template, index.html, which is located in the templates directory. This template extends a base template that is also located in the templates directory.
