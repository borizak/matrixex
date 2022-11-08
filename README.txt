======
SETUP:
======

1. run :
pip install -r requirements.txt
2. 
    download driver binary from:
        https://chromedriver.storage.googleapis.com/<YOUR CHROME VERSION>/<YOUR OS VERSION>
    into :
        ~/.../spear/
 ?????       
3. run the flask application
4. go to 'localhost:5000/spear/'
  ??????
=================
MODULE STRUCTURE:
=================
- The spear module requires explicit call for the init() method
- The spear sub-modules group themed data sources. (spear.news, spear.flights, etc...)
- Each sub-module exposes spear.common.WebData classes, one per supported website/data source, which contain 3 main functions:
        - Attributes (read only):
            - source_url : str 
            - updated : datetime.datetime 
            - storage : str
        
        - Functions:
            - pull(*args, **kwargs) -> bool
            - search(value : str, **kwargs) -> list(object)
            - all() -> object 

(For this exercise, only classes spear.news.BBC_HOMEPAGE and spear.flights.TLV_AIRPORT were implemented.)

======================================
EXTENDING THE MODULE WITH MORE SOURCES:
======================================
In spear/<data category>/__init__.py :

1. Implement a class with a descriptive name (typically, name of the data source), inheriting the spear.common.WebData base class.
    In this class:

    1.  - Specify the class attribute 'url' with the source for your data collection.

    2.  - implement a static scraping method, with signature:
                pull(*args, **kwargs)-> bool

        - This main method is responsible for:
            1. All collection logic, STRICTLY from the class 'source_url' attribute.
            2. Storing the data on disk/db/whatever is relevant to your solution.
        - This method should update the class read-only attributes:
            - 'updated'(datetime.datetime) with the relevant run time
            - 'storage'(str) with a string pointing to your chosen storage solution
        - This method should return:
            True if the process succeeded. 
            False otherwise.

    3. - implement a static load method, with signature:
                all() -> object

        - This method should load ALL the source data from disk/db to memory and return the containing object.
        - This method should return a None object if data for source was not scraped yet.
        
    4. - implement a static search method, with signature :
                search(value : str , **kwargs) -> list(object)

        - This method should return a list of objects (typically url's, but could be any object) which are considered 'hits' for the searched string.
        - This method should return an empty list if no 'hits' were found
        - This method should return a None object only if the data for the source was not scraped yet.
