from selenium import webdriver
from selenium.webdriver.common.by import By
from uuid import uuid4
import json
import os
import time
import random
import pprint
import string

#function: 
path = 'C:/Users/Admin/Chrome Driver/chromedriver.exe'
driver = webdriver.Chrome(path)
page_url = 'https://www.imdb.com/search/keyword/?keywords=anime&sort=user_rating,desc&mode=detail&page=1'
driver.get(page_url)

dict_for_anime = {'ID': '', 'Image Link': [], 'English Title': '', 'Details': [], 'Ratings': [], 'Summary': '',  'URL': '', 'Popularity': ''}
mass_dict = [{}]
    
#function:load and accept cookies
time.sleep(3)
try:
    accept_cookies_button = driver.find_element(By.XPATH, '//button[text()="Accept Cookies"]')
    accept_cookies_button.click()
except:
    pass

#function: creating my crawler list
time.sleep(3)
anime_container = driver.find_element(by=By.XPATH, value='//div[@class="lister-list"]')
anime_list = anime_container.find_elements(by=By.XPATH, value='./div')
link_list = []
for animes in anime_list:
    a_tag = animes.find_element(by=By.TAG_NAME, value='a')
    link = a_tag.get_attribute('href')
    link_list.append(link)

#function: getting a random link
random_link = random.choice(link_list)
driver.get(random_link)
dict_for_anime['URL'] = random_link

#function: creating a unique id
id = str(uuid4())
dict_for_anime['ID'] = id

def getting_a_timestamp():
    t = time.localtime()
    timestamp =  time.strftime('%Y-%m-%d %H:%M:%S', t)
    return timestamp

#function: extracting data
time.sleep(2)
print()
english_title = driver.find_element(by=By.XPATH, value='//h1[@data-testid="hero-title-block__title"]').text 
print(type(english_title))
dict_for_anime['English Title'] = english_title
details_of_anime = driver.find_element(by=By.XPATH, value='//*[@data-testid="hero-title-block__metadata"]').text
dict_for_anime['Details'].append(details_of_anime)
rating_of_anime = driver.find_element(by=By.XPATH, value='//div[@class="sc-7ab21ed2-2 kYEdvH"]').text
print(rating_of_anime)
dict_for_anime['Ratings'].append(rating_of_anime)
storyline = driver.find_element(by=By.XPATH, value='//div[@class="ipc-html-content-inner-div"]').text
dict_for_anime['Summary'] = storyline
timestamp = getting_a_timestamp()
dict_for_anime['Timestamp'] = timestamp
try:
    popularity = driver.find_element(by=By.XPATH, value='//div[@data-testid="hero-rating-bar__popularity__score"]').text
    print(popularity)
    dict_for_anime['Popularity'] = popularity
except:
    pass
title_no_punct = english_title.translate(str.maketrans('', '', string.punctuation))
title_no_space = title_no_punct.replace(" ", "")
print(title_no_space)

#function: printing the anime dictionary
print()
pprint.pprint(dict_for_anime)
mass_dict.append(dict_for_anime)
driver.back()


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

new_folder = createFolder('./raw_data/id_{}'.format(title_no_space))

def save__each_anime_dictionary_to_json( object_to_dump, filepath):   
    print("filepath is", filepath)
    with open(f"raw_data/{filepath}", "w") as outfile:
        json.dump(object_to_dump, outfile, indent=2)
 
save__each_anime_dictionary_to_json(dict_for_anime,'id_{}/{}.json'.format(title_no_space, title_no_space))

driver.get(page_url)

driver.close()

