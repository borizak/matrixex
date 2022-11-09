SETUP:
======

1. run :
    pip install -r requirements.txt

2. 
    download driver binary from:
        https://chromedriver.storage.googleapis.com/<YOUR CHROME VERSION>/<YOUR OS VERSION>
    into :
        ~/.../spear/

MODULE STRUCTURE:
=================
- The spear sub-modules group themed data sources. (spear.news, spear.flights, etc...)
- Each sub-module exposes spear.common.WebData classes, one per supported website/data source, which contain 3 main functions:

        - Attributes (read only):
            - source_url : str 
            - updated : datetime.datetime 
            - storage : str
        
        - Functions:
            - pull(*args, **kwargs) -> None
            - search(value : str, **kwargs) -> list(object)
            - all() -> object 
            - drop() -> None

(For this exercise, only classes spear.news.BBC_HOMEPAGE and spear.flights.TLV_AIRPORT were implemented.)

NOTE-WORTHY SPECIFICS:
=====================
- spear.news.BBC_HOMEPAGE class:
    - Stores the Article data as pickles, on every pull() request
    - Manages and index.json file to slightly optimize duplicate checks
    - Exposes a drop_storage()
- spear.flights.TLV_AIRPORT class:
    - ?

INSTRUCTION FOR EXTENDING THE MODULE WITH MORE SOURCES:
=======================================================
In spear/<data category>/__init__.py :

1. Implement a class with a descriptive name (typically, name of the data source), inheriting the spear.common.WebData base class.
    In this class:

    1.  Set public attributes:
         'source_url' with the source for your data collection.
         'storage' with a pointer to a static location on disk/db etc.

    2.  Implement a classmethod with signature:
    
        ```
        pull(*args, **kwargs)-> bool
        ```

        - This method is responsible for:
        1. All collection logic, STRICTLY from the class 'source_url' attribute.
        2. Storing the data on disk/db/etc.

    3. Implement a classmethod with signature:

        ```
        all() -> list
        ```

        - This method should load ALL the source data from disk/db to memory and return the containing object.
        
    4. - implement a classmethod with signature:
        ```
        search(value : str , **kwargs) -> list(object)
        ```
        - This method should return a list of objects representing the 'hits' for the searched string.

2. The spear module provides a safe context manager for Selenium driver (currently only chrome-107). 

    ```
    from spear.common import DriverChrome
    with DriverChrome() as drv:
            drv.get('www.google.com')
    ```

