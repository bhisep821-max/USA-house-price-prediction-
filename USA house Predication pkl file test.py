#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import stats
from scipy.stats import ttest_ind
from scipy.stats import shapiro
import warnings
warnings.filterwarnings('ignore')


# In[1]:


import joblib
lr=joblib.load('USA house price pred model 100k rnse 25.08.2025.pkl')


# In[2]:


lr


# In[5]:


income=float(input('what is your income'))
age=float(input('what is your age'))
rooms=float(input('what is your number of rooms'))
bedroom=float(input('what is your number of bedrooms'))
pop=float(input('what is your area population'))
user_input=np.array([income,age,rooms,bedroom,pop])
hose_price_pred=lr.predict(user_input.reshape(1,-1))
print(f'Your house can be sold between ${round(hose_price_pred[0])-50000} to $ {round(hose_price_pred[0])+50000}')


# In[ ]:




