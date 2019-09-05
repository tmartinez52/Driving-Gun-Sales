#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv_path1 = "Resources/Gun Violence Archive 2014.csv"
csv_path2 = "Resources/Gun Violence Archive 2015.csv"
csv_path3 = "Resources/Gun Violence Archive 2016.csv"
csv_path4 = "Resources/Gun Violence Archive 2017.csv"
csv_path5 = "Resources/Gun Violence Archive 2018.csv"
csv_path6 = "Resources/Gun Violence Archive 2019.csv"


# In[3]:


gun_violence2014_df = pd.read_csv(csv_path1)
gun_violence2015_df = pd.read_csv(csv_path2)
gun_violence2016_df = pd.read_csv(csv_path3)
gun_violence2017_df = pd.read_csv(csv_path4)
gun_violence2018_df = pd.read_csv(csv_path5)
gun_violence2019_df = pd.read_csv(csv_path6)


# In[4]:


gun_violence2016_df.insert(0, 'Incident ID', range(50000, 50000 + len(gun_violence2016_df)))
gun_violence2017_df.insert(0, 'Incident ID', range(60000, 60000 + len(gun_violence2017_df)))
gun_violence2018_df.insert(0, 'Incident ID', range(70000, 70000 + len(gun_violence2018_df)))
gun_violence2019_df.insert(0, 'Incident ID', range(80000, 80000 + len(gun_violence2019_df)))


# In[5]:


gun_violence_df=gun_violence2014_df.append(gun_violence2015_df)
gun_violence_df.tail()


# In[6]:


gun_violence_df=gun_violence_df.append(gun_violence2016_df)
gun_violence_df.tail()


# In[7]:


gun_violence_df=gun_violence_df.append(gun_violence2017_df)
gun_violence_df.tail()


# In[8]:


gun_violence_df=gun_violence_df.append(gun_violence2018_df)
gun_violence_df.tail()


# In[9]:


gun_violence_df=gun_violence_df.append(gun_violence2019_df)
gun_violence_df.tail()


# In[10]:


gun_violence_df=pd.DataFrame(gun_violence_df)
gun_violence_df.head()


# In[16]:


gun_violence=gun_violence_df.to_csv("Resources/gun_violence.csv", index=False, header=True)


# In[23]:


csv_path7 = "Resources/Mother Jones_Mass Shootings.csv"
csv_path8 = "Resources/gun_violence.csv"


# In[26]:


gun_violence_df = pd.read_csv(csv_path8)
MJ_massshoot_df = pd.read_csv(csv_path7)


# In[27]:


gun_violenceMJ_df = pd.merge(gun_violence_df, MJ_massshoot_df, on="Incident_ID")
gun_violenceMJ_df.head()


# In[29]:


gun_violenceMJ=gun_violenceMJ_df.to_csv("Resources/gun_violenceMJ.csv", index=False, header=True)


# In[32]:


csv_path9 = "Resources/Mother Jones_Mass Shootings-updated.csv"
csv_path10 = "Resources/gun_violence_updated.csv"
csv_path11 = "Resources/gun_violenceMJ.csv"


# In[33]:


mjmsu_df=pd.read_csv(csv_path9)
gvu_df=pd.read_csv(csv_path10)
gvmj_df=pd.read_csv(csv_path11)


# In[34]:


gun_violenceall_df=mjmsu_df.append(gvu_df)
gun_violenceall_df.tail()


# In[35]:


gun_violenceall_df=gun_violenceall_df.append(gvmj_df)
gun_violenceall_df.head()


# In[36]:


gun_violenceall=gun_violenceall_df.to_csv("Resources/gun_violenceall.csv", index=False, header=True)


# In[ ]:




