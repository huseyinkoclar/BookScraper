import scrapy

class Kitapsepeti(scrapy.Spider):
    name = 'kitapsepeti'
    start_urls = ['https://www.kitapsepeti.com/cizgi-roman?stock=1']

    def parse(self, response):
        products = response.css('#list-slide1003')
        max = min(len(products.css('a.fl.col-12.text-description.detailLink::text').getall()),len(products.css('a.col.col-12.text-title.mt::text').getall()),len(products.css('a.fl.col-12.text-title::text').getall()),len(products.css('div.col.col-12.currentPrice::text').getall()))
        i = 0
        for i in range(max):
            yield{
                'title':products.css('a.fl.col-12.text-description.detailLink::text').getall()[i], #.replace("\n", ""),
                'publisher':products.css('a.col.col-12.text-title.mt::text').getall()[i],
                'writers':products.css('a.fl.col-12.text-title::text').getall()[i],
                'price':products.css('div.col.col-12.currentPrice::text').getall()[i] #.replace("\n", "")
            }

        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

