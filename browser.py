from browsermobproxy import Server

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

import psutil
import time

class Browser:
    """Orchestrates proxy server and webdriver, exposing a simple browser interface""" 

    def __init__(self, browsermob_path="./bin/browsermob-proxy"):

        # Kill any existing browsermob processes
        for proc in psutil.process_iter():
            if proc.name() == "browsermob-proxy":
                proc.kill()
        
        # Start Browsermob proxy server
        options = {'port': 8090}
        self._server = Server(path=browsermob_path, options=options)
        self._server.start()

        # Instantiate a Chrome driver with appropriate options
        self._proxy = self._server.create_proxy()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-automation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--proxy-server={0}".format(self._proxy.proxy))
        self._driver = webdriver.Chrome(options=chrome_options)

    def get(self, url):
        """Returns a HAR Json blob resuting from GETing the url"""
        self._proxy.new_har(url)
        self._driver.get(url)
        return self._proxy.har

    def scrollToBottom(self):
        """Synchronously scrolls to the bottom of the page"""
        self._driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    def stop(self):
        """Stops the proxy server and selenium driver"""
        self._server.stop()
        self._driver.quit()

def example():
    b = Browser()
    b.get("https://youtube.com")
    b.scrollToBottom()
    b.stop()

if __name__=="__main__":
    example()
