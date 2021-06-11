import scrapy
import requests
import pandas as pd


DESCRIPTIONS = '//div[@class="card-text-oracle"]/p/text()'  # ''.join()


class DescriptionsScraper(scrapy.Spider):
    descriptions_link = []
    cards = None
    name = 'descriptions'
    start_urls = [
        'https://scryfall.com/'
    ]
    custom_settings = {
        'FEEDS': {
            'cards_descriptions.csv': {
                'format': 'csv',
                'encoding': 'utf-8',
                'indent': 4,
                'overwrite': True
            }
        },
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'CONCURRENT_REQUESTS': 20,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 12,
        'MEMUSAGE_WARNING_MB': 1000,
        'MEMUSAGE_NOTIFY_MAIL': ['francobonfigliovazquez@gmail.com']
    }

    def __init__(self):
        with open('../../cards.csv', 'r', encoding='utf-8') as f:
            self.cards = pd.read_csv(f)
        
        for i, row in self.cards.iterrows():
            self.descriptions_links.append(row['card_link'])

    def parse_descriptions(self, response):
        description = '\n'.join(response.xpath(DESCRIPTIONS).getall())
        yield {
            'description': description
        }

    def parse(self, response):
        for link in self.descriptions_link:
            yield response.follow(link, callback=self.parse_descriptions)
