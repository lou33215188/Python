# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviecrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cineName = scrapy.Field()
    pictureLink = scrapy.Field()
    downloadLink = scrapy.Field()
    iD = scrapy.Field()
