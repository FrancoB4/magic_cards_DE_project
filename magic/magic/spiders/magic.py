import lxml.html as html
import scrapy


CARDS_ITEMS = '//a[@class="card-text text-grid-item"]'
COLLECTIONS_URLS = '//tbody/tr/td[1]/a/@href'
# .replace('\n', '').strip()
COLLECTION_NAME = '//h1[@class="set-header-title-h1"]/text()'
# CARDS = '//a[@class="card-grid-item-card"]/@href'
# .replace('\n', '').strip()  empty list elements
NAMES = '//h6[@class="card-text-title"][1]/text()'
# .replace('\n', '').strip()
TYPES = '//p[@class="card-text-type-line"]/text()'
DESCRIPTIONS = '//div[@class="card-text-oracle"]/p/text()'  # '\n'.join()
# ''.join().replace('\n', '').strip()
# .join().replace('\n', '').strip()
STATS = '//a/div[@class="card-text-stats"]/text()'
CARDS_LINKS = '//a[@class="card-text text-grid-item"]/@href'


class MagicSpider(scrapy.Spider):
    name = 'magic'
    start_urls = [
        'https://scryfall.com/sets?lang=en'
    ]
    custom_settings = {
        'FEEDS': {
            'cards.csv': {
                'format': 'csv',
                'encoding': 'utf-8',
                'indent': 4,
                'overwrite': True
            }
        },
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'CONCURRENT_REQUESTS': 20,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 12,
        'MEMUSAGE_WARNING_MB': 1000,
        'MEMUSAGE_NOTIFY_MAIL': ['francobonfigliovazquez@gmail.com']
    }

    def parse_cards(self, response):
        cards = response.xpath(CARDS_ITEMS).getall()
        names = []
        typess = []
        stats = []
        cards_links = []
        descriptions = []
        collection = response.xpath(
            COLLECTION_NAME).get().replace('\n', '').strip()

        for card in cards:
            card = html.fromstring(card)
            names.append(card.xpath(NAMES)) # ? I can try to get the index [0] here and make it unnecessary to select it in the yield later
            typess.append(card.xpath(TYPES)) # ? *
            stats.append(card.xpath(STATS)) # ? *
            cards_links.append(card.xpath(CARDS_LINKS))
            descriptions.append(' '.join(card.xpath(DESCRIPTIONS)))

        for name, typee, stat, description, card_link in zip(names, typess, stats, descriptions, cards_links):
            if description == '':
                description = '-'
            if stat == []:
                stat.append('-')
            yield {
                'name': name[0].replace('\n', '').strip(),
                'type': typee[0].replace('\n', '').replace('—', '|').strip(),
                'stats': stat[0].replace('\n', '').strip(),
                'description': description,
                'colection': collection,
                'card_link': card_link
            }

    def parse(self, response):
        collections_url = response.xpath(COLLECTIONS_URLS).getall()

        for collection_url in collections_url:
            collection_url += '?as=text'
            yield response.follow(collection_url, callback=self.parse_cards)


# Vamos a intentar aplicar descargar en lugar de cada elemento directamente desde la pagina, vamos a descargar cada objeto carta, y desde dentro de la carta descargaremos
# Todos los items, asi nos aseguramos que cada carta tenga su propia informacion, ademas esto nos permitiria descargar tambien las descripciones.
# Es decir descargariamos el texto HTMl de "CARD" y luego en cada uno de esos codigos buscaremos las exprexiones XPATH que necesitemos
