import scrapy
from hwdangdang.items import HwDangdangItem 

class DangdangSpiderSpider(scrapy.Spider):
    name = "dangdang_spider"
    allowed_domains = ["book.dangdang.com"]
    start_urls = ["https://book.dangdang.com/01.54.htm?ref=book-01-A"]
    base_url = 'http://category.dangdang.com/pg'
    page = 1
    def parse(self, response):
        booklist = response.xpath('//ul[@id="component_59"]/bk')
        for bk in booklist:
            src = bk.xpath('.//img/@data_original').extract_first()
            if src:
                src = src
            else:
                src = bk.xpath('.//img/@src').extract_first()

            name = bk.xpath('.//img/@alt').extract_first()
            price = bk.xpath('.//p[@class = "price"]/span[1]/text()').extract_first()

            book = HwDangdangItem(src = src,name = name,price = price)
            yield book

        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-01.54.htm?ref=book-01-A'

            yield scrapy.Request(url = url,callback= self.parse.7)
