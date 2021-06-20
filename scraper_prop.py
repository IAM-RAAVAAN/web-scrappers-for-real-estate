#!/usr/bin/env python
# coding: utf-8

# In[36]:


import requests 
import re
from bs4 import BeautifulSoup
import pandas as pd


# In[37]:


url='https://www.propertywala.com/properties/type-residential_apartment_flat/for-rent/location-pune_maharashtra'

j=requests.get(url)
k=j.text
s=BeautifulSoup(k,'lxml')


# In[38]:


def title(s):
    title=s.find_all('h4')
    the_text=[]
    for a in title:
        the_text.append(a.text.strip())
        
        #print(the_text[:-4])
    return the_text[:-4]


# In[39]:


def link(s):
    link=[]
    for a in s.findAll('a', attrs={'href': re.compile("/P")}):
        link.append('https://www.propertywala.com/'+a.get('href'))
    the_final=list(set(link[1:]))
    return the_final  


# In[40]:


def price(s):
    prices=[]
    price=s.find_all('div',attrs={'class':"propertyPrice"})
    for p in price:
        prices.append(p.text) 
    return prices


# In[41]:


def area(s):
    area=[]
    areas=s.find_all('li',attrs={'class':"features"})
    for p in areas:
        area.append(p.text.strip()) 
    return area


# In[42]:


def post(s):
    postede=[]
    pdate=s.find_all('li',attrs={'class':"posted"})
    for p in pdate:
        postede.append(p.text.strip()) 
    return postede


# In[43]:


d={}
df=pd.DataFrame(d)
df['titile']=title(s)
df['link']=link(s)
df['post']=post(s)
df['area']=area(s)
df['price']=price(s)
l=[]
l.append(df)


# In[44]:


def fra(s):
    df1=pd.DataFrame(d)
    df1['titile']=title(s)
    df1['link']=link(s)
    df1['post']=post(s)
    df1['area']=area(s)
    df1['price']=price(s)
    return df1


# In[45]:


url='https://www.propertywala.com/properties/type-residential_apartment_flat/for-rent/location-pune_maharashtra?page=2'
for i in range(2,5):
    
    
    url=url[:url.index("=")+1]

    url=url+str(i)
    print(url)
    j=requests.get(url)
    k=j.text
    s=BeautifulSoup(k,'lxml')
    l.append(fra(s))
df2=pd.concat(l)


# In[50]:


df2['price']=df2['price'].apply(lambda x: x.strip())
df2.to_csv('prop.csv')


# In[48]:





# In[ ]:




