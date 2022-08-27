import time

import scrapy


class OzonSpider(scrapy.Spider):
    name = "ozon_news"
    starr_urls = [
        "https://seller.ozon.ru/news/",
    ]

    def parse(self, response):
        count = 0
        for news in response.css("div.news-card a::attr(href)"):
            if count == 10:
                break
            else:
                time.sleep(5)
                yield {
                    "title_name": news.css("h3.news-card__content::text").get(),
                    "tags": news.css("div.news-card__mark::text").getall(),
                }
            count += 1
