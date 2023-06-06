import scrapy


class GithubspiderSpider(scrapy.Spider):
    name = "githubspider"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/explore"]

    def parse(self, response):
        
        pass
