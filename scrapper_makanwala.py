#!/usr/bin/env python
# coding: utf-8

# In[61]:


import requests 
import re
from bs4 import BeautifulSoup
import pandas as pd


# In[62]:


number_of_pages=3


# In[63]:


def locality(s):
    s=requests.get(url).text
    s=BeautifulSoup(s,'lxml')
    sta=s.find_all('span',attrs={'itemprop':"addressLocality"}) 
    k=[]
    for si in sta:
        k.append(si.text)
    return k


# In[64]:



def details(s):
##for prices and BHK AND AREA
    price=s.find_all('span',attrs={'class':"val"}) 
    
    k=[]
    for p in price:
        k.append(p.text)

    l=[]
    for k in k:
        if k:
            l.append(k)
    #geeting the line append in the cards
    k=[]
    for i in range(0,len(l),3):
        k.append(l[i:i+3])
    return k


# In[65]:


def tit_text(s):
  title=s.find_all('a',attrs={'class':"typelink"}) #titles 
  k=[]
  k1=[]
  for a in title:
      k.append( a['href'])
      k1.append(a.text)##links and name that appers
  return k,k1


# In[66]:


def style(s):
    sta=s.find_all('td',attrs={'class':"val"}) 
    k=[]
    for si in sta:
        k.append(si.text)
    return k


# In[67]:


def dep(s):
    detail=s.find_all('li',attrs={'title':"deposit"}) 
    k=[]
    for d in detail:
        k.append(d.text)
    return k


# In[68]:


def name(s):

    sta=s.find_all('span',attrs={'itemprop':"name"}) 
    k=[]
    for si in sta:
        k.append(si.text)
    return k


# In[69]:


def scrap(url):
    s=requests.get(url).text
    s=BeautifulSoup(s,'lxml')
    print()
    col=['BHK','PRICE','AREA']
    #in spreade sheet
    df=pd.DataFrame(details(s),columns=col)
    col=['text','links']
    k,k1=tit_text(s)
    try:
     df['link']=k
    except:
        df['link']='NA'
    try:
        df['text']=k1
    except:
        df['text']='NA'
    try:
        df['deposite']=dep(s)
    except:
        df['deposite']='NA'
    try:
        df['furnished']=style(s)
    except:
        df['furnished']='NA'
    try:
        df['locality']=locality(s)
    except:
        df['locality']='NA'
    try:
        df['Name']=name(s)
    except:
        df['Name']='NA'
    
    return df


# In[70]:


url="https://www.makaan.com/listings?listingType=rent&pageType=CITY_URLS&cityName=Pune&cityId=21&templateId=MAKAAN_CITY_LISTING_BUY"


# In[71]:


dat=[]
df=scrap(url)
dat.append(df)


# In[72]:


url=url+'&page='


# In[73]:


for i in range(2,number_of_pages):
    url=url+str(i)
    print(url)
    df=scrap(url)
    dat.append(df)
    url=url[:-1]
result = pd.concat(dat)


# In[74]:


result.reset_index(inplace = True, drop = True) 


# In[57]:





# In[75]:





# In[76]:


result


# In[78]:


result.to_csv('makkan.csv')


# In[40]:




