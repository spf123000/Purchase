import scrapy
from collections import deque

from jdspider.items import JdspiderItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    # allowed_domains = ['123']   
    def start_requests(self):
        new_urls, new_search = deque(), deque()
        with open('url_list.txt') as f:
            for line in f:
                if line.startswith('https://'):
                    new_urls.append(line.strip())
                else:
                    new_search.append(line.strip())
        for url in new_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = JdspiderItem()
        item['storage_link'] = response.url
        item['storage_name'] = response.xpath('//*[@id="itemName"]')[0].xpath('string(.)').extract_first().strip()
        item['storage_price'] = response.xpath('//*[@id="priceSale"]')[0].xpath('string(.)').extract_first().strip()
        yield item
