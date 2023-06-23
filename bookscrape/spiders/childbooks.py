import scrapy

class Childbooks(scrapy.Spider):
    name = 'childbooks'
    start_urls = ['https://www.kitapyurdu.com/kategori/kitap/1.html']

    def parse(self, response):
        for products in response.css('div.product-cr'):
            yield{
                'title':products.css('div.name.ellipsis').css('span::text').get(),
                'publisher':products.css('div.publisher').css('span::text').get(),
                'writers':products.css('div.author').css('span::text').get(),
                'price':products.css('div.price-new').css('span.value::text').get().replace(' ', '₺') 
            }