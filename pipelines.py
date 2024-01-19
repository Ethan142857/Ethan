# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
os.system('scrapy crawl douban_data')

class DangdangPipeline:
    def open_spider(self,spider):
        self.fp = open('book_3.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    def close_spider(self,spider):
        self.fp.close()

import urllib.request

class DangdangDownloadPipeline:
    def process_item(self,item,spider):
        url = 'http:' + item.get('src')
        if not os.path.exists('./books/'):
            os.mkdir('./books/')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)
        return item