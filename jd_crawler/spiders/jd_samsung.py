# -*- coding: utf-8 -*-
import scrapy
from jd_crawler.items import JdCrawlerItem
debug_log = open("debug_log", 'w', encoding='utf-8')


def log(content):
    debug_log.write(content + '\n')


class JdSamsungSpider(scrapy.Spider):
    name = 'jd_samsung'
    allowed_domains = ['jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&enc=utf-8&spm=2.1.1']

    def parse_single(self, response):
        phone = JdCrawlerItem()
        name = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]/li[1]/@title').extract_first()
        if name is None:
            phone['name'] = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]/@title').extract_first()
        else:
            phone['name'] = name

        # price = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[3]/li[13]/text()')\
        #     .extract_first()
        # if price is None:
        #     phone['price'] = response.xpath('/html/body/div[8]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]/text()')\
        #     .extract_first()
        # else:
        #     phone['price'] = price

        memory = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[6]/dl/dl[2]/dd[2]/text()')\
            .extract_first()
        if memory is None:
            phone['memory'] = "None"
        else:
            phone['memory'] = memory

        power_cap = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[10]/dl/dl[1]/dd/text()')\
            .extract_first()
        if power_cap is None:
            phone['power_cap'] = "None"
        else:
            phone['power_cap'] = str(power_cap)

        color = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[2]/dl/dl[1]/dd/text()')\
            .extract_first()
        if color is None:
            phone['color'] = "None"
        else:
            phone['color'] = str(color)

        camera_pixel_front = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[8]/dl/dl[1]/dd/text()')\
            .extract_first()
        if camera_pixel_front is None:
            phone['camera_pixel_front'] = "None"
        else:
            phone['camera_pixel_front'] = str(camera_pixel_front)

        camera_pixel_back = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[9]/dl/dl[2]/dd/text()')\
            .extract_first()
        if camera_pixel_back is None:
            phone['camera_pixel_back'] = "None"
        else:
            phone['camera_pixel_back'] = str(camera_pixel_back)
        phone['url'] = response.url
        yield phone

    def parse(self, response):

        items = response.xpath('//*[@id="J_goodsList"]/ul/li/@data-sku').extract()
        items = map(lambda x: "https://item.jd.com/{}.html".format(x), items)

        for item in items:
            log(item)
            yield scrapy.Request(item, callback=self.parse_single)
