# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from w3lib.html import replace_tags

import html2text
h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True
h.used = 0

class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def remove_tags(s):
    global h

    if h.used > 1000:
        print("Recreating html2text")
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.used = 0
    else:
        h.used += 1

    return h.handle(s).strip()

def detagify(s):
    return re.sub("\s+", " ", replace_tags(s, " ")).strip()

class Product(scrapy.Item):
    author = scrapy.Field(output_processor=TakeFirst(),)
    title = scrapy.Field()
    description = scrapy.Field()
    date_of_publish = scrapy.Field()
    url = scrapy.Field(output_processor=TakeFirst(),)
    text = scrapy.Field()
    img = scrapy.Field()
    tag = scrapy.Field()
    #image_urls = scrapy.Field()

class CorpusItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst(),)
    text = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),)
    tags = scrapy.Field()
    date_of_publish = scrapy.Field(input_processor=MapCompose(detagify),
        output_processor=TakeFirst(),)
    source = scrapy.Field(output_processor=TakeFirst(),)
    url = scrapy.Field(output_processor=TakeFirst(),)
    img = scrapy.Field(output_processor=TakeFirst(),)
