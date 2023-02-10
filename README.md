# Data Collection Pipeline

In this project, my aim is to webscrape multiple pages of  IMDB for the best animes (Japanese cartoons) to watch by IMDB score using Selenium and requests.


Using Object Orientated Programming, I created a Scraper class and created all the methods I needed to load the page, bypass the cookies on the page and extract the required information. I was then saving the information I scraped for each anime in their own seperate dictionary, in their own folder, which were stored locally as a json file. Part of the information I extracted were the poster image link, which allowed me to go to the image poster source and download the image of each anime. Since my methods were private and belonged solely to my Scraper class, unittesting for each method was not needed. Over time, I eventually edited my code and added arguments so it can run in headless mode. Doing this allowed me to use Docker to contain the scraper thus making the application easily deployable. To allow the user to make changes, every time a new feature is added, the scraper undergoes a CI/CD workflow to test that everything works fine and deploys a new version of the application Dockerhub.

