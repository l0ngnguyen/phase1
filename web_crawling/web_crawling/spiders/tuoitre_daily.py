import scrapy
from scrapy.loader import ItemLoader
from web_crawling.items import ArticleItem

categories = [
    'the-thao',
    'thoi-su',
    'the-gioi',
    'phap-luat',
    'kinh-doanh',
    'van-hoa',
    'suc-khoe',
    'khoa-hoc',
    'giai-tri',
    'giao-duc',
    'xe'
]

class TuoitreSpider(scrapy.Spider):
    name = 'tuoitre'
    custom_settings = {
        'ITEM_PIPELINES': {
            'web_crawling.pipelines.TuoitrePipeline': 400
        }
    }

    def start_requests(self):
        for cat in categories:
            url = f'https://tuoitre.vn/{cat}.html'
            yield scrapy.Request(url=url, callback=self.parse_links)
            
    def parse_links(self, response):
        yield from response.follow_all(css='h3.title-news a', callback=self.parse_details)

    def parse_details(self, response):
        loader = ItemLoader(item=ArticleItem(), selector=response)

        loader.add_value('url', response.url)
        loader.add_value('publisher', 'Tuổi trẻ')
        loader.add_css('datetime', 'div.date-time::text')
        loader.add_value('title', 'h1.article-title::text')
        loader.add_css('body', '#main-detail-body > p')
        loader.add_css('category', 'div.bread-crumbs.fl > ul > li.fl > a::text')
        loader.add_css('writers', 'div.author')
        loader.add_css('tags', 'li.tags-item a::text')

        yield loader.load_item()

if __name__ == '__main__':
    print(END_DATE)
