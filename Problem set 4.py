#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import urllib.request, urllib.parse, urllib.error
import json
import pandas as pd 

#Create lists
animal_id = []
animal_name = []
animal_type = []
length_max = []
weight_max = []
lifespan = []
habitat = []

serviceurl = 'https://zoo-animal-api.herokuapp.com/animals/rand'

#Set seed for repeatability
random.seed(10)
while True:
    
    rand_num = range(0,1000)
    rand_animal_id = random.sample(rand_num,1)
    if len(rand_animal_id) < 1: break

    url = serviceurl + "?" + urllib.parse.urlencode(
        {'name': rand_animal_id})

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None
    
    #Check if animal has been previously selected
    temp_id = js['id']
    if temp_id in animal_id:
        continue
    else:
        animal_id.append(js['id']) 
        animal_name.append(js['name'])
        animal_type.append(js['animal_type'])
        length_max.append(js['length_max'])
        weight_max.append(js['weight_max'])
        lifespan.append(js['lifespan'])
        habitat.append(js['habitat'])
    
    #Print iterations
    if len(animal_id) % 10 == 0:
        print(f'iteration is {len(animal_id)}% complete')
    
    #Exit after selecting 100 animals 
    if len(animal_id) == 100:
        break

#Store in a dataframe
rand_zoo_animals = pd.DataFrame({
                                 'animal_name':animal_name,
                                 'animal_type':animal_type,
                                 'length_max':length_max,
                                 'weight_max':weight_max,
                                 'lifespan':lifespan,
                                 'habitat':habitat
                                })
#export as csv
import os
os.makedirs('/Users/paul.adunola/Desktop', exist_ok=True)
rand_zoo_animals.to_csv('/Users/paul.adunola/Desktop/rand_zoo_animals.csv')


# In[5]:


#Print data
print(rand_zoo_animals)
  
#show the datatypes
print(rand_zoo_animals.dtypes)


# In[6]:


#Change data type
rand_zoo_animals.length_max = rand_zoo_animals.length_max.astype(float)
rand_zoo_animals.weight_max = rand_zoo_animals.weight_max.astype(float)
rand_zoo_animals.lifespan = rand_zoo_animals.lifespan.astype(int)

#show the datatypes
print(rand_zoo_animals.dtypes)


# In[7]:


# Set the figure size - handy for larger output
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [10, 6]
# Set up with a higher resolution screen (useful on Mac)
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

#Make a plot showing the distribution of animal lifespan
rand_zoo_animals["lifespan"].plot(kind="hist")

plt.title("Distribution of Animal's Life Span")
plt.xlabel("Life Span (Years)")


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("dark")

#Aggregate data by animal type
lifespan_by_animal = rand_zoo_animals.groupby(["animal_type"]).mean()
print(lifespan_by_animal)

#Plot Maximum Lenght and Lifespan by Animal Type
lifespan_by_animal.reset_index().plot(
    x="animal_type", y=["length_max", "lifespan"], kind="bar"
)

plt.title("Barplot of Maximum Lenght and Lifespan by Animal Type")
plt.xlabel("Animal Type")
plt.ylabel("Years/Inches")

#Plot pie chart of maximum weight by animal type
lifespan_by_animal.plot.pie(y='weight_max', figsize=(11, 6))
plt.ylabel("Maximum Weight (kg)")


# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt

#Correlation between animal weight, lenght and lifespan
corr_matrix = rand_zoo_animals.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()


# In[ ]:




