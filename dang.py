import scrapy
from dangdang.items import DangdangItem
import os
os.system('scrapy crawl douban_data')
#青春文学类：http://category.dangdang.com/cp01.01.02.00.00.00.html
#成功学类：http://category.dangdang.com/cp01.21.02.00.00.00.html
#历史类：http://category.dangdang.com/cp01.36.07.00.00.00.html
#专业工具书：http://category.dangdang.com/cp01.54.06.00.00.00.html
class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.54.06.00.00.00.html"]
    base_url = 'http://category.dangdang.com/pg'
    page = 1
    def parse(self, response):
        li_list = response.xpath('//ul[@id="component_59"]/li')

        for li in li_list:

            src = li.xpath('.//img/@data-original').extract_first()
            if src:
               src = src
            else:
               src = li.xpath('.//img/@src').extract_first()
               
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()#//*[@id="p29660327"]/p[3]/span[1]
            comment = li.xpath('.//a[@class="search_comment_num"]/text()').extract_first()#//*[@id="p29660327"]/p[4]/a
            book = DangdangItem(src = src,name = name,price = price,comment = comment,lable = lable)
            yield book
        
        if self.page < 5:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.54.06.00.00.00.html'

            yield scrapy.Request(url=url,callback=self.parse)
        #scrap crawl dang -o book.csv
            
        