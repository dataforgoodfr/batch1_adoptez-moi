import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from spa.items import SpaItem

class SpaSpider(CrawlSpider):
    name = "spa-crawler"
    start_urls = ["http://www.spa.asso.fr/adopter-animaux"]
    rules = (
            Rule(LinkExtractor(deny = '/actualites/' , restrict_xpaths = ['//span[@class="field-content"]','//li[@class="pager-next"]']), callback='parse_animal', follow = True),
    )

    def parse_animal(self, response):
        if "http://www.spa.asso.fr/adopter-animaux" in response.url:
            pass
        else:
            item = SpaItem()
            item['name'] = response.xpath('//*/h1[@class="title"]/text()').extract()
            item['item_url'] = response.url
            item['image_url'] = response.xpath('//*/img[@class="field-slideshow-image field-slideshow-image-1"]/@src').extract()
            item['departement'] = response.xpath('//*/div[@class="field field-name-field-departement-refuge field-type-taxonomy-term-reference field-label-inline clearfix"]/div/div/text()').extract()
            item['species'] = response.xpath('//*/div[@class="field field-name-field-esp-ce field-type-list-text field-label-inline clearfix"]/div/div/text()').extract()
            item['color'] = response.xpath('//*/div[@class="field field-name-field-couleur field-type-text field-label-inline clearfix"]/div/div/text()').extract()
            item['size'] = response.xpath('//*/div[@class="field field-name-field-taille field-type-list-text field-label-inline clearfix"]/div/div/text()').extract()
            item['breed'] = response.xpath('//*/div[@class="field field-name-field-race field-type-text field-label-inline clearfix"]/div/div/text()').extract()
            item['gender'] = response.xpath('//*/div[@class="field field-name-field-sexe field-type-list-boolean field-label-inline clearfix"]/div/div/text()').extract()
            item['birth_date'] = response.xpath('//*/div[@class="field field-name-field-date-naissance field-type-text field-label-inline clearfix"]/div/div/text()').extract()
            item['rescue'] = response.xpath('//*/div[@class="field field-name-field-sauvetage field-type-list-boolean field-label-inline clearfix"]/div/div/text()').extract()
            item['medal'] = response.xpath('//*/div[@class="field field-name-field-sauvetage field-type-list-boolean field-label-inline clearfix"]/div/div/text()').extract()
            yield item

