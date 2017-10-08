from scrapy.spider import Spider
from scrapy.selector import Selector
from vldb.items import VldbItem

class VldbSpider(Spider):
    name = "vldb"
    start_urls = [
        'http://www.vldb.org/pvldb/vol10.html/'
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[position()>=2]//li[position()>=2]')
        items = []

        for site in sites:
            item = VldbItem()
            print(site.xpath('a/text()').extract()[0].strip())
            item['author'] = site.xpath('text()[1]').extract()[0].strip().strip(':')
            item['title'] = site.xpath('a/text()').extract()[0].strip()
            items.append(item)

        return items
