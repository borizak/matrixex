import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Internal Objects
__path_ChromeDriver = os.path.join(os.getcwd(), 'chromedriver.exe')

# Driver Class  
class DriverChrome():
    def __enter__(self):
        driver_options = Options()
        driver_options.headless = True
        driver_chrome = webdriver.Chrome(options = driver_options, executable_path= __path_ChromeDriver)
    
        return driver_chrome
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.quit()

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