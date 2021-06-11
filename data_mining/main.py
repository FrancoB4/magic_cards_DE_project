import argparse
from .common import config
import logging
import subprocess
logging.basicConfig(level=logging.INFO)


def _run(cards_site):
    pass


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    cards_sites = config()['cards_database_sites'].keys()

    parse.add_argument('cards_site',
                       help='The site you wont to scrape',
                       type=str,
                       choices=cards_sites)

    arg = parse.parse_args()
    _run(arg.cards_site)