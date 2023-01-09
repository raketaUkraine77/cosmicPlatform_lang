
 from fake_useragent import UserAgent


 class CosmicParser:
     def __init__(self, url):
         self.session = requests.Session()
         self.ua = UserAgent()
         self.session.headers = {
             "Accept": "*/*",
             "User-Agent": self.ua.random
         }
