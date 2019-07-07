# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from yungching_rent.items import YungchingRentItem
class RentAnalysisSpider(scrapy.Spider):
    name = 'rent_analysis'
    allowed_domains = ['rent.yungching']
    start_urls = ['http://rent.yungching.com.tw/']
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Python 3.7\chromedriver.exe")
    
    def parse(self, response):
        
        self.driver.get(response.url)
        while True:
            
            self.driver.find_element_by_xpath('//div[@class="list_pageNavTop"]/a[@class="next"]').click()
            sel = Selector(text=self.driver.page_source)

            house_name = sel.xpath('//h2/a[@title]/text()').getall()
            price = sel.xpath('//p[@class="price"]/span/text()').getall()
            address = sel.xpath('//ul[@class="houseul01"]/li[1]/text()').getall()
            area = sel.xpath('//ul[@class="houseul01"]/li[2]/text()').getall()
            floor = sel.xpath('//ul[@class="houseul03"]/li[1]/text()').getall()
            housetype = sel.xpath('//ul[@class="houseul03"]/li[2]/text()').getall()
            for value in zip (house_name,price,address,area,floor,housetype):
                house_name,price,address,area,floor,housetype = value
                item = YungchingRentItem(house_name=house_name,price=price,address=address,area=area,floor=floor,housetype=housetype)
                yield item            
        
        
