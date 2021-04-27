# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
import numpy as np 
import requests
import csv 
import re
from bs4 import BeautifulSoup


# %%
url='https://www.99acres.com/search/property/rent/pune?city=19&class=O&preference=R&area_unit=1&budget_min=0&res_com=R'
j=requests.get(url)
k=j.text
s=BeautifulSoup(k,'lxml')


# %%
def titel(s):
    titel=[]
    link=[]
    titel=s.find_all('a',attrs={'class':"body_med srpTuple__propertyName"}) 
    for i in titel:
        k=i['href']
        #print(i['href'])
        link.append(k)
        #print(i.text)
    z=[]
    for i in titel:
       z.append(i.text)
    d={
    'link':link,
    'title':z
     }
    df=pd.DataFrame(d)
    return df


# %%
def loc(s):
    location=s.find_all('td',attrs={'class':"list_header_bold srpTuple__spacer10"}) 
    loc=[]
    for i in location:
        loc.append(i.text)
    return loc


# %%
def prices(s):
    prices=s.find_all('td',attrs={'id':"srp_tuple_price"}) 
    k=[]
    for i in prices:
        j=i.text
        j=j.split(' ')
        k.append(j[1])
    return k


# %%
def area(s):
    area=s.find_all('td',attrs={'id':"srp_tuple_primary_area"}) 
    lis_area=[]
    for i in area:
        j=i.text
        j=j.split(" ")
        lis_area.append(j[0])
    return lis_area
    


# %%
def lis__type(s):
    type=s.find_all('td',attrs={'id':"srp_tuple_bedroom"}) 
    lis__type=[]
    for i in type:
        lis__type.append(i.text)
        #print(i.text)
    return lis__type


# %%
def desc(s):
    desc=s.find_all('div',attrs={'id':"srp_tuple_description"}) 
    lis__desc=[]
    for i in desc:
        lis__desc.append(i.text)
        #print(i.text)
    return lis__desc


# %%
def dates(s):
    date_of=s.find_all('div',attrs={'class':"caption_strong_small"}) 
    date_li=[]
    for i in date_of:
        date_li.append(i.text)
        #print(i.text)
    return date_li


# %%
def names(s):
    name=s.find_all('div',attrs={'class':"list_header_semiBold"}) 
    name_l=[]
    for i in name:
        name_l.append(i.text)
    return  name_l[13:-8]


# %%
def owners(s):
    owner=s.find_all('div',attrs={'class':"caption_strong_small"}) 
    owner_l=[]
    for i in owner:
        owner_l.append(i.text)
    return owner_l


# %%



# %%
def frame(s):
    df=titel(s)
    df['prices']=prices(s)
    df['location']=loc(s)
    df['place']=df.title.apply(lambda x: x[x.index('in'):])
    df['type']=lis__type(s)
    df['area']=area(s)
    #df['text']=desc(s)
    df['dates']=dates(s)
    df['link']='https://www.99acres.com'+df['link']
    #df['owners']=owners(s)
    df['names']=names(s)
    return df


# %%
frame(s).to_csv(r'C:\Users\swaraj\Desktop\codes\working\99acers2_pa.csv')


# %%
"""the_data=frame(s)
the_data
the_data['owners']=owner_l
the_data['owners']=the_data['owners'].apply(lambda x:x[x.index('by'):].strip())
the_data['owners']"""


# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
the_data_pull=[]
browser = webdriver.Firefox(executable_path="/home/swaraj/Downloads/driver/geckodriver")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.get(url)
for i in range(2,7):
    i=str(i)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = browser.find_element_by_link_text(i)
    k=element.click()
    
    #j=requests.get(browser.page_source)
    #k=j.text
    s=BeautifulSoup(browser.page_source,'lxml')
    THE_DA=frame(s)
    the_data_pull.append(THE_DA)

    sleep(2)
browser.quit()


# %%
"""    browser = webdriver.Firefox(executable_path="/home/swaraj/Downloads/driver/geckodriver")
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element = browser.find_element_by_link_text('2')
    j=element.click()
    print(browser.page_source.encode('utf-8'))"""
    
   


# %%
k


# %%
the_data_pull.insert(0,the_data)
result = pd.concat(the_data_pull)


# %%
result.to_csv('/run/media/swaraj/volume y/code/work/working/99acers2.csv')


# %%
len(the_data_pull)


