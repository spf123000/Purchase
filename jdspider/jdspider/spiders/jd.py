import scrapy
from collections import deque
import re
import win32api

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
            yield scrapy.Request(url=url, meta={'url':url}, callback=self.parse)

    def parse(self, response):
        item = JdspiderItem()
        try:
            original_url = response.meta['url']
            item['commodity_id'] = re.search(r'\d+', original_url).group()
            item['commodity_link'] = original_url
            item['commodity_name'] = response.xpath('//*[@id="itemName"]')[0].xpath('string(.)').extract_first().strip()
            item['commodity_price'] = response.xpath('//*[@id="priceSale"]')[0].xpath('string(.)').extract_first().strip()
        except Exception:
            win32api.MessageBox(0, '链接' + original_url + '不存在！')
        yield item
