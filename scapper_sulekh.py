#!/usr/bin/env python
# coding: utf-8

# In[111]:


import time
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.options import Options
import pandas as pd
import numpy as np
import requests
import csv
import re
from bs4 import BeautifulSoup
from selenium import webdriver


# In[112]:


def title_link(s):
    tit = []
    link = []
    sta = s.find_all('a', attrs={'class': "bizlinkurl"})
    for k in sta:
        tit.append(k.text)
        link.append(k['href'])
    d = {
        'title_link': tit,
        'links': link
    }
    df = pd.DataFrame(d)
    return df


# In[113]:


def address(s):
    address = []
    sta = s.find_all('div', attrs={'class': "locality"})
    for a in sta:
        address.append(a.text.split()[0])
    return address


# In[114]:


def location(s):
    location = []
    sta = s.find_all('a', attrs={'class': "view-on-map"})
    for a in sta:
        location.append(a['data-latlong'])
    return location


# In[115]:


def prices(s):
    prices = []
    sta = s.find_all('span', attrs={'class': "deposit"})
    for i in sta:
        prices.append(i.text)
    """    sta=s.find_all('span',attrs={'class':"Deposit"})    
    for i in sta:
        prices.append(i.text)"""
    return prices


# In[116]:


def financial(s):
    financial = []
    sta = s.find_all('span', attrs={'class': "price primary"})
    for i in sta:
        financial.append(i.text)
    return financial


# In[117]:


def amenities(s):
    ammenities = []
    sta = s.find_all('div', attrs={'class': "amenities flat"})
    for i in sta:
        ammenities.append(i.text)
    return ammenities


# In[118]:


def spec_flat(s):
    spec_flat = []
    sta = s.find_all('div', attrs={'class': "spec flat"})
    for i in sta:
        spec_flat.append(i.text)
    return spec_flat


# In[119]:


def spec_flat_necce(s):
    spec_flat_necce = []
    sta = s.find_all('div', attrs={'class': "spec icon primary"})
    for i in sta:
        spec_flat_necce.append(i.text)
    return spec_flat_necce


# In[120]:


def the_area(s):
    clean = []
    area = []
    sta = s.find_all('span', attrs={'class': "feature primary"})
    for i in sta:
        area.append(i.text.split())
    for a in area:
        clean.append(" ".join(a[-3:]))
    return clean


# In[121]:


# for a in area:
#     print(" ".join(a[-3:]))


# In[122]:


def dates_bro(s):
    dates_bro = []
    sta = s.find_all('div', attrs={'class': "posted"})
    for i in sta:
        dates_bro.append(i.text)
    return dates_bro


# In[123]:


def the_text(s):
    the_text = []
    sta = s.find_all('span', attrs={'class': "listing-desc view-less"})
    for i in sta:
        the_text.append(i.text)


# In[124]:


url = "https://property.sulekha.com/apartments-flats-for-rent/pune#"
j = requests.get(url)
k = j.text
s = BeautifulSoup(k, 'lxml')


# In[125]:


def the_filter(df):
    the_liost = df['financial']
    prices = []
    deposit = []
    for l in the_liost:
        k = l.split(' ')
        prices.append(k[3])
        deposit.append(k[-4])
    df['prices'] = prices
    df['deposit'] = deposit
    k = df['dates_bro']
    the_posted_dates = []
    details_of = []
    for i in k:
        i = i.strip()
        i = i.split(" ")
        the_posted_dates.append(i[-3:])
        details_of.append(' '.join(i[0:-3]))
    df['the_posted_dates'] = the_posted_dates
    df['details'] = details_of
    df_new = df.drop(['financial',	'dates_bro'], axis=1)
    df_new = df_new.drop(['amenities'], axis=1)
    k = len(df['the_posted_dates'])
    the_date = []
    for i in range(0, k):
        j = df['the_posted_dates'][i]
        the_date.append(" ".join(j))
    df_new['the_posted_dates'] = pd.to_datetime(the_date)
    return df_new


# In[126]:


def data_frames(s):
    df = title_link(s)
    df['adress'] = address(s)
    # df['prices']=prices(s)
    df['financial'] = financial(s)
    df['dates_bro'] = dates_bro(s)
    df['spec_flat'] = spec_flat(s)
    df['spec_flat_necce'] = spec_flat_necce(s)
    df['amenities'] = amenities(s)
    df['location'] = location(s)
    df['area'] = the_area(s)
    df = the_filter(df)
    return df


# In[127]:


# In[128]:
options = Options()
options.headless = True

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
the_data_pull = []
# browser = webdriver.Firefox(executable_path=r"C:\Users\swaraj\Desktop\codes\modules\geckodriver-v0.29.1-win64\geckodriver")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.get(url)
for i in range(2, 7):
    i = str(i)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    try:
        element = browser.find_element_by_link_text("View More")
        k = element.click()
    except:
        pass

    # j=requests.get(browser.page_source)
    # k=j.text
    s = BeautifulSoup(browser.page_source, 'lxml')
    THE_DA = data_frames(s)
    the_data_pull.append(THE_DA)

    sleep(2)



# In[129]:


df = pd.concat(the_data_pull)


# In[130]:


df['links'] = df['links'].apply(lambda x: 'https://property.sulekha.com'+x)


# In[131]:


df


# In[133]:


df.to_csv(r"C:\Users\swaraj\Desktop\codes\modules\working\sulekha.csv")


# In[ ]:
