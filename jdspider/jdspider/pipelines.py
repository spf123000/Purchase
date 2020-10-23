# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from .mysql import MysqldbHelper


class JdspiderPipeline(MysqldbHelper):
    def __init__(self):
        super().__init__()

    def process_item(self, item, spider):
        self.insert('storage_storage', item)
        return item
