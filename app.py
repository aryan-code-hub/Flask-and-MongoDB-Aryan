from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# MongoDB Atlas Connection
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000) if MONGO_URI else None

db = client["studentdb"] if client else None
collection = db["students"] if db is not None else None


# Task 1: JSON API Route
@app.route("/api")
def api():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return jsonify(data)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        return jsonify({"error": str(e)}), 500


# Home Page Form
@app.route("/")
def home():
    return render_template("form.html")


# Task 2: Form Submit and MongoDB Insert
@app.route("/submit", methods=["POST"])
def submit():
    try:
        if collection is None:
            raise RuntimeError("MongoDB connection is not configured.")

        # Check MongoDB connection
        client.admin.command("ping")

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            return render_template(
                "form.html",
                error="Please enter both name and email.",
                name=name,
                email=email
            ), 400

        data = {
            "name": name,
            "email": email
        }

        collection.insert_one(data)

        return redirect(url_for("success"))

    except Exception:
        app.logger.exception("Form submission failed")
        return render_template(
            "form.html",
            error="Data could not be submitted. Please check the MongoDB connection and try again."
        ), 500


# Success Page
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
