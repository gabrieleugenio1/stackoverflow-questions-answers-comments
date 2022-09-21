# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DadosItem(scrapy.Item):
    # define the fields for your item here like:
    question = scrapy.Field()
    answer = scrapy.Field()
    comments = scrapy.Field()
    votes = scrapy.Field()
    amount_comments = scrapy.Field()
    pass
