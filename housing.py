#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxOptions
import pandas as pd 
import numpy as np 
import csv 
from bs4 import BeautifulSoup 
import requests


# In[2]:


url='https://housing.com/rent/search-M2P2r4v3l939lxd541t'
j=requests.get(url)
k=j.text
s=BeautifulSoup(k,'lxml')


# In[3]:


def price(s):
    prices=[]
    price=s.find_all('div',attrs={'class':"css-1cxwewr"})
    for p in price:
        prices.append(p.text) 
    return prices


# In[4]:



def titles(s):
    title=[]
    titles=s.find_all('div',attrs={'class':"css-ybv4ci"})
    for p in titles:
        title.append(p.text) 
    return title


# In[5]:


def location(s):
    loca=[]
    location=s.find_all('div',attrs={'class':"css-1o3sqfg"})
    for p in location:
        loca.append(p.text) 
    return loca


# In[6]:


def furnished(s):
    fur=[]
    furni=s.find_all('div',attrs={'class':"css-14teu4h"})
    for p in furni:
        fur.append(p.text) 
    return fur


# In[7]:


def contac(s):
    own=[]
    o=s.find_all('div',attrs={'class':"css-wni7av"})
    for p in o:
        own.append(p.text)
    return own 


# In[8]:


def link(s):
    l=[]
    o=s.find_all('a',attrs={'class':"css-1ym6yxe"})
    url='https://housing.com'
    for p in o:
            l.append(url+p['href'])
    return l


# In[9]:


d={
    'prices' : price(s),
    'locations':location(s),
    'furnishde':furnished(s),
    'the_own':contac(s),
    'links':link(s),
    'title':titles(s)

}
df=pd.DataFrame(d)


# In[10]:


def the_funki(s):
    d={
    'prices' : price(s),
    'locations':location(s),
    'furnishde':furnished(s),
    'the_own':contac(s),
    'links':link(s),
    'title':titles(s)

    }
    df=pd.DataFrame(d)
    return df


# In[11]:


from selenium import webdriver


options = Options()
options.headless = True

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)


from time import sleep
the_data_pull=[]
#browser = webdriver.Firefox(executable_path=r"C:\Users\swaraj\Desktop\codes\modules\geckodriver-v0.29.1-win64\geckodriver")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.get(url)
for i in range(2,7):
    i=str(i)
    print(i)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    
    #j=requests.get(browser.page_source)
    #k=j.text
    s=BeautifulSoup(browser.page_source,'lxml')
    THE_DA=the_funki(s)
    the_data_pull.append(THE_DA)

    sleep(2)
browser.quit()


# In[12]:



f=pd.concat(the_data_pull)


# In[13]:


f
f['area']=f['furnishde'].apply(lambda x:x[x.index('d')+1:])
f['furnishde']=f['furnishde'].apply(lambda x:x[:x.index('d')+1])


# In[14]:


f


# In[15]:


f.to_csv(r'C:\Users\swaraj\Desktop\codes\housing.csv')


# In[ ]:




