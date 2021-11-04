import scrapy
from scrapy.loader import ItemLoader
from web_crawling.items import ArticleItem
from datetime import date, datetime, timedelta

def get_dates_between(start_date, end_date):
    delta = end_date - start_date       # as timedelta

    dates = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        day = f'{day.day}-{day.month}-{day.year}'
        dates.append(day)
    
    return dates

START_DATE = date(2021, 11, 2)
END_DATE = datetime.now().date()


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

    def start_requests(self):
        for cat in categories:
            for date in get_dates_between(START_DATE, END_DATE):
                url = f'https://tuoitre.vn/{cat}/xem-theo-ngay/{date}.html'
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
