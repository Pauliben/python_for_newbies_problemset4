import json, requests
import pandas as pd

title = []
year = []
author = []
wiki_url = []

response = requests.get(url = 'https://the-dune-api.herokuapp.com/books/500')
result = response.json()
#print(result)

for record in result:
    title.append(record['title'])
    year.append(record['year'])
    author.append(record['author'])
    wiki_url.append(record['wiki_url'])

book_list = pd.DataFrame({
    'Title':title,
    "Year":year,
    "Author":author,
    "Wiki_url":wiki_url
})

import os
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
os.makedirs('/blue/bsc4452/viannam/Jupyter_content', exist_ok=True)
book_list.to_csv('/blue/bsc4452/viannam/Jupyter_content/book_list.csv')
#print(book_list.head())

year = defaultdict(int)
count=0
books = open("book_list.csv")
for line in books:
    line = line.rstrip().split(",")
    #print(line)
    year[line[2]] += 1
#for y in year:
    #print(y +': '+ str(year[y]))
new = pd.DataFrame.from_dict(year, orient = 'index')  
#print(new)

plt.hist(new)
plt.xlabel('Books per year')
