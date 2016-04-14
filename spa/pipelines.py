# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class SpaPipeline(object):
    def process_item(self, item, spider):
        # Only select pets with enough informations
        if (item['name']) and (item['species']) and (item['gender']):
            item['name'][0] = item['name'][0].title().partition(' ')[0].partition(',')[0]
            
            # Lowercase some fields
            lowercase_fields = ['breed', 'gender', 'species']
            for field in lowercase_fields:
                if item[field]:
                    item[field][0] = item[field][0].lower()
            
            # Add gender and pronoun to the ``species`` field
            if item['gender'][0] == 'femelle':
                if item['species'][0] == 'chat':
                    item['species'][0] = 'une chatte'
                elif item['species'][0] == 'chien':
                    item['species'][0] = 'une chienne'
            else:
                if item['species'][0] == 'chat':
                    item['species'][0] = 'un chat'
                elif item['species'][0] == 'chien':
                    item['species'][0] = 'un chien'
            
            # Drop reserved pets
            reserved_words = [u'reserv', u'réserv']
            if any(word in item['name'][0].lower() for word in reserved_words):
                raise DropItem("This pet is already reserved")
            
            # Keep only the number of the departement
            if item['departement']:
                item['departement'][0] = item['departement'][0].partition(' ')[0].partition('-')[0]

            # Keep only the first image
            if item['image_url']:
                item['image_url'] = item['image_url'][0]

            return item
        else:
            raise DropItem("This animal has not enough information")
