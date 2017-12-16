
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

# We can load any dataset and pass it in 
# the function find_unique_first_column:
dataset = pd.read_csv('C://Users/akilesh/Downloads/weather_nominal.csv')
PA_B = []
PB_A = []


# In[3]:


# Finding P(A|B):
# This code is independennt of text or numeric
def prob_cal(d,P):
    f = 0
    p = [1]*(len(d))
    c = 0
    z = 0
    k = 1
    ud = []
    ud = list(ud)
    p = list(p)
    n = d.columns[0:len(d.columns)]
    n = list(n)
    while k < len(d.columns):
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
        # Multiplication of the probabilities with respect to the 
        # class of the element(as stated in naive bayes theorem): 
        [ud*p for ud,p in zip(ud,p)]
        p = ud
        k = k+1
    print ("The probability of playing golf in this weather is: ",
          ud[1]*100, "%")
    P.append(ud[1])
    return P


# In[4]:


def find_unique_first_column(d,P):
    i = 0
    j = 0
    col_element = d.iloc[:,0].unique()
    col_element = list(col_element)
    col_unique = []
    while j < len(col_element):
        while i < len(d):
            if col_element[j] == d.iloc[i,0]:
                col_unique.append(d.iloc[i,:])
                print(col_unique)
                i = i+1
            else:
                i = i+1
        col_unique = pd.DataFrame(col_unique)
        prob_cal(col_unique, P)
        col_unique = []
        i = 0
        j = j+1
        
# for finding P(B|A)
def p_b_a(d,P):
    d1 = d
    c = d.columns
    d1[[c[0], c[len(d.columns)-1]]] = d1[[c[len(d.columns)-1], c[0]]]
    find_unique_first_column(d1, P)
    
    
        


# In[6]:


# Calculate P(A)
def P_a(d):
    P_a = []
    count_a = 0
    i = 0
    j = 0
    col_element = d.iloc[:,0].unique()
    col_element = list(col_element)
    while j < len(col_element):
        while i < len(d):
            if col_element[j] == d.iloc[i,0]:
                count_a = count_a + 1
                i = i+1
            else:
                i = i+1
        P_a.append(count_a/len(d))
        j = j+1
        i = 0
    return P_a

# Calculate P(B)
def P_b(d):
    P_b = []
    count_b = 0
    i = 0
    j = 0
    col_element = d.iloc[:,len(d.columns) - 1].unique()
    col_element = list(col_element)
    while j < len(col_element):
        while i < len(d):
            if col_element[j] == d.iloc[i,len(d.columns)-1]:
                count_b = count_b + 1
                i = i+1
            else:
                i = i+1
        P_b.append(count_b/len(d))
        j = j+1
        i = 0
    return P_b


            
            
        
        
        
    


# In[ ]:


def overall_prob(P):
    i = 0
    s = 1
    while i < len(P):
        P[i] = P[i]*s
        s = P[i]
        i = i+1
    P = []    
    P = s
    return P
        


# In[ ]:

set_p = [PA_B, PB_A, P_a(dataset), P_b(dataset)] 

# check accuracy P(A|B)={P(B|A)*P(A)}/{P(B)}
def find_accuracy(s):
    Acc = overall_prob(PA_B)/(overall_prob(PB_A)
      *overall_prob(P_a(dataset))/overall_prob(P_b(dataset)))*100
    print ('Test Accuracy:' , Acc, '%')
    return Acc


find_unique_first_column(dataset, PA_B)
p_b_a(dataset, PB_A)
find_accuracy(set_p)


