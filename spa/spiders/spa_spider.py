import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from spa.items import SpaItem

class SpaSpider(CrawlSpider):
    name = "spa-crawler"
    start_urls = ["http://la-spa.fr/adopter-animaux"]
    rules = (
            Rule(LinkExtractor(deny = ['/actualites/'], restrict_xpaths = ['//span[@class="animal-name"]','//li[@class="pager-item"]']), callback='parse_animal', follow = True),
    )

    def parse_animal(self, response):
        if "http://www.spa.asso.fr/adopter-animaux" in response.url:
            pass
        else:
            item = SpaItem()
            item['name'] = response.xpath('//*/h1[@class="title col-xs-12"]/text()').extract()
            item['item_url'] = response.url
            item['image_url'] = response.xpath('//*/div[@class="field field-name-field-image-slideshow field-type-image field-label-hidden"]/div/div/img/@src').extract()
            item['departement'] = response.xpath('//*/span[@class="refuge-name"]/text()').extract() 
            item['species'] = response.xpath('//*/div[@class="field field-name-field-esp-ce field-type-list-text field-label-inline clearfix"]/div/div/a/text()').extract() 
            item['breed'] = response.xpath('//*/div[@class="field field-name-field-race field-type-text field-label-inline clearfix"]/div/div/a/text()').extract()
            item['gender'] = response.xpath('//*/div[@class="field field-name-field-sexe field-type-list-boolean field-label-inline clearfix"]/div/div/a/text()').extract()
            yield item

