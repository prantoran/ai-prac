# import the library used to query a website
import urllib.request

# specify the url
wiki = "https://en.wikipedia.org/wiki/Bangladesh"

#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki) 

# pip3 install beautifulsoup4
# import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, 'html.parser')

# to look at nested structure of HTML page
# print(soup.prettify())


# soup.<tag>: Return content between opening and closing tag including tag.
print(soup.title)

# soup.<tag>.string: Return string within given tag
print(soup.title.string)

# Find all the links within page’s <a> tags::  
# We know that, we can tag a link using tag “<a>”. 
# So, we should go with option soup.a and it should return the links available in the web page
# print(soup.a)
# $ <a id="top"></a>
# Above, we have only one output. Now to extract all the links within <a>, we will use find_all()
# print(soup.find_all("a")) 
print(soup.find_all("a").__len__())


# to show only links, we need to iterate over each a tag and then return the link using attribute “href” with get
# all_links = soup.find_all("a")
# for link in all_links:
#     print(link.get("href"))

# to extract information within all table 
all_tables=soup.find_all('table')
# print(all_tables)
# for t in all_tables:
#     print(t.string)

right_table=soup.find('table', class_='wikitable sortable')
# print(right_table)


A=[]
# B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    print("cells:")
    print(cells)
    # print("states:")
    # print(states)
    print("\n")
    
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        
        
        
        # B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

print("A")
print(A)
# print("B")
# print(B)
print("C")
print(C)
print("D")
print(D)
print("E")
print(E)
print("F")
print(F)
print("G")
print(G)


print(A.__len__())
# print(B.__len__())
print(C.__len__())
print(D.__len__())
print(E.__len__())
print(F.__len__())
print(G.__len__())


import pandas as pd


df=pd.DataFrame(A,columns=['Division'])
# df['State/UT']=B
df['Capital']=C
df['Established']=D
df['Area']=E
df['Population']=F
df['Density']=G

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)


'''
other features of beautifulsoup
.parent, .contents, .descendants and .next_sibling, .prev_sibling
'''