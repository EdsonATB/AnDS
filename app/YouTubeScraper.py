from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class YouTubeScraper:
    def __init__(self, headless=True):
        self.driver = self._initialize_driver(headless)
    
    def _initialize_driver(self, headless):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver

    def search_video(self, query):
        self.driver.get("https://www.youtube.com/")
        search_box = self.driver.find_element(By.XPATH, 
            '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
        search_box.send_keys(query)
        search_button = self.driver.find_element(By.XPATH, 
            '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button')
        search_button.click()
        
    def click_first_video(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
                '(//ytd-video-renderer//a[@id="video-title"])[1]'))
        ).click()

    def get_video_url(self):
        return self.driver.current_url

    def extract_video_id(self, url):
        match = re.search(r'v=([a-zA-Z0-9_-]+)', url)
        if match:
            return match.group(1)
        else:
            raise ValueError("ID do vídeo não encontrado.")

    def close(self):
        self.driver.quit()

def robo_get_video_id(pesquisa: str, headless=False):
    scraper = YouTubeScraper(headless)
    try:
        scraper.search_video(pesquisa)
        scraper.click_first_video()
        current_url = scraper.get_video_url()
        return scraper.extract_video_id(current_url)
    finally:
        scraper.close()


