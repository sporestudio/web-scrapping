from scrapy import Spider 
from scrapy.selector import Selector


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_url = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]


def parse(self, response):
    questions = Selector(response).xpath('//*[@id="question-summary-78856856"]/h3')


