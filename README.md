# 🏠 Match My Mansion 🌟

## Overview

**"Match My Mansion"** is a web application designed to assist users in finding and predicting property prices. It features property listings, price predictions, and personalized recommendations using advanced machine learning techniques. Built with **Flask** for the back-end, **HTML** and **Tailwind CSS** for the front-end, and utilizing a **Random Forest** model for price prediction, this app also integrates data gathering tools like **Selenium** and **BeautifulSoup**.

## Features

- **Property Listings**: Browse and view detailed information about various properties.
- **Price Prediction**: Predict property prices based on input factors such as location, size, and type.
- **Recommendations**: Receive tailored property suggestions based on user preferences, including nearby locations, price range, and furnishing type.
- **Market Trends**: Analyze market trends using statistical visualizations.
- **Data Gathering**: Collect property data from various sources using web scraping.

## Tech Stack

- **Back-End**: Flask (Python)
- **Front-End**: HTML, Tailwind CSS
- **Machine Learning**: Random Forest
- **Data Gathering**: Selenium, BeautifulSoup
- **Database**: MySQL

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/veer-debug/match-my-mansion.git
   cd match-my-mansion
2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install Required Packages**

     ```bash
     pip install -r requirements.txt
4. **Set Up the Database**
      ```bash
      python manage.py migrate
5. **Run the Application**
       ```bash

       python app.py
# Usage
- **Property Listings:** Navigate to the listings page to view and explore properties.
- **Price Prediction:** Use the prediction form to estimate property prices based on input details.
- **Recommendations:** View recommended properties tailored to your preferences.
- **Market Trends:** Access the statistics page to see visualizations of market trends.

# AI Integration
### Price Prediction
- **Model Used:** Random Forest
- **Description:** The Random Forest model is trained on historical property data to provide accurate price predictions based on features such as location, property size, and amenities.
Recommendation System
- **Techniques Used:** Collaborative filtering and content-based methods.
- **Description:** Provides personalized property recommendations based on user preferences and historical interactions.
# Example of AI in Action
- **Data Collection:** Gather property data using Selenium and BeautifulSoup.
- **Model Training:** Train the Random Forest model with historical data to learn price trends.
- **Prediction:** Users input property features to receive estimated price ranges.
- **Recommendations:** The system suggests properties based on user preferences and previous interactions.
# Contributing
*Contributions are welcome! If you have suggestions, improvements, or fixes, please follow these guidelines:*

Fork the repository.
Create a new branch for your changes.
Commit your changes with descriptive messages.
Push your changes to your forked repository.
Create a pull request from your branch to the main repository.
License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements
- **Flask:** A lightweight WSGI web application framework.
- **Tailwind CSS:** A utility-first CSS framework.
- **Random Forest:** A machine learning algorithm for predictive modeling.
- **Selenium & BeautifulSoup:** Tools for web scraping and data collection.
