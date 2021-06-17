# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import numpy as np
import requests
import csv
import re
from bs4 import BeautifulSoup


# %%
url = 'https://www.99acres.com/flats-for-rent-in-pune-ffid'
j = requests.get(url)
k = j.text
s = BeautifulSoup(k, 'lxml')


# %%
def titel(s):
    titel = []
    link = []
    # the filter is being applied to filter the neccesary file from the site
    titel = s.find_all('a', attrs={'class': "body_med srpTuple__propertyName"})
    for i in titel:
        k = i['href']
        # print(i['href'])
        link.append(k)
        # print(i.text)
    z = []
    for i in titel:
        z.append(i.text)
    d = {
        'link': link,
        'title': z
    }
    df = pd.DataFrame(d)
    return df


# %%
def loc(s):
    location = s.find_all(
        'td', attrs={'class': "list_header_bold srpTuple__spacer10"})
    loc = []
    for i in location:
        loc.append(i.text)
    return loc


# %%
def prices(s):
    prices = s.find_all('td', attrs={'id': "srp_tuple_price"})
    k = []
    for i in prices:
        k.append(i.text)
    return k


# %%
def area(s):
    area = s.find_all('td', attrs={'id': "srp_tuple_primary_area"})
    lis_area = []
    for i in area:
        lis_area.append(i.text)
    return lis_area


# %%
def lis__type(s):
    type = s.find_all('td', attrs={'id': "srp_tuple_bedroom"})
    lis__type = []
    for i in type:
        lis__type.append(i.text)
        # print(i.text)
    return lis__type


# %%
def desc(s):
    desc = s.find_all('div', attrs={'id': "srp_tuple_description"})
    lis__desc = []
    for i in desc:
        lis__desc.append(i.text)
        # print(i.text)
    return lis__desc


# %%
def dates(s):
    date_of = s.find_all('div', attrs={'class': "caption_strong_small"})
    date_li = []
    for i in date_of:
        date_li.append(i.text)
        # print(i.text)
    return date_li


# %%
def frame(s):
    df = titel(s)
    df['prices'] = prices(s)  # scrspping the data fro tth prices
    df['location'] = loc(s)  # location in the card that is displayed
    df['type'] = lis__type(s)
    df['area'] = area(s)  # area oh the house
    # df['text']=desc(s)
    df['dates'] = dates(s)  # the on which the property was posted o the 99
    df['link'] = 'https://www.99acres.com'+df['link']
    return df


# %%
the_data = frame(s)
the_data


# %%


# %%
url = url+'?page='
the_data_pull = []
browser = webdriver.Firefox(
    executable_path=r"C:\Users\swaraj\Desktop\codes\modules\geckodriver-v0.29.1-win64\geckodriver")
browser.get(url)
for i in range(2, 50):
    i = str(i)
    url = url+i
    print(url)
    s = requests.get(url).text
    s = BeautifulSoup(s, 'lxml')
    #k.append(the_data(s))
    url = url[:url.index('=')+1]
    
 
        

    #s = BeautifulSoup(browser.page_source, 'lxml')
    THE_DA = frame(s)
    the_data_pull.append(THE_DA)

    sleep(2)
browser.quit()


# %%
the_data_pull.insert(0, the_data)
result = pd.concat(the_data_pull)


# %%
result.to_csv('hjjolkkjj99acers2.csv')


# %%
