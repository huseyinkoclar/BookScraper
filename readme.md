# Kitap Bilgisi Kazıyıcı

Bu proje, 'kitapyurdu.com' ve 'kitapsepeti.com' sitelerinden kitaplarla ilgili verileri kazımak için Scrapy kütüphanesini kullanan bir uygulamadır. Örümcekler, siteleri taramak ve kitap adı, yazar, fiyat gibi bilgileri kazımak için kullanılmaktadır. Kazılan veriler, MongoDB veritabanında depolanmakta ve isteğe bağlı olarak JSON formatında dosyaya kaydedilmektedir. Ayrıca, projenin otomatik çalıştırılması için crontab veya benzer bir zamanlama aracı kullanılabilir.

## Gereksinimler

Projenin çalışması için aşağıdaki kütüphanelere ihtiyaç vardır:

- itemadapter==0.8.0
- pymongo==3.12.0
- Scrapy==2.9.0

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın:
   git clone https://github.com/huseyinkoclar/BookScraper

2. Proje dizinine gidin:
    cd BookScaper

3. Proje bağımlılıklarını yükleyin:
    pip install -r requirements.txt

## Kullanım
1. settings.py dosyasını düzenleyin ve gerekli ayarları yapın (örneğin, veritabanı bağlantısı vb.).

Terminalde aşağıdaki komutları çalıştırarak örümceği başlatın:
    scrapy crawl kitapyurdu
    scrapy crawl kitapsepeti

## Veritabanı Bağlantısı

Bu projede, verileri depolamak için MongoDB veritabanı kullanılmaktadır. Varsayılan olarak, MongoDB'nin yerel kurulumunda çalışan `27017` numaralı port kullanılmaktadır.

Veritabanı bağlantı ayarlarını `settings.py` dosyasında düzenleyebilirsiniz. Bağlantı URL'si, kullanıcı adı, şifre ve diğer ilgili parametreleri gerektiği gibi yapılandırabilirsiniz.

## Otomatik Çalıştırma

Projenin her gün değişen bir kaynak için kullanılacağı düşünülürse her gün belli bir saatte çalışması için yapılması gereken işlemler buradaki içerikte bulunmaktadır. Aşağıdaki adımları izleyerek bu otomatik çalıştırmayı yapılandırabilirsiniz:

1. Bilgisayarınızda `crontab` veya benzer bir zamanlama aracı kullanarak otomatik çalıştırmayı ayarlayın. Örnek olarak, her gün saat 12:00'de çalıştırılmasını istediğimizi varsayalım. Bu durumda, crontab ayarlarınızda şu komutu ekleyebilirsiniz:

   ```bash
    0 12 * * * cd /path/to/your/scrapy/project && scrapy crawl kitapyurdu
    0 12 * * * cd /path/to/your/scrapy/project && scrapy crawl kitapsepeti


## Log Sistemi

Projede datadan kaynaklı(çoğunlukla eksik data) herhangi bir şekilde data çekilemezse log.txt dosyasında toplam kaç item eksik olduğu görülebilmektedir.

## Halihazırda yapılmış scrape işleminden örnek datalar
![image](https://github.com/huseyinkoclar/BookScraper/assets/75777777/82b799cc-07f5-458e-9d85-e0292f136e9a)


