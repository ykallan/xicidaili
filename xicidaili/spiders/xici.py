# -*- coding: utf-8 -*-
import scrapy
import pandas


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']

    start_url = 'https://www.xicidaili.com/nn/'

    def start_requests(self):
        for i in range(1, 21):
            yield scrapy.Request(url=self.start_url+str(i), callback=self.parse)
            # break

    def parse(self, response):

        data = pandas.read_html(response.text)
        # print(type(html[0]))
        # print(type(html))
        # html[0].to_csv('proxy2.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
        # Index(['国家', 'IP地址', '端口', '服务器地址', '是否匿名', '类型', '速度', '连接时间', '存活时间',
        #        '验证时间'],
        #       dtype='object')
        for i in range(len(data)):
            print(data['类型'][i] + "://" + data['IP地址'][i] + ":" + data['端口'][i])
            break



