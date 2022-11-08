from spear.common import WebData, driver_chrome as drv
class TLV_AIRPORT(WebData):
    url = 'http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx'
    updated = None 
    storage = None

    @classmethod
    def pull(cls, *args, **kwargs) -> bool:
        return False

    @classmethod
    def search(cls, value : str, **kwargs) -> list:
        return None

    @classmethod
    def all(cls) -> object:
        return None 


     