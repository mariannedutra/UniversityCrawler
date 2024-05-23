# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
from scrapy.pipelines.files import FilesPipeline


class CrawlerProjectPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.url.split("/")[-1]
        return file_name