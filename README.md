# Movie Sentiment Analysis Project
This project is part of my final project for the Data Academy course organised by the Data Afrique Hub.
This project is a complete web application for analyzing the sentiment of movie comments. It consists of two parts: the frontend, built with Vue.js (using Vite), and the backend, developed with Django and Django REST Framework.

## Features

- **Frontend**:
  - Responsive user interface to explore movies.
  - Listing of movies, integrating data from TMDB.
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
   git clone https://github.com/Projet12345/My-finaldataacademyproject.git
   cd My-finaldataacademyproject

2. **Install the Backend**:
    - Create and activate a virtual environment:
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    - Install dependencies:
    pip install -r requirements.txt
    - Migrate the database:
    python manage.py makemigrations
    python manage.py migrate

3. Install the Frontend:

    Navigate to the frontend folder.
    Install dependencies:
    bash

3. npm install

   - Start the development server:
   bash

    npm run dev

4. Run the Backend:

    In the backend folder, start the server:
    bash

   - python manage.py runserver

## Technologies Used
   - Frontend: Vue.js, Vite
   - Backend: Django, Django REST Framework
   - Database: PostgreSQL
   - Dataset: IMDB Dataset from Kaggle
   - TMDB API
  
## Local links
   - Frontend: http://localhost:5173/
   - API: http://localhost:8000/api/
   - API Dcumentation: http://localhost:8000/api/docs/

Authors

   - Anderson Nguetoum - [Linkedin](https://www.linkedin.com/in/anderson-nguetoum-likeufack-b8888124a/)



