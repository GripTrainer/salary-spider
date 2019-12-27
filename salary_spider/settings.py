import os

from dotenv import load_dotenv

load_dotenv()

BOT_NAME = 'salary_spider'

SPIDER_MODULES = ['salary_spider.spiders']
NEWSPIDER_MODULE = 'salary_spider.spiders'
ROBOTSTXT_OBEY = True
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
RAYGUN_API_KEY = os.getenv("RAYGUN_API_KEY")

EXTENSIONS = {
    "salary_spider.extensions.RaygunErrorMonitoring": 500
}

ITEM_PIPELINES = {
    "salary_spider.pipelines.DatabasePipeline": 400
}


