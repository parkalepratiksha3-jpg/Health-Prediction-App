# Health Prediction App

## Project Overview
The Health Prediction App is a Python-based application that helps users manage patient health records and generate AI-powered informational remarks.

## Features
- Add new patient records
- View all patient records
- Update patient details
- Delete patient records
- Validate email addresses and dates of birth
- Validate numeric health values
- Generate AI-based health remarks using Google Gemini API
- Store records in an SQLite database

## Technologies Used
- Python
- Streamlit
- SQLite
- Pandas
- Google Gemini API
- Python-dotenv

## Installation and Setup

1. Clone the repository:
   `git clone https://github.com/parkalepratiksha3-jpg/Health-Prediction-App.git`

2. Open the project folder.

3. Install dependencies:
   `python -m pip install -r requirements.txt`

4. Create a `.env` file in the project folder and add your Gemini API key:
   `GEMINI_API_KEY=your_api_key_here`

5. Run the application:
   `python -m streamlit run app.py`

## Disclaimer
AI-generated remarks are for general informational purposes only. They are not medical advice or a diagnosis. Please consult a qualified healthcare professional for medical interpretation.
