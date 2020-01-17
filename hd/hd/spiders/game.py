# -*- coding: utf-8 -*-
import scrapy
import json
from hd.items import PcItem

class SportsSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = ['matchweb.sports.qq.com']
    start_urls = ['http://matchweb.sports.qq.com/team/rank?competitionId=100008&callback=CBATeamRankCallback']

    def parse(self, response):
        mas = PcItem()
        #mercury = response.xpath('//table[@id="tb-ranking"/tr[contains(@class,"item nth-")')
        mercury=response.text

        '''
        for jay in mercury:
            mas['pm'] = jay.xpath('.//td[@class="serial"]/p/text()')[0].extract()
            mas['qd'] = jay.xpath('.//img/text()')[0].extract()
            mas['sum']= jay.xpath('.//')
        '''
        with  open('C:\\Users\\Administrator\\PycharmProjects\\pc\\pc\\pc\\spiders\\ss.json','r') as f:
             a=json.load(f)
        for k in a['data']['list']:
            mas['pm']=k['serial']
            mas['sum']=int(k['wins'])+int(k['losses'])
            mas['qd']=k['name']
            mas['ying']=k['wins']
            mas['fu']=k['losses']
            mas['feng']=int(int(k['wins'])*2)+int(k['losses'])
            mas['shenglv']=k['wining-percentage']+str('%')

            yield  mas