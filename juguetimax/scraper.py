from bs4 import BeautifulSoup
import requests

class Scraper_juguetimax():
    def __init__(self, link):
        self.__link = link
        self.__html = None 
        self.__createSoup(self.__link)
        self.__price = self.__get_price(self.__html)
        self.__status = self.__get_status(self.__html)

    def __createSoup(self, link):
        response = requests.get(link)
        response.raise_for_status()
        self.__html = BeautifulSoup(response.text, 'html.parser')
        

    def __get_price(self, html):
        pass

    def __get_status(self, html):
        pass


if __name__ == '__main__':
    Scraper_juguetimax('https://www.juguetimax.com/products/lego-star-wars-casco-de-piloto-de-caza-tie-fighter-75274')