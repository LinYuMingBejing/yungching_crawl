# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class YungchingRentPipeline(object):
    def __init__(self):
        dbparams={
            'host' : '127.0.0.1',
            'port' : 3306,
            'user' : 'root',
            'password' : 'a828215362',
            'database' : 'yungching',
            'charset' : 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None
    def process_item(self, item, spider):
        params = (item['house_name'],item['price'],item['address'],item['area'],item['floor'],item['housetype'])
        self.cursor.execute(self.sql, params)
        self.conn.commit()
        return item
    
    @property
    def sql(self):
        if not self._sql:
            self._sql="""
            insert into yungching(id,house_name,price,address,area,floor,housetype)
            values(null, %s, %s, %s, %s, %s, %s)
            """
            return self._sql
        return self._sql
