# Data Collection Pipeline

In this project, my aim is to webscrape IMDB for the best animes to watch by IMDB score using Selenium and requests. Using Object Orientated Programming, I created a scraper class and created all the methods I needed to extract the required information. I was then storing the information I scraped for each anime in their own seperate dictionary which were stored locally as a json file. I eventually edited my code so it can run in headless mode so that I can can use Docker to contain the scraper thus making the application easily deployable. To allow the user to make changes, every time a new feature is added, the scraper undergoes a CI/CD workflow to test that everything works fine and deploys a new version of the application Dockerhub

