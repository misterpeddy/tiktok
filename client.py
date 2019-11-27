from browser import Browser
import atexit

BASE_URL = "https://www.tiktok.com/en"

class TikTokClient:
    """Provides a REST-ful interface to the TikTok application"""

    def __init__(self):
        self.browser = Browser()
        atexit.register(self._clean_up)
    
    def getTrending(self):
        """Returns list of Trending posts"""
        trending_url = self._construct_url("trending")
        self.browser.get(trending_url)
        self.browser.scrollToBottom()
        web_elements = self.browser._driver.find_elements_by_xpath(
                "//div[@class='jsx-1410658769 video-feed-item']/div/div/div/a")

        posts = []
        for el in web_elements:
            posts.append({
                'url': el.get_attribute('href'), 
                'author': el.get_attribute('href').split("/")[3]})
        return posts

    def _construct_url(self, page):
        return "{}/{}".format(BASE_URL, page)

    def _clean_up(self):
        self.browser.stop()

def example():
    client = TikTokClient()
    client.getTrending()

if __name__=="__main__":
    example()
