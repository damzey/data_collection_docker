from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from uuid import uuid4
import json
import pprint
import time
import random
import requests
import logging


class Scraper:
    '''
    This class is used to represent the scraper.

    Attributes:
        path (str): the path in which the chromedriver is installed
        driver (): this asttribute stores
        page_url (string): this attribute stores the link for the page I want to load and scrape
        dict_for_anime (dict): a dictionary for each anime
        mass_dict (list): a list of dictionaries 
    '''
    def __init__(self):
        '''See help(Scraper) for accurate signature'''
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--log-level=2')
        self.logging = logging.getLogger('selenium.webdriver.remote.remote_connection')
        self.logging.setLevel(logging.ERROR)
        self.path = 'C:/Users/Admin/Chrome Driver/chromedriver.exe'
        self.driver = webdriver.Chrome(self.path, options = self.options)
        self.page_url = 'https://www.imdb.com/search/keyword/?keywords=anime&sort=user_rating,desc&mode=detail&page=1'
        self.dict_for_anime = {'ID': '', 'Image Link': [], 'Title': '', 'Details': [], 'Ratings': [], 'Summary': [],  'URL': [], 'Timestamp': ''}
        self.mass_dict = [{}]

    def __load_page_to_scrape(self):
        """ This method loads up the page I want to scrape"""
        self.driver.get(self.page_url)

    def __load_and_accept_cookies(self):
        """ This method bypasses cookies"""
        time.sleep(3)
        try:
            accept_cookies_button = self.driver.find_element(By.XPATH, '//button[text()="Accept Cookies"]')
            accept_cookies_button.click()
        except Exception as e:
            print(e)
        else:
            pass

    def __create_list_of_website_links(self):
        """
        This method creates a crawler list

        The purpose of this function is to find all of the elements that contain a 
        link for an anime, and store this in a list. The end product is a list that 
        contains  all of the links for the anime pages.
        """
        anime_container = self.driver.find_element(by=By.XPATH, value='//div[@class="lister-list"]')
        anime_list = anime_container.find_elements(by=By.XPATH, value='./div')
        link_list = []
        for animes in anime_list:
            a_tag = animes.find_element(by=By.TAG_NAME, value='a')
            link = a_tag.get_attribute('href')
            link_list.append(link)
            self.logging.info(link_list)
        return link_list

    def __getting_a_link(self):
        """ This method returns the first link to an anime show on the page """
        anime = self.driver.find_element(by=By.XPATH, value='//*[@class="lister-item-content"]') 
        a_tag = anime.find_element(by=By.TAG_NAME, value='a')
        anime_link = a_tag.get_attribute('href')
        self.dict_for_anime['URL'].append(anime_link)
        return anime_link
    
    def generate_a_random_link_to_scrape(self, link_list):
        """ This method picks a random link from the crawler list we created earlier """
        random_link = random.choice(link_list)
        self.dict_for_anime['URL'].append(random_link)
    
    def __create_unique_id_for_each_anime(self):
        """
        This method creates a universal unique identifier (UUID) for all the animes

        A different UUID gets added to each anime dictionary.
        The purpose of this function is to make it easier to link the details of the anime to the
        image poster, once we download them
        """
        unique_id = str(uuid4())
        self.dict_for_anime['ID'] = unique_id
        return unique_id
    
    def __timestamp(self):
        """ 
        This method creates a timestamp
        
        The purpose of this which gives us the date and time the page was scraped. 
        This is then added to the dictionary for the anime. The benefits of creating this 
        method is that the timestamp to be dynamic, rather than being a stationary value.
        """
        t = time.localtime()
        timestamp =  time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.dict_for_anime['Timestamp'] = timestamp
        return timestamp
    
    def __extract_data_from_anime_link(self, anime_url) :
        time.sleep(4)
        driver = self.driver
        driver.get(anime_url)
        driver.maximize_window()
        time.sleep(4)
        title = self.driver.find_element(by=By.XPATH, value='//h1[@data-testid="hero-title-block__title"]').text 
        self.dict_for_anime['Title'] = title
        details_of_anime = self.driver.find_element(by=By.XPATH, value='//*[@data-testid="hero-title-block__metadata"]').text
        self.dict_for_anime['Details'].append(details_of_anime)
        rating_of_anime = self.driver.find_element(by=By.XPATH, value='//div[@class="sc-7ab21ed2-2 kYEdvH"]').text
        self.dict_for_anime['Ratings'] = details_of_anime
        storyline = self.driver.find_element(by=By.XPATH, value='//div[@class="ipc-html-content-inner-div"]').text
        self.dict_for_anime['Summary'].append(storyline)
        return title, details_of_anime, rating_of_anime, storyline

    def __display_anime_dictionary(self):
        """ This method prints the anime dictionary, and adds the anime dictionary to the 
        list of dictionaries"""
        print()
        pprint.pprint(self.dict_for_anime)
        self.mass_dict.append(self.dict_for_anime)
        self.driver.back()
    
    def __extract_image_url_for_each_anime(self):
        """ 
        This method extracts the image link for the poster.
        
        There are two purposes for this method. Firstly, we need the URL link for the image to add to 
        the dictionary for the respective anime. Secondly, we need the anime poster url to
        download the image
        """
        time.sleep(2)
        anime2 = self.driver.find_element(by=By.XPATH, value='//div[@class="ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width sc-d383958-0 gvOdLN celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2"]') 
        a = anime2.find_element(by=By.TAG_NAME, value='a')
        image_url = a.get_attribute('href')
        self.dict_for_anime['Image Link'].append(image_url)
        return image_url

    def __download_image(self, image_url, filepath):
        """ 
        This method downloads the image poster for the anime
        
        This method takes two arguments, the image link we gathered from the previous method,
        and the filepath where we would like the save the image
        """
        self.image_data = requests.get(image_url).content
        with open(f"raw_data/{filepath}", 'wb') as handler:
            handler.write(self.image_data)

    def __save__each_anime_dictionary_to_json(self, object_to_dump, filepath):
        """ 
        This method stores the dictionary for the anime
        
        This method takes two arguments, the image link we gathered from the previous method,
        and the filepath where we would like the image 
        """
        
        with open(f"raw_data/{filepath}", "w") as outfile:
            json.dump(object_to_dump, outfile, indent=2)
    
    def __navigating_the_page_url(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        next_button = self.driver.find_element(by=By.XPATH, value='//*[@class="lister-page-next next-page"]')
        footer_of_page = self.driver.find_element(by=By.XPATH, value='//*[@class="footer filmosearch"]')
        footer_next_page_link = footer_of_page.find_element(by=By.TAG_NAME, value='a')
        next_page = footer_next_page_link.get_attribute('href')
        self.driver.get(next_page)
        time.sleep(3)
    
#Since I have created all the functions I need for my code to run, I shall tidy it up my code.
#I shall create new methods that group together various method

    def load_page_and_bypass_cookies(self):
        self.__load_page_to_scrape()
        self.__load_and_accept_cookies()

    def get_link_extract_all_data_display_dict(self):
        self.list_of_limks = self.__create_list_of_website_links()
        anime_url = self.__getting_a_link()
        self.__create_unique_id_for_each_anime()
        self.__extract_data_from_anime_link(anime_url)
        self.__timestamp()
        self.image_link = self.__extract_image_url_for_each_anime()
        self.__display_anime_dictionary()

    def get_json_file_and_download_image(self):
        self.__save__each_anime_dictionary_to_json(self.dict_for_anime, '/id_bleach/data.json')
        self.__download_image(self.image_link, '/id_bleach/23112022_152410_1.jpg') 

    def navigate_and_go_to_next_page(self):
        self.__navigating_the_page_url()

def scraping_method():

    scrape = Scraper()
    scrape.load_page_and_bypass_cookies()
    scrape.get_link_extract_all_data_display_dict()
    scrape.get_json_file_and_download_image()
    scrape.navigate_and_go_to_next_page()
    scrape.driver.close()

if __name__ == '__main__':
    scraping_method()