# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time
class SeleniumMiddleware(object):
    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\Python 3.7\chromedriver.exe")
        # super(SeleniumMiddleware,self).__init__()

    # def __del__(self):
    #     self.driver.close()
    def process_request(self, request, spider):

        
        
        try:
            
            self.driver.get(request.url)
            self.driver.find_element_by_xpath('//div[@class="list_pageNavTop"]/a[@class="next"]').click()
            self.driver.find_element_by_xpath('//div[@class="list_pageNavTop"]/a[@class="next"]').click()
            print('正在爬取')
            
        except TimeoutException:
            return HtmlResponse(url=request.url,request=request,status=500)
            
        return HtmlResponse(url = self.driver.current_url,body=self.driver.page_source,request=request,encoding='utf-8')

