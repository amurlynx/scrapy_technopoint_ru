# Scrapy settings for scrapy_technopoint_ru project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_technopoint_ru'

SPIDER_MODULES = ['scrapy_technopoint_ru.spiders']
NEWSPIDER_MODULE = 'scrapy_technopoint_ru.spiders'

ITEM_PIPELINES = ['scrapy_technopoint_ru.pipelines.SQLiteStorePipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_technopoint_ru (+http://www.yourdomain.com)'
