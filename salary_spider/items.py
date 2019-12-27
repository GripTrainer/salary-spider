# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassdoorJob(scrapy.Item):

    job_title = scrapy.Field()
    median_base_salary = scrapy.Field()
    min_base_salary = scrapy.Field()
    max_base_salary = scrapy.Field()
    sample_size = scrapy.Field()
    employer_name = scrapy.Field()
    employer_size = scrapy.Field()
    employer_sector = scrapy.Field()
    employer_industry = scrapy.Field()
    employer_location = scrapy.Field()
    employer_location_type = scrapy.Field()
