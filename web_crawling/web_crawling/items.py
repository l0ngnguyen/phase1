# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def clean_text(text):
    return remove_tags(text).strip()

class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    publisher = scrapy.Field()
    datetime = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field(input=MapCompose(lambda paragraphs: [clean_text(p) for p in paragraphs]))
    category = scrapy.Field()
    writers = scrapy.Field(input=MapCompose(clean_text))
    tags = scrapy.Field()

if __name__ == '__main__':
    doc = '<div class="author">\r\n            <i class="icon-pencil"></i>MINH ANH\r\n        </div>'
    print(remove_tags(doc).strip())