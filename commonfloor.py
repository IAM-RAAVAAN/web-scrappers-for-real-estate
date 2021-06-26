#!/usr/bin/env python
# coding: utf-8

# In[57]:


import datetime
import pandas as pd
import numpy as np
import re
import requests
import selenium
import csv
import urllib
from bs4 import BeautifulSoup
import logging
logging.basicConfig(filename='comn', level=logging.DEBUG,
                    format='%(levelname)s:%(message)s:%(asctime)s')
logging.debug('comn fired')

# In[58]:


tod = datetime.datetime.now().date()


d = datetime.timedelta(days=50)
a = tod - d
logging.debug(a)


# In[59]:


url = 'https://www.commonfloor.com/pune-property/for-rent'
s = requests.get(url).text
s = BeautifulSoup(s, 'lxml')


# In[60]:


def head(s):
    head1 = []
    head = s.find_all('h2')
    for i in head:
        head1.append(i.text)
    return head1


# In[61]:


def link(s):
    lin = []
    for a in s.select("h2 > a"):
        lin.append(a['href'])
    return lin


# In[62]:


def owner(s):

    posters = []
    poster = s.find_all('div', attrs={'class': 'infownertext'})
    for i in poster:
        posters.append(i.text.split())
    return posters


# In[63]:


def prices(s):
    price = []
    pric = s.find_all('span', attrs={'class': 's_p'})
    for i in pric:
        price.append(i.text)
    return price


# In[64]:


def info(s):
    info = []
    inf = s.find_all('div', attrs={'class': 'inforow pull-left graybg'})
    for i in inf:
        info.append(i.text.split())
    area = []
    for i in info:
        area.append(i[2])
    inform = []
    for i in info:
        inform.append(i[6:-1])
    bath = []
    for i in info:
        bath.append(i[-1])
    the_details = []
    for i in inform:
        the_details.append(i[:-1])
    return area, bath, the_details


# In[65]:


def date(s):
    dates = []
    dat = s.find_all('div', attrs={'class': 'posteddate'})
    for i in dat:
        dates.append(i.text[8:])
    return dates


# In[66]:


# areas,bathroom,others=info(s)
# link=link(s)
# header=head(s)[1:-1]
# price=prices(s)


# In[67]:


# d={
#     'areas':areas,
#     'bathroom':bathroom
# }

# df=pd.DataFrame(d)


# In[68]:


# df['other']=others
# df['links']=link
# df['header']=header
# df['prices']=price
# df['other']=df['other'].apply(lambda x:" ".join(x))
# df['date']=date(s)
# df['date']=df['date'].apply(lambda x: re.sub(r"\D","",x))
# df['owner']=owner(s)
# df['owner']=df['owner'].apply(lambda x: x[2:])
# df['owner']=df['owner'].apply(lambda x: " ".join(x))
# df


# In[69]:


def the_data(s):

    areas, bathroom, others = info(s)
    # print(link(s))
    l = link(s)
    header = head(s)
    price = prices(s)
    d = {
        'areas': areas,
        'bathroom': bathroom
    }

    df = pd.DataFrame(d)
    df['other'] = others
    # print(links)
    df['links'] = l
    df['header'] = header
    df['prices'] = price
    df['other'] = df['other'].apply(lambda x: " ".join(x))
    df['date'] = date(s)
    df['date'] = df['date'].apply(lambda x: x.strip())
    df['owner'] = owner(s)
    df['owner'] = df['owner'].apply(lambda x: x[2:])
    df['owner'] = df['owner'].apply(lambda x: " ".join(x))
    df['links'] = df['links'].apply(lambda x: 'https://www.commonfloor.com/'+x)

    return df


# In[70]:


url = url+'?page='
k = []
for i in range(2, 4):
    i = str(i)
    url = url+i
    logging.debug(url)
    s = requests.get(url).text
    s = BeautifulSoup(s, 'lxml')
    k.append(the_data(s))
    url = url[:-1]

df = pd.concat(k)
dates_of = []
for d in df['date']:
    if d == 'Today':
        dates_of.append(t)
    else:
        d = re.sub(r"\D", " ", str(d))
        d = int(d)
        # print(d)
        temp = datetime.timedelta(days=d)
        a = tod - temp
        dates_of.append(a)

df['date'] = dates_of
fur = []
for head in df['header']:
    if 'Furnished' in head:
        head = head.split(' ')
        st = head[:head.index('Furnished')+1]

        st = ' '.join(st)
        fur.append(st)
    else:
        fur.append(" ")
df['furnished'] = fur

the_head = []
for head in df['header']:
    if 'Furnished' in head:
        head = head.split(' ')
        del head[:head.index('Furnished')+1]
        head = " ".join(head)
        the_head.append(head)
    else:
        the_head.append(head)
df['header'] = the_head


# In[74]:


df


# In[76]:

logging.debug('-------------cmn file stored---------------------')
df.to_csv("commonfloor.csv")


# In[ ]:
