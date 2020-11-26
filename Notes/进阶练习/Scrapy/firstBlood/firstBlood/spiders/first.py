import scrapy


class SpidernameSpider(scrapy.Spider):
    # 爬虫文件名称
    name = 'first'
    # 允许的域名：用来限定start——urls列表中哪些url可以进行请求，（一般不用）
    allowed_domains = ['www.xxx.com']
    # 起始的url列表,该列表存放的url会被scrapy自动进行请求的发送
    start_urls = ['http://www.baidu.com/','http://www.baidu.com/']

    def parse(self, response):
        print(response)
