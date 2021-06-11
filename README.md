# Magic The Gathering Cards Scraper
#### A simple script that extracts all important data of all Magic cards from the not official Magic site 'Scryfall Magic'

### Configs:
- The URL of the page is: https://scryfall.com/
- The script uses the Python Scrapy framework
- It extracts the name, type,  stats, description and collection  of each card (in spell or instant cards it only extracts what is necessary)
- The output of the scraper is a csv file that contains all dirty information. This file can be opened in Excel or Google Docs to make easier read it.
- The next step of the process is clean the data using Python´s Pandas module and enrich it to export it to a database

### Extra information:
- The value '-' in any key represents 'not applicable', referring to the cards that do not have that key
- In the current state, the script can extract all the cards listed in the 'booster pack' entry in the page list (approximately 13000 cards)

### How does it work?
#### Coming soon...
