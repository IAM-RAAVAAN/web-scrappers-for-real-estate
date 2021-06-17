#!/usr/bin/env python
# coding: utf-8

# In[188]:


import pandas as pd 
import numpy as np 
import requests
import csv 
import re
from bs4 import BeautifulSoup


# In[189]:


url='https://www.99acres.com/property-in-ahmedabad-ffid'
j=requests.get(url)
k=j.text
s=BeautifulSoup(k,'lxml')


# In[190]:


def titel(s):
    titel=[]
    link=[]
    #the filter is being applied to filter the neccesary file from the site 
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


# In[191]:


def loc(s):
    location=s.find_all('td',attrs={'class':"list_header_bold srpTuple__spacer10"}) 
    loc=[]
    for i in location:
        loc.append(i.text)
    return loc


# In[192]:


def prices(s):
    prices=s.find_all('td',attrs={'id':"srp_tuple_price"}) 
    k=[]
    for i in prices:
        k.append(i.text)
    return k


# In[193]:


def area(s):
    area=s.find_all('td',attrs={'id':"srp_tuple_primary_area"}) 
    lis_area=[]
    for i in area:
        lis_area.append(i.text)
    #print(lis_area)
    return lis_area
    


# In[194]:


def lis__type(s):
    type=s.find_all('td',attrs={'id':"srp_tuple_bedroom"}) 
    lis__type=[]
    for i in type:
        lis__type.append(i.text)
        #print(i.text)
    return lis__type


# In[195]:


def desc(s):
    desc=s.find_all('div',attrs={'id':"srp_tuple_description"}) 
    lis__desc=[]
    for i in desc:
        lis__desc.append(i.text)
        #print(i.text)
    return lis__desc


# In[196]:


def dates(s):
    date_of=s.find_all('div',attrs={'class':"caption_strong_small"}) 
    date_li=[]
    for i in date_of:
        date_li.append(i.text)
        print(i.text)
    #print(date_li)
    #print(len(date_li))
    return date_li


# In[197]:


def frame(s):
    df=titel(s)
    df['prices']=prices(s)#scrspping the data fro tth prices 
    df['location']=loc(s)#location in the card that is displayed
    df['type']=lis__type(s)
    df['area']=area(s)#area oh the house 
    #df['text']=desc(s)
    try:
        df['dates']=dates(s)#the on which the property was posted o the 99
    except:
        df['dates']='not give'
    df['link']='https://www.99acres.com'+df['link']
    return df


# In[198]:



the_data=frame(s)
the_data.to_csv('99acers2.csv')


# In[12]:





# In[199]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
from time import sleep
the_data_pull=[]
#browser = webdriver.Firefox(executable_path="root/firefox/geckodriver")
browser.get(url)
# element = browser.find_element_by_link_text('Newest First')
# k=element.click()
for i in range(2,3):
    
   
        i=str(i)
        print(i)
        try:
            
            element = browser.find_element_by_link_text(i)
            k=element.click()
            s=BeautifulSoup(browser.page_source,'lxml')
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            s=BeautifulSoup(browser.page_source,'lxml')
            THE_DA=frame(s)
            the_data_pull.append(THE_DA)
        except:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            s=BeautifulSoup(browser.page_source,'lxml')
            THE_DA=frame(s)
            the_data_pull.append(THE_DA)
        # else :
        #         url='https://www.99acres.com/property-for-rent-in-pune-ffid-page-10'               
        #         i=str(i)
        #         print(i)
        #         url=url[:url.index('page')+5]
        #         url=url+i
        #         print(url)
        #         browser.get(url)
        #         s=BeautifulSoup(browser.page_source,'lxml')
        #         THE_DA=frame(s)
                
        #         print(THE_DA.shape)
        #         the_data_pull.append(THE_DA)


        sleep(2)
browser.quit()


# In[200]:


the_data_pull.insert(0,the_data)
result = pd.concat(the_data_pull)


# In[201]:


result.to_csv('hjjolkkjj99acers2.csv')
result.shape


# In[202]:


# for u in result.prices:
#     print(u)


# In[203]:



# result['prices'].apply(lambda x:type(x))


# In[204]:


# result=result.dropna(subset=['prices'])
# k=result['prices'].apply(lambda x: re.sub('[^A-Za-z0-9.]+', ' ', x))


# In[205]:


k


# In[206]:


# j=[]
# for x in k:
#     x=x.split()
#     if 'lacs' in x:
#         x=float(x[0])*100000
#         j.append(x)
#     elif 'Lac' in x:
#         x=float(x[0])*100000
#         j.append(x)
#     elif 'Cr' in x:
#         x=float(x[0])*10000000
#         j.append(x)
#     elif 'lac' in x:
#         x=float(x[0])*100000
#         j.append(x)

#     else:
#         if len(x)==1:
#             try:
#                 x=float(x[0])*100000
#                 j.append(x)
#             except:
#                 x=0
#                 j.append(x)
#         else:
#             x=0
#             j.append(x)
    

# j


# In[207]:


# sum(j)/len(j)


# In[209]:


# sum(kp)/len(kp)


# In[208]:


# kp=[]
# for i in j:
#     if i != 0:
#         kp.append(i)

