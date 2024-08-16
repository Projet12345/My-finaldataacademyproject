# Movie Sentiment Analysis Project
This project is part of my final project for the Data Academy course organised by the Data Afrique Hub.
This project is a complete web application for analyzing the sentiment of movie comments. It consists of two parts: the frontend, built with Vue.js (using Vite), and the backend, developed with Django and Django REST Framework.

## Features

- **Frontend**:
  - Responsive user interface to explore movies.
  - Listing of movies with ratings and details, integrating data from TMDB.
  - User authentication system to allow users to leave comments.

- **Backend**:
  - API built with Django REST Framework.
  - Integration of a sentiment analysis model trained on the IMDB dataset from Kaggle.
  - Storage of analyzed comments with their results in a database.

## How It Works

1. **Registration and Login**:
   - Users can create an account and log in to comment on films.

2. **Comment Submission**:
   - When a user submits a comment, it is evaluated by the model to determine whether it is positive or negative.

3. **Comment Analysis**:
   - Comments are stored in the database along with their analysis results.

4. **Model Testing**:
   - Python scripts were used to generate users and comments to test the robustness of the model.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <REPOSITORY_URL>
   cd <repository_name>