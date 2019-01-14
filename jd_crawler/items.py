# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    memory = scrapy.Field()
    power_cap = scrapy.Field()
    color = scrapy.Field()
    camera_pixel_front = scrapy.Field()
    camera_pixel_back = scrapy.Field()
    url = scrapy.Field()
