
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

dataset = pd.read_csv('C://Users/akilesh/Downloads/weather_nominal.csv')
c = 0
ud = []
p = 1


# In[3]:

dataset


# In[4]:

d = {'Sunny': 1, 'Overcast': 2, 'Rainy': 3}
dataset.Outlook = [d[item] for item in dataset.Outlook.astype(str)]


# In[5]:

type(dataset)


# In[6]:

#d1 is for sunny weather
d1 = dataset[dataset['Outlook'] == 1]
#d2 is for overcast weather
d2 = dataset[dataset['Outlook'] == 2] 
#d3 is for rainy weather
d3 = dataset[dataset['Outlook'] == 3]


# In[7]:

d1
n = d1.columns[0:5]
n = list(n)


# In[8]:

d2


# In[9]:

d3


# In[13]:

def prob_cal(d):
    f = 0
    p = [1]*(len(d))
    c = 0
    z = 0
    k = 1
    ud = []
    ud = list(ud)
    p = list(p)
    
    while k <= 4:
        u = d[n[k]].unique()
        u =list(u)
        lo = d[n[k]]
        lo = list(lo)
        l = len(u)
        while f < l:
            s = u[f]
            f = f+1
            while z < len(lo):
                if lo[z] == s:
                    c = c+1
                    pr = c/len(d)
                    z = z+1
                else:
                    z = z+1
            ud.append(pr)
        #Multiplication of the probabilities with respect to the class of the element(as stated in naive bayes theorem) 
        [ud*p for ud,p in zip(ud,p)]
        p = ud
        k = k+1
    print( "The probability of playing golf in this weather is: ", ud[1]*100, "%")
    
    
             
            
        


# In[14]:

prob_cal(d1)
prob_cal(d2)
prob_cal(d3)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[13]:




# In[14]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



