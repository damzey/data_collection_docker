# Data Collection Pipeline

In this project, my aim is to webscrape IMDB for the best animes to watch, storing all of the information in a list

Milestone 3

In this Milestone, I used OOP to create a Scraper class. Inside this class I created a method that loads the page I want to scrape, a mwthod that bypasses the cookies on the page, a method that creates a crawler list (a list of links for each page), and a method that navigates the webpage (whether that I have used Selenium, specifically the webdriver module, as this module allows you to navigate to the desired web page. The browser loads all the resources of the website (JavaScript files, images, CSS files, etc.) and executes all the script on the page. 

Milestone 4

In this Milestone, I have created more method that allow you to web scrape data from my chosen site. This milestone further developed what I had already built in the previous milestone. In this milestone, I created a method that takes you to a single details page from the initial URL page. I also created a method that scrapes the page and extracts all of the required information, which would be stored in individual dictionaries. Another method I created was creating a folder called raw_data in the root of your project. Within there, I would create a folder with the id of the product as it's name. In that folder, I saved each anime dictionary in a file called data.json in their respective id folder name.
Another method I created at this stage was a method for downloading each image poster from the image link. This would also be saved in the respective id folder name.

Milestone 5

In this milestone, we worked on our documentation and our unit testing of public methods. Firstly, it was pivital that we go back and optimise the code we creaated in the previous milestone. At this stage, I abstracted my objects (writing a few core methods that handle all the low-level funcrions). This allowed me to call a few core methods instead of calling every function, one after the other, thus making my code easier to implement. I also decided to change all of my methods to private,  as I am only using one class for my scrsper. These methods are then being tested once I call the public method. 
In terms of documentation, I added docstrings to each function, so that they are easy to understand by other users of my scraper.

Milestone 6

In this milestone, I containerised our code in a docker using Docker Desktop. In order to do this, we first had to evaluate our code, and figure out if I could have made the code more efficient. Once I optimised the efficiency of my code, I ran the code in headless mode (this run the browser as it normally would, but without the graphical user interface.) This is essential to run my scraper within the Docker container. I then had to create a Dockerfile that builds my scraper image locally. 
In order to do this, I chose a base image, put everything required by the scraper within the container, installed any dependencies and anything else required by my implementation. Finally, I ran the main Python file and built the image. Once I was certwain my image ran correclty, I pushed the Docker Image to Docker Hub

Milestone 7

The main purpose of this final milestone was to create a continuous integration and continuous deployment (CI/CD) pipeline to build and deploy my Docker image to DockerHub. In order to do this, I used GitHub Actions as that is a popular CI/CD platform for automating your build, test, and deployment. I set up the relevant GitHub secrets that contains the credentials required to push to your Dockerhub account. From this, I then set up my workflow, and built upon it to allow my workflow to push the image to Docker Hub.