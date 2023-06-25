import scrapy
from ..items import BookscrapeItem

class Kitapyurdu(scrapy.Spider):
    name = 'kitapyurdu'
    start_urls = ['https://www.kitapyurdu.com/index.php?route=product/category&sort=purchased_365&order=DESC&path=1_87&filter_category_all=true&filter_in_shelf=1']
    item = BookscrapeItem()
    
    def parse(self, response):
        for products in response.css('div.product-cr'):
            if(products.css('div.price-new').css('span.value::text').get() is None):
                yield{
                    'title':products.css('div.name.ellipsis').css('span::text').get(),
                    'publisher':products.css('div.publisher').css('span::text').get(),
                    'writers':products.css('div.author.compact.ellipsis').css('a.alt::text').get(), #.replace(" ", ""),
                    'price':products.css('span.price-old').css('span.value::text').get() #.replace(" ", "") + " TL"
                }
            else:
                yield{
                    'title':products.css('div.name.ellipsis').css('span::text').get(),
                    'publisher':products.css('div.publisher').css('span::text').get(),
                    'writers':products.css('div.author.compact.ellipsis').css('a.alt::text').get(), #.replace(" ", ""),
                    'price':products.css('div.price-new').css('span.value::text').get() #.replace(" ", "") + " TL"
                }


        next_page = response.css('a.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        