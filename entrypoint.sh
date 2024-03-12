#!/bin/bash

# Perform any necessary setup tasks here

# Sleep for a while to allow time for the database to start up
sleep 10

# Perform database migrations
flask db migrate
flask db upgrade 

# Start your Flask application
python3 app.py
