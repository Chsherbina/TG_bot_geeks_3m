import requests
from parsel import Selector
from pprint import pprint


class HouseParser:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    def get_page(self):
        response = requests.get(HouseParser.MAIN_URL) # запрос страницы с сервера
        print(response.status_code) # проверка, правельный ли путь
        # print(response.text[:350])
        self.page = response.text

    def get_page_title(self): # запрос краткого описания страницы
        html = Selector(text=self.page)
        title = html.css('title::text').get()
        print(title)

    def get_flat_links(self):
        selector = Selector(text=self.page)
        links = selector.css('div.listing a::attr(href)').getall()
        links = list(map(lambda l: f'{self.BASE_URL}{l}', links))
        pprint(links)
        return links[:3]


if __name__ == '__main__':
    parser = HouseParser()
    parser.get_page()
    parser.get_page_title()
    parser.get_flat_links()
