
# coding: utf-8

# In[10]:

import pandas as pd
import numpy as np
import arff
from sklearn.model_selection import train_test_split


# In[2]:


# We can use any of the datasets below:
# dataset = arff.load(open('C: // Users / akilesh / Desktop
#                        / Nsu big data books / weather.nominal.arff',
#                        'r', encoding="utf-8")) 
dataset = arff.load(open('C:/Users/akilesh/Desktop/Nsu big data books/soybean.arff','r', encoding="utf-8"))
attrs = dataset['attributes']
dataset = pd.DataFrame(dataset['data']).dropna()
dataset = np.array(dataset)

# In[4]:
def prepare_dataset(dataset):
    no_col = len(dataset[0, :]) - 1
    attrslen = len(attrs)
    datalabels = dataset[:, (attrslen - 1)]
    datafeatures = dataset[:, 0:(attrslen - 1)]
    return no_col, datalabels, datafeatures   


# In[5]:


# split the dataset into 4 parts:
def split_dataset(datafeatures, datalabels):
    f_train, f_test, l_train, l_test = train_test_split(datafeatures, 
                                                    datalabels, 
                                                    test_size=0.3, 
                                                    random_state=100)
    return f_train, f_test, l_train, l_test

def Naive_Bayes_Classifier(dataset):
    feature_prob = {}
    count = 0
    true_prediction = 0
    no_col, datalabels, datafeatures = prepare_dataset(dataset)
    f_train, f_test, l_train, l_test = split_dataset(datafeatures, datalabels)
    for i in range(len(f_test)):
        for j in range(len(f_train)):
            if f_test[i, 0] == f_train[j, 0]:
                for z in range((no_col)):
                    if f_test[i, z] == f_train[j, z]:
                        count = count+1
                count = count/(len(f_train[0, :]))
                feature_prob.update({j: count})
                count = 0
        # Find the row with has the highest probabilistic match (m)
        # In this case we consider the l_train[m] is the predicted label
        m = max(feature_prob.keys(), key=(lambda key: feature_prob[key]))
        feature_prob = {}
        # Check the true test label with the predicted label:
        if l_train[m] == l_test[i]:
                true_prediction = true_prediction+1
    Acc = true_prediction/len(l_test)
    print ("The accuracy of this model is:", Acc*100, "%")
        

Naive_Bayes_Classifier(dataset)



# In[ ]:





# In[ ]:



