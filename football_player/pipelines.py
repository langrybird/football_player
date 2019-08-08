# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from football_player.items import FootballPlayerItem
import pymysql

class FootballPlayerPipeline(object):
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '123456', 'test1', use_unicode=True, charset='utf8')
        # get cursor
        self.cursor = self.db.cursor()
        print("connecting mysql success!")
    print('test process')



    def process_item(self, item, spider):
        sqlstr = "insert into players(num,name,birthday,height,weight,position,nationality,price,contract_end,starting_info,bench_info,assist,team_name) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        item['num'],item['name'],item['birthday'],item['height'],item['weight'],item['position'],item['nationality'],item['price'],item['contract_end'],item['starting_info'],item['bench_info'],item['assist'],item['team_name'])
        self.cursor.execute(sqlstr)
        return item


    def close_spider(self, spider):
        self.db.commit()
        self.db.close()