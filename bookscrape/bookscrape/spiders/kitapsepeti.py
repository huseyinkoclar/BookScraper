import scrapy

skipped = 0
class Kitapsepeti(scrapy.Spider):
    name = 'kitapsepeti'
    start_urls = ['https://www.kitapsepeti.com/cizgi-roman?stock=1'] #cizgi roman kategorisi

    def parse(self, response):
        products = response.css('#list-slide1003')
        max = min(len(products.css('a.fl.col-12.text-description.detailLink::text').getall()),len(products.css('a.col.col-12.text-title.mt::text').getall()),len(products.css('a.fl.col-12.text-title::text').getall()),len(products.css('div.col.col-12.currentPrice::text').getall()))
        global skipped
        for i in range(max):
            try:
                yield{
                    'title':products.css('a.fl.col-12.text-description.detailLink::text').getall()[i].replace("\n", ""), #kitap ismi 
                    'publisher':products.css('a.col.col-12.text-title.mt::text').getall()[i], #yayıncı
                    'writers':products.css('a.fl.col-12.text-title::text').getall()[i], #yazar
                    'price':products.css('div.col.col-12.currentPrice::text').getall()[i].replace("\n", "") #fiyat
                }
            except AttributeError:
                skipped += 1

       
        if response.css('a.next') != []:
            next_page = response.css('a.next').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        else: 
            with open('log.txt', 'a') as f:
                f.write(str(skipped) + ' item skipped due to missing information while scraping on the kitapsepeti.com\n')
 

