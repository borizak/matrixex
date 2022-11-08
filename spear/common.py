import os
from selenium import webdriver

# Internal Objects
__path_ChromeDriver = os.path.join(os.getcwd(), 'chromedriver.exe')

# Public Objects
driver_chrome = None

# Setups
def driver_chrome_setup():
    global driver_chrome
    driver_chrome = webdriver.Chrome(executable_path= __path_ChromeDriver)

#Base Classes
class WebData():
    url = None
    updated = None 
    storage = None

    def __init__(self) -> None:
        pass 
    @staticmethod
    def pull(cls, *args, **kwargs) -> bool:
        return False

    @staticmethod
    def search(cls, value : str, **kwargs) -> list:
        return None

    @staticmethod
    def all(cls) -> object:
        return None 