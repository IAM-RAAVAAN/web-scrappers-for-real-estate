#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import csv
import os
import sys


# In[3]:


os.chdir('/root/working')
# print(i)

#print (os.getcwd())
directory = os.listdir()


# In[41]:


d = {}
fr = []
csv_files = []
for files in directory:
    # print(files)
    if files.endswith(".csv"):
        csv_files.append(files)
        #print(files, "-----------------------")
        f = pd.read_csv(files)

        # print(time.time()-e1234)
        #f['file_name'] = files
        # print(f)
        d[files] = f
        fr.append(f)
        files = files[:files.index('.')]
        ([files])


# In[81]:


d['commonfloor.csv'].columns = ['0', 'area', 'bathrooms', 'text',
                                'link', 'title', 'prices', 'dates', 'owner', 'furnished']
# d['prop.csv'].columns=['0','title','link','text','area','prices']
d['propertywala.csv'].columns = ['0', 'title', 'owner', 'area', 'text', 'link']
d['housing.csv'].columns = ['0', 'prices', 'location',
                            'furnished', 'owner', 'link', 'title', 'area']
d['housing1.csv'].columns = ['0', 'prices', 'location',
                             'furnished', 'owner', 'link', 'title', 'area']

d['sulekha.csv'].columns = ['0', 'title', 'link', 'location', 'text',
                            'text1', 'co-ordinate', 'area', 'prices', 'depo', 'dates', 'owner']
d['sulekha1.csv'].columns = ['0', 'title', 'link', 'location', 'text',
                             'text1', 'co-ordinate', 'area', 'prices', 'depo', 'dates', 'owner']

d['scraped_data.csv'].columns = ['0', 'type', 'prices', 'area',
                                 'link', 'title', 'depo', 'furnished', 'location', 'owner']
d['magicbricks.csv'].columns = ['0', 'text',
                                'owner', 'title', 'prices', 'location']


# In[100]:


# d['99acers.csv']


# In[89]:


f = []
for k in d.keys():
    print(k)
    print(d[k].columns)
    f.append(d[k])


# In[101]:


re = pd.concat(f[1:])


# In[102]:


re


# In[103]:


re = re.drop(['Unnamed: 0', '0', 'names'], axis=1)


# In[104]:


re = re.drop(['place'], axis=1)


# In[107]:


re.to_csv('data_still.csv')


# In[ ]:
