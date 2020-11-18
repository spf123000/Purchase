# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    commodity_id = scrapy.Field()
    commodity_link = scrapy.Field()
    commodity_name = scrapy.Field()
    commodity_price = scrapy.Field()
    commodity_num = scrapy.Field()
    commodity_total = scrapy.Field()