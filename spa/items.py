# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpaItem(scrapy.Item):
    name = scrapy.Field()
    item_url = scrapy.Field()
    image_url = scrapy.Field()
    departement = scrapy.Field()
    species = scrapy.Field()
    breed = scrapy.Field()
    gender = scrapy.Field()

