import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from time import sleep

class SpiderUlbraSpider(CrawlSpider):
    name = "spider_ulbra"
    allowed_domains = ["ulbra-to.br"]
    start_urls = ["https://ulbra-to.br/bibliotecadigital/publico/home/documento"]

    rules = (Rule(LinkExtractor(allow=r"/documento"), callback="parse_item", follow=True),)
    
    def start_requests(self):
      page_number = 1
      while True:
          new_url = f"https://ulbra-to.br/bibliotecadigital/publico/home/documento/{page_number}"
          if new_url != None:
              yield scrapy.Request(
                  url=new_url,
                  callback=self.parse
              )
              sleep(0.1)
              page_number += 1



    def parse_item(self, response):
        file_url = response.css('a[href$=".pdf"]::attr(href)').get()
        file_url = response.urljoin(file_url)
        yield { 'file_url': file_url }
