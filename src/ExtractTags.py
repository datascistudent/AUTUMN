__author__ = 'gkannappan'

from bs4 import BeautifulSoup
from pprint import pprint

soup = BeautifulSoup(open(r"/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_new.txt", 'r+'))

tag = [tag.name for tag in soup.find_all()]
pprint(tag)