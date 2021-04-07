# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests 
import re
from bs4 import BeautifulSoup
import pandas as pd


# %%
number_of_pages=3


# %%

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

    k=[]
    for i in range(0,len(l),3):
        k.append(l[i:i+3])
    return k


# %%
def tit_text(s):
  title=s.find_all('a',attrs={'class':"typelink"}) #titles 
  k=[]
  k1=[]
  for a in title:
      k.append( a['href'])
      k1.append(a.text)##links and name that appers
  return k,k1


# %%
def style(s):
    sta=s.find_all('td',attrs={'class':"val"}) 
    k=[]
    for si in sta:
        k.append(si.text)
    return k


# %%
def dep(s):
    detail=s.find_all('li',attrs={'title':"deposit"}) 
    k=[]
    for d in detail:
        k.append(d.text)
    return k


# %%



# %%
def scrap(url):
    j=requests.get(url)
    k=j.text
    s=BeautifulSoup(k,'lxml')
    print()
    col=['BHK','PRICE','AREA']
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
    
    return df


# %%
url="https://www.makaan.com/listings?listingType=rent&pageType=CITY_URLS&cityName=Pune&cityId=21&templateId=MAKAAN_CITY_LISTING_BUY"


# %%
dat=[]
df=scrap(url)
dat.append(df)


# %%
url=url+'&page='


# %%
for i in range(2,number_of_pages):
    url=url+str(i)
    df=scrap(url)
    dat.append(df)
result = pd.concat(dat)


# %%
result.reset_index(inplace = True, drop = True) 


# %%
result.to_csv('scraped_data.csv')


# %%



