
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

from sklearn import datasets


# In[3]:

myirisdata=datasets.load_iris()


# In[6]:

myirisdata.data.shape


# In[7]:

myirisdata.data


# In[8]:

myirisdata.keys()


# In[9]:

myirisdata.target


# In[11]:

myirisdata.target.shape


# In[12]:

myirisdata.feature_names


# In[13]:

myirisdata.target_names


# In[14]:

myirisdata.DESCR


# In[15]:

X_input=myirisdata.data


# In[17]:

Y_target=myirisdata.target


# In[18]:

X_input.shape


# In[19]:

Y_target.shape


# In[20]:

X_input_train=X_input[:-10]


# In[21]:

X_input_train.shape


# In[22]:

X_input_test=X_input[-10:]


# In[23]:

X_input_test.shape


# In[24]:

Y_target_train=Y_target[:-10]


# In[25]:

Y_target_train.shape


# In[26]:

Y_target_test=Y_target[-10:]


# In[27]:

Y_target_test.shape


# In[30]:

from sklearn.neighbors import KNeighborsClassifier


# In[31]:

myknn=KNeighborsClassifier()


# In[32]:

mymodel=myknn.fit(X_input_train,Y_target_train)


# In[37]:

YA=Y_target_test


# In[38]:

YA


# In[39]:

YP=mymodel.predict(X_input_test)


# In[40]:

YP


# In[41]:

YA-YP


# In[45]:

from sklearn import metrics


# In[46]:

metrics.accuracy_score(YA,YP)


# In[47]:

m=metrics.accuracy_score(YA,YP)


# In[48]:

n=m*100


# In[49]:

n


# In[ ]:



