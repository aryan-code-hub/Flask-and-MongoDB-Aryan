# Flask and MongoDB Atlas Assignment
# Project Source Code: https://github.com/aryan-code-hub/Flask-and-MongoDB-Aryan?
## Project Overview

This project is a Flask web application integrated with MongoDB Atlas. It allows users to submit their name and email through a registration form and stores the submitted information in a MongoDB database.

## Technologies Used

* Python
* Flask
* MongoDB Atlas
* PyMongo
* HTML
* JSON
* python-dotenv

## Project Features

1. Flask web application.
2. API endpoint `/api` that returns data in JSON format.
3. Registration form to collect name and email.
4. MongoDB Atlas integration to store submitted data.
5. Success page after successful submission.
6. Error handling for failed submissions.

## Project Structure

Flask_and_MangoDB_Aryan/
├── app.py
├── data.json
├── templates/
│   ├── form.html
│   └── success.html
├── screenshots/
├── README.md
├── Documentation.md
├── requirements.txt
├── .env
├── .gitignore
└── venv/

## How to Run the Project

### 1. Create and activate a virtual environment

python -m venv venv
.\venv\Scripts\Activate.ps1

### 2. Install dependencies

python -m pip install flask pymongo dnspython certifi python-dotenv

### 3. Configure environment variables

Create a `.env` file and add your MongoDB Atlas connection string using the variable `MONGO_URI`.

Do not share or upload your database credentials.

### 4. Start the Flask application

python app.py

### 5. Open the application

Open `http://127.0.0.1:5000` in your browser.

## API Endpoint

* `/api` — Returns JSON data from `data.json`.

## Testing

The Flask application was tested successfully. Form submissions were saved in MongoDB Atlas, and the success page was displayed after submission.

Screenshots of the application, terminal output, and MongoDB data are included in the `screenshots` folder.

## Author

Aryan
