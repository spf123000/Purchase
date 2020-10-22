# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    storage_link = scrapy.Field()
    storage_name = scrapy.Field()
    storage_price = scrapy.Field()