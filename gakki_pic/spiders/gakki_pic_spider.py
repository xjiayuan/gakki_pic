# -*- coding:utf-8 -*-

from scrapy import Spider
from gakki_pic.items import GakkiPicItem

class GakkiSpider(Spider):
    name = "gakki_pic_spider"
    start_urls = ["http://tieba.baidu.com/p/5155206664"]
    
    def parse(self, response):
        image_url = response.xpath("//img[@class='BDE_Image']/@src").extract()
        print "The urls:/n", image_url
        
        item = GakkiPicItem()
        item["gakki_image_url"] = image_url
        
        yield item
