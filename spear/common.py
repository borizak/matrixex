import os
import re 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Internal Objects

# Driver Class  
class DriverChrome():
    def __init__(self, visual :bool = False ):
        self.visual = visual
    def __enter__(self):
        path = os.path.join(os.getcwd(), 'chromedriver.exe')
        if not self.visual:
            driver_options = Options()
            driver_options.headless = True
            self.driver = webdriver.Chrome(options = driver_options, executable_path= path)
        else:
            self.driver = webdriver.Chrome(executable_path= path)
        return self.driver
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.driver.quit()

#Base Classes
class WebData():
    url = None
    updated = None 
    storage = None

    def __init__(self) -> None:
        pass 

    @classmethod
    def pull(cls, *args, **kwargs) -> bool:
        return False

    @classmethod
    def search(cls, value : str, **kwargs) -> list:
        return None

    @classmethod
    def all(cls) -> object:
        return None 
