#import libraries

import urllib.request as urllib2
from bs4 import BeautifulSoup

# specify the url

p = 'https://en.wikipedia.org/wiki/Rose'

# for loop
data = []
for pg in p:
 # query the website and return the html to the variable ‘page’
 page = urllib2.urlopen(pg)

# parse the html using beautiful soap and store in variable `soup`
 soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
 name_box = soup.find('p', attrs={'class': 'hatnote navigation-not-searchable'})
 name = name_box.text.strip() # strip() is used to remove starting and trailing

