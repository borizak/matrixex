import os 
import os.path as path
from html_table_parser.parser import HTMLTableParser
import pandas

import spear.common as common
from spear.common import DriverChrome as Driver, WebData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Flight():
    def __init__(self,url, content):
        self.url = url
        self.content = content

    def contains(self, text : str):
        return text in self.content

    def source(self):
        with Driver() as drv:
            drv.get(self.url).page_source

class TLV_AIRPORT(WebData):
    source_url = 'http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx'
    storage = path.join(os.getcwd(), f'FLIGHTS_STORE')

    __flights_buffer = {}
    # __index_file = path.join(storage, "index.json")  
    # __homepage_article_class_name = 'block-link__overlay-link'

    def __init__(self) -> None:
        super().__init__()
        if not path.exists(self.storage):
            os.mkdir(self.storage)

    @classmethod
    def pull(cls, *args, **kwargs) -> None:
        # request = urllib.request.Request(url=cls.source_url)
        # page_content =  urllib.request.urlopen(request).read().decode('utf-8')
        
        with Driver(visual = True) as drv:
            drv.get(cls.source_url)
            
            button = drv.find_element(By.ID, "next")
            while(button.is_displayed()):
                button.click()
            
            parser = HTMLTableParser()
            parser.feed(drv.page_source)
            table_as_df = pandas.DataFrame(parser.tables[0])
            print(table_as_df)
            #     # drv.execute_script("arguments[0].click();", button_object)
                
            # print('a')
            # # driver.execute_script("arguments[0].click();", l)
            # # extract_table()
            # # turn_into_json()
            # print(source) 
        
    @classmethod
    def search(cls, value : str, **kwargs) -> list:
        pass 
    @classmethod
    def all(cls) -> list:
        pass

     