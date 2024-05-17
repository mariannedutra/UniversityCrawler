import scrapy

from time import sleep

class ULBRASpider(scrapy.Spider):
    name = "ceulp"
    allowed_domains = ["ulbra-to.br"]
    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
    }
    start_urls = ["https://ulbra-to.br/bibliotecadigital/publico/home/documento"]
    

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


    def parse(self, response):

        if "Nenhum documento encontrado" in response.text:
            self.logger.info(f"Nenhuma página encontrada para page{self.page_number}")
            return
        
        title = response.css('.page-header h1::text').get().strip()
        pdf_links = response.css('a[href$=".pdf"]::attr(href)').extract()
        
        for link in pdf_links:
            yield scrapy.Request(response.urljoin(link), callback=self.save_pdf, meta={'title': title})

    def save_pdf(self, response):
        title = response.meta['title']
        file_name = response.url.split('/')[-1]
        yield {
            'title': title,
            'file_name': file_name,
            'file_url': response.url
        }