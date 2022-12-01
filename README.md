# Data Collection Pipeline

In this project, my aim is to webscrape IMDB for the best animes to watch, storing all of the information in a list

Milestone 1

In this Milestone, I have created a basic automated web scraping process that bypasses cookies, navigates the page and  getsputs that data in a dictionary. I have used Selenium, specifically the webdriver module, as this module allows you to navigate to the desired web page. The  browser loads all the resources of the website (JavaScript files, images, CSS files, etc.) and executes all the JavaScript on the page. We can also create methods to bypass and execute certain actions, making it wasier to process later on. 

Milestone 2

In this Milestone, I have created functions that allow you to web scrape data from my chosen site. This stage built on what I had already built in the previous milestone. I created various methods to navigate the inital  URL page to a single details page. This page would then be scraped and extract all of the required information, which would be stored in individual dictionaries. These individual dictionaries will be stored  which were saved locally in a json file. 

Milestone 5

In this milestone, we worked on our documentation and our unit testing of public methods. Firstly, it was pivital that we go back and optimise the code we creaated in the previous milestone. At this stage, I abstracted my objects (writing a few core methods that handle all the low-level funcrions). This allowed me to call a few core methods instead of calling every function, one after the other, thus making my code easier to implement. I also decided to change all of my methods to private,  as I am only using one class for my scrsper. These methods are then being tested once I call the public method. 
In terms of documentation, I added docstrings to each function, so that they are easy to understand by other users of your scraper.

Milestone 6