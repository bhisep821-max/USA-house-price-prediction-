#!/usr/bin/env python
# coding: utf-8

# ## 06.08.2025

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


import numpy as np
import stats
from scipy.stats import ttest_ind
from scipy.stats import shapiro


# In[37]:


# data=np.array([20,50,50,30,30,10,40,60,90,28])
# data
def cal_stats(data):
    total=sum(data)
    print('Total Sum:', total)
    
    count=len(data)
    print('Total count:', count)
    
    maximum=max(data)
    print('Maximum value:',maximum)
    
    avg=np.mean(data)
    print('Average:' , avg)
    
    median = np.median(data)
    print('Median:',median)
    
    try:
        stats.mode(data)
    except:
        print('No Mode')
    
    ran = max(data)-min(data)
    print('Rang:', ran)
    
    
    
    # percentile
    q1 = np.percentile(data,25)
    print('Quartile 1:',q1)
    
    # q2 = np.percentile(data,50)
    # print('Quartile 2:',q2)
    
    q3 = np.percentile(data,75)
    print('Quartile 3:',q3)
    
    IQR= np.percentile(data,75) -np.percentile(data,25)
    print('IQR:',IQR)
    
    # whisker
    lw=q1-IQR*1.5
    uw=q3+IQR*1.5
    print('Lower Whisker:',lw)
    print('Upper Whisker:',uw)
    
    outlire = q3-q1
    print('outelire:',outlire)
    
    outliers = []
    for i in data:
        if i<lw or i>uw:
            outliers.append(i)
    print(len(outliers))
    
    outliers = len([ i for i in data if i<lw or i>uw])
    print('Number of outliers:',outliers)
    
    very=np.var(data,ddof=1)
    print('Variance:',very)
    
    std_dev=very**0.5
    print('Standard deviation:',std_dev)
    
    lower=avg-1*std_dev
    upper=avg+1*std_dev
    perc=((data>=lower) & (data<=upper)).sum() / count
    print(f'1 standard Deveation range: ({lower:2f} to {upper:2f})-->{perc*100:2f}% of data')
    
    for i in range(1,4):
        lower=avg-i*std_dev
        upper=avg+i*std_dev
        perc=((data>=lower) & (data<=upper)).sum() / count
        print(f'{i} standard Deveation range: ({lower:2f} to {upper:2f})-->{perc*100:2f}% of data')
    
    skew = stats.skewness(data)
    print('Skewness:',skew)
    
    kurt=stats.kurtosis(data)
    print('Kurtosis:',kurt)
    
    stat_val,p_value=shapiro(data)
    if p_value>0.05:
        print('Likely Follows Normal Distribution')
    else:
        print('Likely Dose Not follow Normal Distribution')
    
    standard_error=std_dev/np.sqrt(count)
    for conf, z in [(95,1.95),(97,2.17),(99,2.576)]:
        moe=standard_error*z
        lower=avg+moe
        upper=avg+moe
        print(f'{conf}% confidence interval:{lower:2f},{upper:2f}')

