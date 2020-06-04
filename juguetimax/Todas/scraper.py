from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import re
#import logging
#logging.basicConfig(level=logging.INFO)
from config import config

#logger = logging.getLogger(__name__)

class Scraper_juguetimax():
    def __init__(self):
        #logger.info('generating scraper')
        print('generating scraper')
        self.__driver = webdriver.Chrome(executable_path='../chromedriver')
        self.__creds_email = config()['creds']['email']
        self.__creds_password = config()['creds']['password']
        self.__log_in(self.__creds_email, self.__creds_password)


    def __log_in(self, email, password):
        #logger.info('logging in')
        print('logging in')
        try:
            self.__driver.get('https://www.juguetimax.com/account/login?checkout_url=/')
            ## making sure the page loaded
            #time.sleep(10)
            delay = 5
            page_loaded = WebDriverWait(self.__driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="form-field"]/input[@id="customer_email"]')))
            
            email_box = self.__driver.find_element_by_xpath('//form[@action="/account/login"]/div[@class="form-field"]/input[@id="customer_email"]')
            email_box.send_keys(email)

            password_box = self.__driver.find_element_by_xpath('//form[@action="/account/login"]/div[@class="form-field form-field--account-password"]/input[@id="customer_password"]')
            password_box.send_keys(password)

            log_in_button = self.__driver.find_element_by_xpath('//form[@action="/account/login"]/div[@class="form-action-row"]/button[@type="submit"]')
            log_in_button.click()

            time.sleep(3)
        except:
            print('error in log_in function; it was not possible to log-in')

    
    def search_product(self, url):
        #logger.info('searching product')
        print('searching product')
        try:
            self.__driver.get(url)
        except:
            print('error in search_product function for url:\n', url)


    def get_availability(self):
        #logger.info('obtaining availability')
        print('obtaining availability')
        try:
            ## making sure the page loaded
            #time.sleep(10)
            delay = 5
            page_loaded = WebDriverWait(self.__driver, delay).until(EC.presence_of_element_located((By.XPATH, '//h1[@class="product-title"]/p')))
            
            availability = self.__driver.find_element_by_xpath('//h1[@class="product-title"]/p').text
            availability = availability.lower()
            return availability

        except:
            print('error in get_availability function\n')
            return None


    def get_price(self):
        #logger.info('obtaining price')
        print('obtaining price')
        try:
            ## making sure the page loaded
            #time.sleep(10)
            delay = 5
            page_loaded = WebDriverWait(self.__driver, delay).until(EC.presence_of_element_located((By.XPATH, '//div[@class="price--main"]/span')))

            price_text = self.__driver.find_element_by_xpath('//div[@class="price--main"]/span').text
            price_list = re.split(':', price_text)
            price_number = price_list[1]
            price = price_number.replace('$', '').strip()
            return price

        except:
            print('error in get_price function\n')
            return None


    def log_out(self):
        ## making sure the page loaded
        #time.sleep(10)
        delay = 5
        page_loaded = WebDriverWait(self.__driver, delay).until(EC.presence_of_element_located((By.XPATH, '//li[@class="site-header-account-link"]/a[@href="/account/logout"]')))
        
        log_out_button = self.__driver.find_element_by_xpath('//li[@class="site-header-account-link"]/a[@href="/account/logout"]')
        log_out_button.click()

        time.sleep(3)


    def close_driver(self):
        self.__driver.close()


    def check_request_status(self, url):
        response = requests.get(url)
        request_status = response.status_code
        return request_status


if __name__ == '__main__':
    url_product = 'https://www.juguetimax.com/products/lego-super-heroes-persecucion-en-helicoptero-de-viuda-negra-76162'
    scraper = Scraper_juguetimax()
    scraper.search_product(url_product)
    availability = scraper.get_availability()
    print(availability)
    price = scraper.get_price()
    print(price)

    scraper.log_out()
    scraper.close_driver()
    
