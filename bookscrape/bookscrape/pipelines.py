# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class BookscrapePipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

    def process_item(self, item, spider):
        if(spider.name == 'kitapsepeti'):
            self.collection = self.conn['smartmaple']['kitapsepeti']
        elif(spider.name == 'kitapyurdu'):
            self.collection = self.conn['smartmaple']['kitapyurdu']
        self.collection.insert(dict(item))
        return item
