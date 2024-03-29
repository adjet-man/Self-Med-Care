# Project Documentation: 
Self-Med Care Web App

# Overview: 
Self-Med Care is a web application designed to provide medication and treatment suggestions based on user input regarding basic health conditions. The application allows users to search for common health issues such as cold, stomach ache, headache, etc., and receive recommendations for medications and treatments.

# Project Flow:
- NB: Template was used and redesigned. 

- Home Page (index.html):
This is the landing page of the Self-Med Care web app.
Users can enter their health condition into a search form.
Upon submitting the form, users are directed to the Results page.
- Results Page (results.html):
This page displays the search results based on the user's input.
It shows the condition searched for and the suggested medications and treatments.
Users can view the recommendations and take necessary actions based on the provided information.

# Technologies Used:
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Data Storage: JSON (data.json file)

# Components: 
- index.html:

  - Home page of the Self-Med Care web app.
  - Contains a search form where users can input their health condition.
    
- results.html:

  - Page for displaying search results.
  - Shows the condition searched for and the suggested medications and treatments.

- app.py:

  - Backend Python script responsible for handling requests and providing search functionality.
  - Utilizes the Flask framework to create API endpoints.
  - Loads health condition data from the data.json file.
  - Provides endpoints for retrieving all data and searching for specific conditions.

# app.py Code Explanation: 
- '/data' Endpoint: Provides all health condition data stored in the data.json file.
- '/search' Endpoint: Handles search queries. It filters data based on the condition provided in the request and returns matching results.
The search functionality is case-insensitive and supports partial matches with any word in the condition input.

# Deployment: 
- On your terminal run app.py for server to run.
- To include more data , changes can be made to the Data.json.
