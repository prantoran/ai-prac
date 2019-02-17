# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://en.wikipedia.org/wiki/Bangladesh'

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# print(soup)

# Take out the <div> of name and get its value
name_box = soup.find('a', attrs={'title': 'Dhaka'})
print("name:", name_box)
name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('a', attrs={'title':'Dhaka Division'})
price = price_box.text
print(price)


import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
