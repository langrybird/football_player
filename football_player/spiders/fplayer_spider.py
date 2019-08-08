import  scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from football_player.items import FootballPlayerItem

class FplayerSpider(scrapy.Spider):
    name = 'fplayer'
    allowed_domains = ["win007.com"]
    start_urls = [
       "http://zq.win007.com/cn/team/Lineup/19.html", #英超
       "http://zq.win007.com/cn/team/Lineup/82.html",  # 西甲
       "http://zq.win007.com/cn/team/Lineup/88.html", #德甲
       "http://zq.win007.com/cn/team/Lineup/150.html", #意甲
       "http://zq.win007.com/cn/team/Lineup/197.html", #法甲
       "http://zq.win007.com/cn/team/Lineup/37.html", #中超
       "http://zq.win007.com/cn/team/Lineup/181.html"  # 中超

    ]
    team_url = 'http://zq.win007.com/cn/team/Lineup/'
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait':10}, endpoint='render.html')


    def parse(self, response):

        title = response.xpath('//div[@id="mainTitle"]/table/tbody/tr/td/table/tbody/tr/td/text()').extract()

        for sel in response.xpath('//div[@id="div_Table2"]/table/tbody/tr'):

            item = FootballPlayerItem()
            if len(sel.xpath('td[1]/text()').extract()):
                item['num'] = sel.xpath('td[1]/text()').extract()[0]
            else:
                item['num'] = ''
            if len(sel.xpath('td[2]/a/text()').extract()):
                item['name'] = sel.xpath('td[2]/a/text()').extract()[0]
            else:
                item['name'] = ''
            if len(sel.xpath('td[3]/text()').extract()):
                item['birthday'] = sel.xpath('td[3]/text()').extract()[0]
            else:
                item['birthday'] = ''
            if len(sel.xpath('td[4]/text()').extract()):
                item['height'] = sel.xpath('td[4]/text()').extract()[0]
            else:
                item['height'] = ''
            if len(sel.xpath('td[5]/text()').extract()):
                item['weight'] = sel.xpath('td[5]/text()').extract()[0]
            else:
                item['weight'] = ''
            if len(sel.xpath('td[6]/text()').extract()):
                item['position'] = sel.xpath('td[6]/text()').extract()[0]
            else:
                item['position'] = ''
            if len(sel.xpath('td[7]/text()').extract()):
                item['nationality'] = sel.xpath('td[7]/text()').extract()[0]
            else:
                item['nationality'] = ''
            if len(sel.xpath('td[8]/text()').extract()):
                item['price'] = sel.xpath('td[8]/text()').extract()[0]
            else:
                item['price'] = ''
            if len(sel.xpath('td[9]/text()').extract()):
                item['contract_end'] = sel.xpath('td[9]/text()').extract()[0]
            else:
                item['contract_end'] = ''
            if len(sel.xpath('td[10]/text()').extract()):
                item['starting_info'] = sel.xpath('td[10]/text()').extract()[0]
            else:
                item['starting_info'] = ''
            if len(sel.xpath('td[11]/text()').extract()):
                item['bench_info'] = sel.xpath('td[11]/text()').extract()[0]
            else:
                item['bench_info'] = ''
            if len(sel.xpath('td[12]/text()').extract()):
                item['assist'] = sel.xpath('td[12]/text()').extract()[0]
            else:
                item['assist'] = ''
            item['team_name'] = title[0]
            yield item

        options = response.xpath('//option/@value').extract()
        if len(options):
            for option in options:
                url_info = self.team_url+option+'.html'
                yield SplashRequest(url=url_info, callback=self.parse_item,
                                    args={'wait': 10}, endpoint='render.html')
        else:
            pass

    def parse_item(self, response):
        title = response.xpath('//div[@id="mainTitle"]/table/tbody/tr/td/table/tbody/tr/td/text()').extract()

        for sel in response.xpath('//div[@id="div_Table2"]/table/tbody/tr'):
            item = FootballPlayerItem()
            if len(sel.xpath('td[1]/text()').extract()):
                item['num'] = sel.xpath('td[1]/text()').extract()[0]
            else:
                item['num'] = ''
            if len(sel.xpath('td[2]/a/text()').extract()):
                item['name'] = sel.xpath('td[2]/a/text()').extract()[0]
            else:
                item['name'] = ''
            if len(sel.xpath('td[3]/text()').extract()):
                item['birthday'] = sel.xpath('td[3]/text()').extract()[0]
            else:
                item['birthday'] = ''
            if len(sel.xpath('td[4]/text()').extract()):
                item['height'] = sel.xpath('td[4]/text()').extract()[0]
            else:
                item['height'] = ''
            if len(sel.xpath('td[5]/text()').extract()):
                item['weight'] = sel.xpath('td[5]/text()').extract()[0]
            else:
                item['weight'] = ''
            if len(sel.xpath('td[6]/text()').extract()):
                item['position'] = sel.xpath('td[6]/text()').extract()[0]
            else:
                item['position'] = ''
            if len(sel.xpath('td[7]/text()').extract()):
                item['nationality'] = sel.xpath('td[7]/text()').extract()[0]
            else:
                item['nationality'] = ''
            if len(sel.xpath('td[8]/text()').extract()):
                item['price'] = sel.xpath('td[8]/text()').extract()[0]
            else:
                item['price'] = ''
            if len(sel.xpath('td[9]/text()').extract()):
                item['contract_end'] = sel.xpath('td[9]/text()').extract()[0]
            else:
                item['contract_end'] = ''
            if len(sel.xpath('td[10]/text()').extract()):
                item['starting_info'] = sel.xpath('td[10]/text()').extract()[0]
            else:
                item['starting_info'] = ''
            if len(sel.xpath('td[11]/text()').extract()):
                item['bench_info'] = sel.xpath('td[11]/text()').extract()[0]
            else:
                item['bench_info'] = ''
            if len(sel.xpath('td[12]/text()').extract()):
                item['assist'] = sel.xpath('td[12]/text()').extract()[0]
            else:
                item['assist'] = ''
            item['team_name'] = title[0]
            yield item

