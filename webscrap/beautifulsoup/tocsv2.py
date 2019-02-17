from urllib.request import urlopen
from bs4 import BeautifulSoup


quote_page = ['http://bdlaws.minlaw.gov.bd/print_sections_all.php?id=693', 'http://bdlaws.minlaw.gov.bd/print_sections_all.php?id=694']

# for loop
data = []
for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urlopen(pg)
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    # Take out the <div> of name and get its value
    name_box = soup.find('span', attrs={'class': 'big_title'}) 
    name = name_box.text.strip() # strip() is used to remove starting and trailing
    # get the index price
    price_box = soup.find('span', attrs={'class':'midium_title'})
    price = price_box.text
    # save the data in tuple
    data.append((name, price))


import csv
from datetime import datetime

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    # The for loop
    for name, price in data:
        writer.writerow([name, price, datetime.now()])