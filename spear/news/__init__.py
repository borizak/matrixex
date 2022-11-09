import os 
import os.path as path
import json 

import spear.common as common
from spear.common import DriverChrome as Driver, WebData
from selenium.webdriver.common.by import By

class Article():
    def __init__(self,url, content):
        self.url = url
        self.content = content

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
        if not path.exists(self.storage):
            os.mkdir(self.storage)

    @classmethod
    def pull(cls, *args, **kwargs) -> None:
        with Driver() as drv:
            
            urls = cls.__fetch_urls(drv)
            new_urls = list(set(urls) - set(cls.__known_urls()))
            for url in new_urls:
                drv.get(url)
                cls.__articles_buffer[url] = Article(url = url, content= drv.page_source)

        cls.__store_articles_from_buffer()

    @classmethod
    def search(cls, value : str, **kwargs) -> list:
        hits = []
        for article in cls.all():
            if article.contains(value):
                hits.append(article)
        return hits 

    @classmethod
    def all(cls) -> list:
        all_articles = []
        index = cls.__index()
        for url in index:
            with open(index[url], 'r') as f:
                content = json.load(f)['content']
                all_articles.append(Article(url= url, content= content ))
        return all_articles

    @classmethod
    def __fetch_urls(cls, driver) -> list:    
        driver.get(cls.source_url)
        article_objects = driver.find_elements(By.CLASS_NAME,cls.__homepage_article_class_name )
        return [obj.get_attribute('href') for obj in article_objects]
          
    @classmethod
    def __store_articles_from_buffer(cls)-> None:
        new_index_values = {}
        for url in cls.__articles_buffer:
            new_file_path = cls.__storage_path_for_url(url)
            with open(new_file_path, "w") as f:
                article = cls.__articles_buffer[url]
                dumped_data = {f"content" : article.content}
                json.dump(dumped_data, f)
                new_index_values[url] = new_file_path
        
        cls.__index_add(new_index_values)
        
        cls.__articles_buffer = {}
        
    @classmethod
    def __storage_path_for_url(cls, url)->str:
        storable_name = url.replace("/", "_").replace(":", "_").replace(" ", "_").replace("-", "_")
        return path.join(cls.storage,f"{storable_name}.json")
    
    @classmethod
    def __index(cls) -> dict:
        index = {}
        if path.exists(cls.__index_file):
            with open(cls.__index_file, "r") as f:
                index = json.load(f)
        return index        

    @classmethod
    def __index_add(cls, values : dict) -> None: 
        index = cls.__index()
        for key in values:
            index[key] = values[key]
        with open(cls.__index_file, "w") as f:
            json.dump(index, f)

    @classmethod
    def __known_urls(cls) -> list:
        return cls.__index().keys()

    # Trying to Store in case an interruption occured while the buffer still contains data
    def __del__(self):
        if len(self.__articles_buffer) > 0:
            try:
                self.__store_articles()
            except Exception as e:
                pass 


