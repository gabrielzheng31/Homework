# -*- coding: utf-8 -*-
import scrapy
from doubantopic.items import DoubantopicItem

class DbtopicSpider(scrapy.Spider):
    name = 'dbtopic'
    allowed_domains = ['https://www.douban.com/group/topic/105419585/']
    start_urls = ['https://www.douban.com/group/topic/105419585//']

    def parse(self, response):
        sel = scrapy.Selector(response)
        title = sel.xpath('//div[@id="content"]')
        main_topic = sel.xpath('//div[@class="topic-doc"]//div[@class="topic-content"]')
        reply = sel.xpath('//ul[@class="topic-reply"]//div[@class="reply-doc content"]')
        items = []

        title_item = DoubantopicItem()
        title_item['content'] = title.xpath('h1/text()').extract()[0].strip()
        items.append(title_item)

        main_topic_item = DoubantopicItem()
        main_topic_item['content'] = main_topic.xpath('p/text()').extract()[0]
        items.append(main_topic_item)

        for each in reply:
            item = DoubantopicItem()
            item['content'] = each.xpath('p/text()').extract()
            items.append(item)

        return items
