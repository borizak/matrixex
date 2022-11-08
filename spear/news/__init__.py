import spear
from spear.common import DriverChrome as Driver, WebData


class BBC_HOMEPAGE(WebData):
    source_url = 'https://www.bbc.com/'
    updated = None 
    storage = None

    def __init__(self) -> None:
        
        super().__init__()

    @classmethod
    def pull(cls, *args, **kwargs) -> bool:
        
        # get raw
        raw_list = []
        raw_list = cls.download_main_page_articles()
         
        # basic structure (by url??)
        article_content_by_url = {} 
        for article in raw_list:
            url = extract_url(article)
            content = extract_article_content(article)
            article_content_by_url[url] = content
            cls.store_article(article)
        
        return False

    @classmethod
    def search(cls, value : str, **kwargs) -> list:
        hits = []
        for article in cls.all():
            if string_is_in_article(article, value):
                hits.append[article]
        return hits 

    @classmethod
    def all(cls) -> object:
        articles = list(str)
        articles = cls.get_all_articles()
        return articles

    @classmethod
    def download_main_page_articles(cls):
        articles = []
        source = None 
        with Driver() as drv:
            drv.get(cls.source_url)
            source = drv.page_source
        print(source)
        return articles
        
    
    @classmethod
    def store_article():
        pass

    @classmethod
    def get_all_articles():
        pass 
    




def extract_url():
    pass

def extract_article_content():
    pass

def string_is_in_article():
    pass


