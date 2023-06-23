# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscrapeItem(scrapy.Item):
    title = scrapy.Field()
    publisher = scrapy.Field()
    writers = scrapy.Field()
    price = scrapy.Field()
