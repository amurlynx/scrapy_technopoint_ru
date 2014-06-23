# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spider import Spider
from scrapy.selector import Selector

from scrapy_technopoint_ru.items import Lev0Item

class TechnoSpider(Spider):
    name = "techno"
    allowed_domains = ["technopoint.ru"]
    start_urls = [
        "http://technopoint.ru/catalog/",
    ]

    def parse(self, response):
        sel = Selector(response)
        #print sel
        lev0 = sel.xpath('//ul/li[@class="lev3"]')
        items =[]
        for cat in lev0:
            item = Lev0Item()
            item['Name'] = cat.xpath('a/text()').extract()
            item['Href'] =  "http://technopoint.ru"+''.join(cat.xpath('a/@href').extract())
            item['Count'] = cat.xpath('span[@class="count"]/text()').extract()
            items.append(item)
        #sites = sel.xpath('/html/body/*/div[@class="quote"]')
        #items = []
        #print sites
        #for site in sites:           
        #    item = Quotes()
        #    item['title'] = site.xpath('div [@class="text"]').extract()
        #    #.select('//div[@class="text"]').extract()
        #    print site.xpath('div [@class="text"]').extract()
        #    items.append(item)
        return items
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
