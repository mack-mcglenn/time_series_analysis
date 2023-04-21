#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sb
import statsmodels.api as sm
import env
import warnings
warnings.filterwarnings('ignore')
import os
#


# In[5]:


# Store data

def connect(db):
    
    """This function will pull the information from my env file (username, password, host,
    database) to connect to Codeup's MySQL database"""
    
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def get_store_data():
    q = """ Select * from items
            join sales using(item_id)
            join stores using(store_id)"""
    
    df = pd.read_sql(q, connect('tsa_item_demand'))
    
    return df

def wrangle_store_data():
    file= 'tsa_item_demand.csv'
    
    if os.path.isfile(file):
        df= pd.read_csv(file)
    else:
        df= get_store_data()
        
    return df

