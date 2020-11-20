import scrapy
from collections import deque
import re
import traceback

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
            item['commodity_id'] = response.xpath('//*[@id="detailTab"]/div/div[1]/@report-pageparam').extract_first()
            # re.search(r'\d+', original_url).group()
            item['commodity_link'] = original_url
            item['commodity_name'] = response.xpath('//*[@id="itemName"]')[0].xpath('string(.)').extract_first().strip()
            item['commodity_price'] = re.search(r'\d+(.\d+)', response.xpath('//*[@id="priceSale"]')[0].xpath('string(.)').extract_first().strip()).group()
            item['commodity_num'] = '1'
            item['commodity_total'] = str(float(item['commodity_price']) * int(item['commodity_num']))
        except Exception:
            print(traceback.format_exc())
        yield item
