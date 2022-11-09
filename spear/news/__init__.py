import spear
from spear.common import DriverChrome as Driver, WebData
from selenium.webdriver.common.by import By
from datetime import datetime
import re 
import pickle
import os 
import os.path as path
import json 


class Article():
    def __init__(self,url, page_source):
        self.url = url
        self.content = re.sub("\<.*?\>","\n<>\n",page_source) # Removing anything in Tag brackets

    def contains(self, text : str):
        return text in self.content

    def source(self):
        with Driver() as drv:
            drv.get(self.url).page_source

class BBC_HOMEPAGE(WebData):
    source_url = 'https://www.bbc.com/'
    storage = path.join(os.getcwd(), f'ARTICLES_STORE')

    __articles_buffer = {}
    __index_file = path.join(storage, "index.json")  
    __homepage_article_class_name = 'block-link__overlay-link'

    def __init__(self) -> None:
        super().__init__()
        os.mkdir(self.storage)

    @classmethod
    def pull(cls, *args, **kwargs) -> None:
        with Driver() as drv:
            
            urls = cls.__fetch_urls(drv)
            new_urls = list(set(urls) - set(cls.__known_urls()))
            for url in new_urls:
                drv.get(f"{cls.source_url}/{url}") #TODO < is this allways the case??
                cls.__articles_buffer[url] = Article(url = url, page_source= drv.page_source)

        cls.__store_articles_from_buffer()

    @classmethod
    def search(cls, value : str, **kwargs) -> list(Article):
        hits = []
        for article in cls.all():
            if article.contains(value):
                hits.append[article]
        return hits 

    @classmethod
    def all(cls) -> list(Article):
        all_articles = []
        index = cls.__index()
        for url in index:
            with open(index[url]) as p:
                all_articles.append(pickle.load(p))
        return all_articles

    @classmethod
    def __fetch_urls(cls, driver) -> list(str):    
        driver.get(cls.source_url)
        article_objects = driver.find_elements(By.CLASS_NAME,cls.__homepage_article_class_name )
        return [obj.get_attribute('href') for obj in article_objects]
          
    @classmethod
    def __store_articles_from_buffer(cls)-> None:
        new_index_values = {}
        for url in cls.articles:
            new_pickle_path = cls.__storage_path_from_url(url)
            with open(new_pickle_path, "wb") as p:
                pickle.dump(cls.__articles_buffer[url], p)
                new_index_values[url] = new_pickle_path
        
        cls.__index_add(new_index_values)
        
        cls.__articles_buffer = {}
        
    @classmethod
    def __storage_path_for_url(cls, url)->str:
        storable_name = url.replace("/", "..")
        return path.join(cls.storage,f"{storable_name}.pickle")
    
    @classmethod
    def __index(cls) -> dict:
        return {} if not path.exists(cls.__index_file) else \
            json.load(cls.__index_file)

    @classmethod
    def __index_add(cls, values : dict) -> None: 
        index = cls.__index()
        for key in values:
            index[key] = values[key]
        json.dump(index, cls.__index_file)

    @classmethod
    def __known_urls(cls) -> list(str):
        return cls.__index.keys()

    # Trying to Store in case an interruption occured while the buffer still contains data
    def __del__(self):
        if len(self.articles_buffer) > 0:
            try:
                self.__store_articles()
            except Exception as e:
                pass 


