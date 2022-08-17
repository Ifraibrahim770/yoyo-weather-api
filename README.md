# YOYO WEATHER API


## To deploy the project (Docker):<br>
 - Install Docker (get it from [HERE](https://docs.docker.com/get-docker/):  and make sure its added to the PATH
 - Navigate to the project's root directory
 - Open a terminal session using Windows Terminal, GitBash or any other CLI tool 
 - You will need a .env file with valid credentials, a sample has been provided, check .env_example
 - Once you have a valid env file run the command
 - Run the command:<br>
   ```
    docker-compose --env-file .env up
   ``` 
 - Wait for the image to build and run on port 8080

## To deploy the project (Locally):<br>
 - Navigate to the project's root directory
 - Create and activate a python3 virtual environment using conda or venv
 - Run the command
   ```
   pip install - r requirements.txt
   ``` 
 - You will need a .env file with valid credentials, a sample has been provided, check .env_example
 - Once the .env file is present, Run the command:<br>
   ```
   python manage.py runserver
   ``` 
 - In some cases for the project to work correctly you might have to run migrations
   ```
   python manage.py migrate
   ``` 
 - Wait for the server to run on port 8080

## Project Endpoints:<br>
 - The host may be <strong>0.0.0.0:8080</strong> or <strong>127.0.0.1:8080</strong> depending on how the project was
deployed
     ```
    http://127.0.0.1:8080/api/docs
    ```
 - Returns a swagger web page where you can interact with the api
   ```
   http://127.0.0.1:8080/api/{location}?days={days}
    ```
 - Returns an api response with temperature information for the specified location
within the specified number of days
    ```
   http://127.0.0.1:8080
    ```
 - Redirects to the docs page

   

