import scrapy



skipped = 0
class Kitapyurdu(scrapy.Spider):
    name = 'kitapyurdu'
    start_urls = ['https://www.kitapyurdu.com/index.php?route=product/category&sort=purchased_365&order=DESC&path=1_87&filter_category_all=true&filter_in_shelf=1']
    #psikoloji kategorisi
    
    def parse(self, response):
        global skipped
        for products in response.css('div.product-cr'):
            try:
                if(products.css('div.price-new').css('span.value::text').get() is None):
                    yield{
                        'title':products.css('div.name.ellipsis').css('span::text').get(), #kitap ismi
                        'publisher':products.css('div.publisher').css('span::text').get(), #yayıncı
                        'writers':products.css('div.author.compact.ellipsis').css('a.alt::text').get().replace(" ", ""), #yazar
                        'price':products.css('span.price-old').css('span.value::text').get().replace(" ", "") + " TL" #fiyat
                    }
                else:
                    yield{
                        'title':products.css('div.name.ellipsis').css('span::text').get(), #kitap ismi
                        'publisher':products.css('div.publisher').css('span::text').get(), #yayıncı
                        'writers':products.css('div.author.compact.ellipsis').css('a.alt::text').get().replace(" ", ""), #yazar
                        'price':products.css('div.price-new').css('span.value::text').get().replace(" ", "") + " TL" #fiyat
                    }
            except AttributeError:
                skipped += 1

        
        if response.css('a.next') != []:
            next_page = response.css('a.next').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        else: 
            with open('log.txt', 'a') as f:
                f.write(str(skipped) + ' item skipped due to missing information while scraping on the kitapyurdu.com\n')
            