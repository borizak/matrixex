from spear.common import WebData, driver_chrome as drv


class BBC_HOMEPAGE(WebData):
    source_url = 'https://www.bbc.com/'
    updated = None 
    storage = None

    def __init__(self) -> None:
 
        super().__init__()

    @staticmethod
    def pull(cls, *args, **kwargs) -> bool:
        
        # get raw
        raw_list = []
        raw_list = download_main_page_articles()
         
        # basic structure (by url??)
        article_content_by_url = {} 
        for article in raw_list:
            url = extract_url(article)
            content = extract_article_content(article)
            article_content_by_url[url] = content
            store_article(article)
        
        return False

    @staticmethod
    def search(cls, value : str, **kwargs) -> list:
        hits = []
        for article in cls.all():
            if string_is_in_article(article, value):
                hits.append[article]
        return hits 

    @staticmethod
    def all(cls) -> object:
        articles = list(str)
        articles = get_all_articles()
        return articles



def download_main_page_articles():
    pass 
def extract_url():
    pass
def extract_article_content():
    pass
def store_article():
    pass
def string_is_in_article():
    pass
def get_all_articles():
    pass 
