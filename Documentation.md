# Flask and MongoDB Atlas Assignment Documentation

## 1. Objective

The objective of this assignment is to build a Flask web application that provides a JSON API and stores registration details in MongoDB Atlas.

## 2. Tools and Technologies

* Python 3.13
* Flask
* MongoDB Atlas
* PyMongo
* HTML
* JSON
* VS Code
* PowerShell

## 3. Project Features

* Flask web application with a registration form.
* `/api` endpoint that returns JSON data from `data.json`.
* Form submission with name and email fields.
* MongoDB Atlas integration for storing submitted details.
* Success page displayed after successful submission.

## 4. Setup and Execution

### Step 1: Create a virtual environment

```powershell
python -m venv venv

### Step 2: Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1

### Step 3: Install project dependencies

```powershell
python -m pip install -r requirements.txt

### Step 4: Configure MongoDB Atlas

Create a `.env` file in the project root and configure the `MONGO_URI` environment variable with the MongoDB Atlas connection string.

**Security:** Do not include the actual connection string, password, or other credentials in documentation or screenshots.

### Step 5: Start the application

```powershell
python app.py

### Step 6: Open the application

Open the following address in a browser:

`http://127.0.0.1:5000`

## 5. API Endpoint

* **Endpoint:** `/api`
* **Purpose:** Returns the data defined in `data.json` in JSON format.

## 6. Testing and Results

* Verified that the MongoDB Atlas connection responds successfully.
* Submitted registration details through the web form.
* Verified that the success page is displayed after submission.
* Verified that submitted data appears in MongoDB Atlas.

## 7. Screenshots

The `screenshots` folder contains screenshots of the Flask server, registration form, successful submission, and saved MongoDB data.

## 8. Conclusion

The Flask application was successfully connected to MongoDB Atlas. Registration details were submitted through the web form and verified in the database.