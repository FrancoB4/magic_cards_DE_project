# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Cards(scrapy.Item):
    card = scrapy.Field()
    names = scrapy.Field()
    types = scrapy.Field()
    stats = scrapy.Field()
    descriptions = scrapy.Field()
    collections = scrapy.Field()
    urls = scrapy.Field()