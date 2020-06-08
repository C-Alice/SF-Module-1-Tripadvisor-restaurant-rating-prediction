import pandas as pd
from multiprocessing.dummy import Pool
import requests
from bs4 import BeautifulSoup
import time
import re

#creating a list of links to parse
links_list = ['https://www.tripadvisor.ru'+i for i in data['URL_TA']]

#function to collect required features        
def links_scrapper(link):
    response = requests.get(link,time.sleep(0.5), headers = {'User-agent': 'Mozilla/5.0'})
    page = BeautifulSoup(response.text, 'lxml')
    try:
        marks = [i.text for i in page.find_all('span', class_='row_num is-shown-at-tablet')]
    except:
        marks = 0
    try:
        photos = re.findall(r'\d+', page.find('span', class_='details').text)[0]
    except:
        photos = 0
    return {re.findall('-(d\d+)-', link)[0]: {'marks': marks, 'photos':photos}}


pool = Pool(15)

marks_photos_data = pool.map(links_scrapper, links_list)

#function to create a dataframe from collected data    
def build_df(extra_data):
    result = self.scrapper()
    keys = []
    marks = []
    photos = []
    for elem in extra_data:
        for key, value in elem.items():
            keys.append(key)
            marks.append(value['marks'])
            photos.append(value['photos'])
    return pd.DataFrame({'ID_TA': keys, 'marks': marks, 'photos':photos})

