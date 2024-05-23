import scrapy
from time import sleep

from crawler_project.items import CrawlerProjectItem

class UniversitySpider(scrapy.Spider):
    name = "go-spider"
    allowed_domains = ["ulbra-to.br"]
    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
    }
    start_urls = ["https://ulbra-to.br/bibliotecadigital/publico/home/documento"]
    desired_courses = ["Sistemas de Informação", "Engenharia de Software", "Ciência da Computação"]

    def start_requests(self):
        page_number = 1
        while page_number != 5000:
            new_url = f"https://ulbra-to.br/bibliotecadigital/publico/home/documento/{page_number}"
            yield scrapy.Request(
                url=new_url,
                callback=self.parse
            )
            page_number += 1

    def parse(self, response):
        if "Nenhum documento encontrado" in response.text:
            self.logger.info(f"Nenhuma página encontrada para page {response.url}")
            return
        
        
        course = response.css('strong:contains("Curso:") + a::text').get()
        
        if course and course.strip() in self.desired_courses:
            title = response.css('.page-header h1::text').get().strip()
            pdf_links = response.css('a[href$=".pdf"]::attr(href)').extract()

            for link in pdf_links:
                yield scrapy.Request(response.urljoin(link), callback=self.parse_item, meta={'title': title,'course': course.strip()})
        else:
            self.logger.info(f"Curso {course} não corresponde aos cursos desejados na página {response.url}")

    def parse_item(self, response):
        title = response.meta['title']
        file_url = response.url     

        item = CrawlerProjectItem()
        
        item['file_urls'] = [file_url]
        item['original_file_name'] = file_url.split('/')[-1]
        item['title'] = title

        yield item