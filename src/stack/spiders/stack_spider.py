from scrapy import Spider 
from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_url = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]


def parse(self, response):
    questions = Selector(response).xpath('//*[@id="question-summary-78856856"]/h3')

    for question in questions:
        item = StackItem()
        item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
        item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
        yield item

