# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FootballPlayerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #球员号码
    num = scrapy.Field()
    #姓名
    name = scrapy.Field()
    #生日
    birthday = scrapy.Field()
    #身高
    height = scrapy.Field()
    #体重
    weight = scrapy.Field()
    #位置
    position = scrapy.Field()
    #国籍
    nationality = scrapy.Field()
    #身家
    price = scrapy.Field()
    #合同截止日
    contract_end = scrapy.Field()
    #首发次数
    #starting_times = scrapy.Field()
    #首发进球数
    #starting_goals = scrapy.Field()
    #首发数据
    starting_info = scrapy.Field()
    #替补数据
    bench_info = scrapy.Field()
    #替补次数
    #bench_times = scrapy.Field()
    #替补进球数
    #bench_goals = scrapy.Field()
    #助攻次数
    assist = scrapy.Field()
    #球队
    team_name = scrapy.Field()

