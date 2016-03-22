# -*- coding: utf-8 -*-

# Scrapy settings for spa project

BOT_NAME = 'spa'

SPIDER_MODULES = ['spa.spiders']
NEWSPIDER_MODULE = 'spa.spiders'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spa.pipelines.SpaPipeline': 300,
}