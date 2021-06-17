import subprocess
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def run():
    logger.info('Starting the scrap process')
    start_spider()
    logger.info('Scraping already ends')
    logger.info('Moving scraped data...')
    move_data('cards.csv', '../../', '../transform')
    logger.info('Starting transform process')
    start_transform()
    logger.info('Moving transformed data to load...')
    move_data('clean_cards.csv', '../transform', '../load')
    move_data('clean_stats.csv', '../transform', '../load')
    move_data('clean_types.csv', '../transform', '../load')
    logger.info('Starting load process')
    start_load()
    


def start_spider():
    subprocess.run(['scrapy', 'crawl', 'magic'], cwd='../..')


def move_data(file, place, where):
    subprocess.run(['mv', file, where], cwd=place)


def start_transform():
    subprocess.run(['python3.9', 'main.py'], cwd='../transform')

 
def start_load():
    subprocess.run(['python3.9', 'main.py'], cwd='../load')
 
 
if __name__ == '__main__':
    run()