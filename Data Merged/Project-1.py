#!/usr/bin/env python
# coding: utf-8

# In[129]:


import pandas as pd
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd


# In[32]:


get_ipython().run_line_magic('autosave', '0')


# In[33]:


#Pulled gun violence data from each year on the Gun Violence Archive
csv_path1 = "Resources/Gun Violence Archive 2014.csv"
csv_path2 = "Resources/Gun Violence Archive 2015.csv"
csv_path3 = "Resources/Gun Violence Archive 2016.csv"
csv_path4 = "Resources/Gun Violence Archive 2017.csv"
csv_path5 = "Resources/Gun Violence Archive 2018.csv"
csv_path6 = "Resources/Gun Violence Archive 2019.csv"


# In[34]:


gun_violence2014_df = pd.read_csv(csv_path1)
gun_violence2015_df = pd.read_csv(csv_path2)
gun_violence2016_df = pd.read_csv(csv_path3)
gun_violence2017_df = pd.read_csv(csv_path4)
gun_violence2018_df = pd.read_csv(csv_path5)
gun_violence2019_df = pd.read_csv(csv_path6)


# In[4]:


#Created Incident IDs for each year
gun_violence2016_df.insert(0, 'Incident ID', range(50000, 50000 + len(gun_violence2016_df)))
gun_violence2017_df.insert(0, 'Incident ID', range(60000, 60000 + len(gun_violence2017_df)))
gun_violence2018_df.insert(0, 'Incident ID', range(70000, 70000 + len(gun_violence2018_df)))
gun_violence2019_df.insert(0, 'Incident ID', range(80000, 80000 + len(gun_violence2019_df)))


# In[5]:


#appended 2014 data to 2015 data
gun_violence_df=gun_violence2014_df.append(gun_violence2015_df)
gun_violence_df.tail()


# In[6]:


#appended 2016 data to 2014 and 2015 data
gun_violence_df=gun_violence_df.append(gun_violence2016_df)
gun_violence_df.tail()


# In[7]:


#appended 2017 data to the remainder of the data (2014, 2015, 2016)
gun_violence_df=gun_violence_df.append(gun_violence2017_df)
gun_violence_df.tail()


# In[8]:


#appended 2018 data to the remainder of the data (2014, 2015, 2016, 2017)
gun_violence_df=gun_violence_df.append(gun_violence2018_df)
gun_violence_df.tail()


# In[9]:


#appended 2019 data to the remainder of the data (2014, 2015, 2016, 2017, 2018)
gun_violence_df=gun_violence_df.append(gun_violence2019_df)
gun_violence_df.tail()


# In[10]:


#Created a dataframe from all years of the data
gun_violence_df=pd.DataFrame(gun_violence_df)
gun_violence_df.head()


# In[16]:


#wrote the data to a csv file
gun_violence=gun_violence_df.to_csv("Resources/gun_violence.csv", index=False, header=True)


# In[23]:


#pulled Mother Jones Mass shooting data and gun violence archives data
csv_path7 = "Resources/Mother Jones_Mass Shootings.csv"
csv_path8 = "Resources/gun_violence.csv"


# In[26]:


gun_violence_df = pd.read_csv(csv_path8)
MJ_massshoot_df = pd.read_csv(csv_path7)


# In[27]:


#Merged the gun violence data with Mother Jones Mass shooting data 
gun_violenceMJ_df = pd.merge(gun_violence_df, MJ_massshoot_df, on="Incident_ID")
gun_violenceMJ_df.head()


# In[29]:


#Wrote the file to a csv file
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


# In[5]:


gun_violenceall=gun_violenceall_df.to_csv("Resources/gun_violenceall.csv", index=False, header=True)


# In[4]:


csv_path_gunsales = "Resources/gun_sales_cleaned.csv"


# In[5]:


gunsales_csv=pd.read_csv(csv_path_gunsales)


# In[6]:


#looked at gun sales by state groupby state
gunsales_grpstate1_df=gunsales_csv.groupby(["state"])
gunsales_grpstate1_df=gunsales_grpstate1_df.sum()
gunsales_grpstate1_df.head()


# In[7]:


gunsales_grpstate1_df.columns


# In[8]:


gunsales_grpstate1_df=gunsales_grpstate1_df.reset_index()
gunsales_grpstate1_df.head()


# In[9]:


gunsales_bystate_df=pd.DataFrame(gunsales_grpstate1_df)
gunsales_bystate_df.head()


# In[10]:


# Removed unecessary columns
gunsales_bystate_df=gunsales_bystate_df.drop(['monthyr_num', 'returned_handgun', 'returned_long_gun', 'returned_other', 'Year'], axis=1)
gunsales_bystate_df.head()


# In[11]:


csv_path_pop = "Resources/us_population2016_data.csv"


# In[12]:


uspop2016_csv=pd.read_csv(csv_path_pop)
uspop2016_csv.head()


# In[14]:


#Merged in population data into gun sales data
gunsales_bystatepop_df=pd.merge(gunsales_bystate_df, uspop2016_csv, on="state", how="outer")
gunsales_bystatepop_df.head()


# In[15]:


gunsales_bystatepop_df=gunsales_bystatepop_df.drop([11, 21, 49])


# In[16]:


gunsales_bystatepop_df


# In[17]:


gunsales_bystatepop_df.dtypes


# In[18]:


gunsales_bystatepop_df['pop_estimate_2016']=gunsales_bystatepop_df['pop_estimate_2016'].str.replace(",","").astype(float)
gunsales_bystatepop_df['pop_estimate_2016']


# In[103]:


gunsales_bystatepop_df["percentage_gunpurchase"] = (gunsales_bystatepop_df["Total Sales"]/gunsales_bystatepop_df["pop_estimate_2016"])*100
gunsales_bystatepop_df["percentage_gunpurchase"]


# In[19]:


gunsales_bystatepop_df=pd.DataFrame(gunsales_bystatepop_df)
gunsales_bystatepop_df.head()


# In[20]:


gunsales_bystatepop_df=gunsales_bystatepop_df.to_csv("Resources/gunsales_bystatepop_df.csv", index=False, header=True)


# In[21]:


csv_path_gunsales = "Resources/gun_sales_cleaned.csv"
gunsales_csv=pd.read_csv(csv_path_gunsales)
gunsales_csv.head()


# In[22]:


#Grouped the gunsales data by month year variable
gunsales_grpstate2_df=gunsales_csv.groupby(["monthyr_num"])
gunsales_grpstate2_df=gunsales_grpstate2_df.sum()
gunsales_grpstate2_df.head()


# In[23]:


gunsales_grpstate2_df=gunsales_grpstate2_df.reset_index()
gunsales_grpstate2_df.head()


# In[24]:


gunsales_grpstate2_df=pd.DataFrame(gunsales_grpstate2_df)
gunsales_grpstate2_df.head()


# In[25]:


gunsales_grpstate3_df=gunsales_grpstate2_df.drop(['handgun', 'long_gun', 'other','multiple','returned_handgun', 'returned_long_gun', 'returned_other', 'Year'], axis=1)
gunsales_grpstate3_df.head()


# In[26]:


gunsales_grpstate3_df=pd.DataFrame(gunsales_grpstate3_df)
gunsales_grpstate3_df.head()


# In[27]:


gunsales_grpstate_df =gunsales_grpstate3_df.to_csv("Resources/gunsales_grpdate_df.csv", index=False, header=True)


# In[28]:


csv_path1_mj = "Resources/mj_cleaned.csv"
mj_clean_df=pd.read_csv(csv_path1_mj)
mj_clean_df


# In[29]:


mj_clean3_df = mj_clean_df[mj_clean_df['MJ_total_victims']>=5]


# In[30]:


mj_clean3_df


# In[31]:


gunsales_clean3_df=mj_clean3_df.to_csv("Resources/mj_clean3_df.csv", index=False, header=True)


# In[32]:


csv_path_gtrends = "Resources/2014-2019-07-31_GTrends.csv"
gtrends_clean_df=pd.read_csv(csv_path_gtrends)
gtrends_clean_df.head()


# In[33]:


gtrends_mean=gtrends_clean_df["Relative Value"].mean()
gtrends_mean


# In[34]:


gtrends_std=gtrends_clean_df["Relative Value"].std()
gtrends_std


# In[35]:


gtrends_std_half=gtrends_std/2
gtrends_std_half


# In[36]:


gtrends_cut_score=gtrends_mean-gtrends_std_half
gtrends_cut_score


# In[37]:


#Chose to use those only spikes in Google Trends for the word "shooting" that were 1/2 of a standard deviation below the mean in relative value. 

gtrends_clean1_df = gtrends_clean_df[gtrends_clean_df['Relative Value']>=23]
gtrends_clean1_df


# In[38]:


gtrends_clean1_df=pd.DataFrame(gtrends_clean1_df)
gtrends_clean1_df.head()


# In[39]:


gtrends_clean1_df.dtypes


# In[40]:


gtrends_clean1_df['Month']=gtrends_clean1_df['Month'].str.replace('-','').astype(float)
gtrends_clean1_df['Month']


# In[41]:


gtrends_clean1_df['Month']=gtrends_clean1_df['Month'].astype(int)


# In[42]:


gtrends_clean1_df.head()


# In[43]:


gtrends_clean1_df =gtrends_clean1_df.to_csv("Resources/gtrends_clean1_df.csv", index=False, header=True)


# In[44]:


csv_path2_mj="Resources/mj_clean3_df.csv"
mj_clean4_df=pd.read_csv(csv_path2_mj)
mj_clean4_df


# In[45]:


mj_clean4_df["MJ_date"] = pd.to_datetime(mj_clean4_df["MJ_date"]).dt.strftime("%Y%m%d")
mj_clean4_df["MJ_date"]


# In[46]:


mj_clean4 =mj_clean4_df.to_csv("Resources/mj_clean4.csv", index=False, header=True)


# In[47]:


mj_clean4_df["MJ_date"] =mj_clean4_df["MJ_date"].astype(int)


# In[49]:


mj_clean5_df=mj_clean4_df["MJ_date"].floordiv(100)
mj_clean5_df


# In[50]:


mj_clean5 =mj_clean5_df.to_csv("Resources/mj_clean5.csv", index=False, header=True)


# In[51]:


# Reading all of the clean csv files
mj_shoot_path1 = "Resources/mj_clean5.csv"
gtrends_path2 = "Resources/gtrends_clean1_df.csv"
gunsales_path3 = "Resources/gunsales_grpdate_df.csv"
mj_shoot_path4="Resources/mj_clean3_df.csv"


# In[52]:


mj_date_df = pd.read_csv(mj_shoot_path1)
gtrends_df = pd.read_csv(gtrends_path2)
gunsales_df = pd.read_csv(gunsales_path3)
mj_shoot5_df=pd.read_csv(mj_shoot_path4)


# In[53]:


mj_date_df=pd.DataFrame(mj_date_df)
mj_date_df.head()


# In[54]:


mj_date_df=mj_date_df.rename(columns={"MJ_date": "monthyr_num"})
mj_date_df.head()


# In[55]:


mj_shoot5_df=pd.DataFrame(mj_shoot5_df)
mj_shoot5_df.head()


# In[56]:


mj_shoot8_df = pd.concat([mj_date_df, mj_shoot5_df], axis=1)
mj_shoot8_df.head()


# In[57]:


mj_shoot10_df=mj_shoot8_df.drop(['case', 'MJ_location', 'summary','MJ_fatalities','MJ_injured', 'MJ_loc_type', 'shooter_gender', 'sources','mental_health_sources', 'sources_additional_age','latitude', 'longitude', 'shooting_type','MJ_year','city','state','age_of_shooter', 'prior_signs_mental_health_issues', 'mental_health_details','weapons_obtained_legally','where_obtained', 'weapon_type', 'weapon_details', 'shooter_race'], axis=1)
mj_shoot10_df.head()


# In[58]:


mj_shoot10_df=mj_shoot10_df.drop(['MJ_date'], axis=1)
mj_shoot10_df.head()


# In[59]:


mj_shoot10_df=pd.DataFrame(mj_shoot10_df)
mj_shoot10_df.head()


# In[60]:


monthyr_counts=mj_shoot10_df["monthyr_num"].value_counts()
monthyr_counts.head()


# In[61]:


mjgrp_monthyr_df=mj_shoot10_df.groupby(['monthyr_num'])
mjgrp_monthyr_df.count().head


# In[62]:


total_victims=mjgrp_monthyr_df["MJ_total_victims"].sum()
total_victims.head()


# In[63]:


mj_shoot11_df=pd.DataFrame({"Number of Incidents":monthyr_counts, "Total Number of Victims in Month":total_victims})
mj_shoot11_df.head()


# In[64]:


mj_shoot11_df=mj_shoot11_df.reset_index()
mj_shoot11_df.head()


# In[65]:


mj_shoot12_df=mj_shoot11_df.rename(columns={"index": "monthyr_num"})
mj_shoot12_df.head()


# In[66]:


gtrends_df.head()


# In[67]:


gtrends1_df=gtrends_df.rename(columns={"Month": "monthyr_num"})
gtrends1_df.head()


# In[68]:


massshoot_impact_df=pd.merge(mj_shoot12_df, gtrends1_df, on="monthyr_num", how="outer")
massshoot_impact_df


# In[69]:


massshoot_impact1_df = massshoot_impact_df.dropna(how='any')
massshoot_impact1_df


# In[70]:


def monthyr_impact(row):
    return row["monthyr_num"]+1
massshoot_impact1_df["monthyr_impact"] = massshoot_impact1_df.apply(monthyr_impact, axis=1)
massshoot_impact1_df.head()


# In[71]:


massshoot_impact1_df=pd.DataFrame(massshoot_impact1_df)
massshoot_impact1_df.head()


# In[72]:


massshoot_impact1_df['monthyr_impact']=massshoot_impact1_df['monthyr_impact'].astype(int)
massshoot_impact1_df.head()


# In[73]:


def monthyr_prev(row):
    return row["monthyr_impact"]-100
massshoot_impact1_df["monthyr_prev"] = massshoot_impact1_df.apply(monthyr_prev, axis=1)
massshoot_impact1_df.head()


# In[74]:


massshoot_impact1_df['monthyr_prev']=massshoot_impact1_df['monthyr_prev'].astype(int)
massshoot_impact1_df.head()


# In[75]:


massshoot_impact1_df=pd.DataFrame(massshoot_impact1_df)
massshoot_impact1_df.head()


# In[77]:


gun_sales_path12 = "Resources/nics-firearm-background-checks.csv"
gunsales_clean13 = pd.read_csv(gun_sales_path12)
gunsales_clean13.head()


# In[78]:


gunsales_clean13["Total Sales"] = (gunsales_clean13["handgun"]+gunsales_clean13["long_gun"]+gunsales_clean13["other"]+gunsales_clean13["multiple"])
gunsales_clean13["Total Sales"]


# In[79]:


gunsales_clean13=pd.DataFrame(gunsales_clean13)
gunsales_clean13.head()


# In[80]:


gunsales_clean13.columns


# In[81]:


gunsales_clean13=gunsales_clean13.drop(['month', 'state', 'permit', 'permit_recheck', 'handgun',
       'long_gun', 'other', 'multiple', 'admin', 'prepawn_handgun',
       'prepawn_long_gun', 'prepawn_other', 'redemption_handgun',
       'redemption_long_gun', 'redemption_other', 'returned_handgun',
       'returned_long_gun', 'returned_other', 'rentals_handgun',
       'rentals_long_gun', 'private_sale_handgun', 'private_sale_long_gun',
       'private_sale_other', 'return_to_seller_handgun',
       'return_to_seller_long_gun', 'return_to_seller_other', 'totals'], axis=1)
gunsales_clean13.head()


# In[82]:


gunsales_clean13_df = gunsales_clean13[gunsales_clean13['monthyr_num']>201212]
gunsales_clean13_df.tail()


# In[83]:


gunsales_clean13_df=gunsales_clean13_df.groupby(["monthyr_num"])
gunsales_clean13_df=gunsales_clean13_df.sum()
gunsales_clean13_df.head()


# In[84]:


gunsales_clean13_df=gunsales_clean13_df.reset_index()
gunsales_clean13_df.head()


# In[85]:


gunsales_clean13_df["monthyr_prev"] = (gunsales_clean13_df["monthyr_num"])
gunsales_clean13_df["monthyr_prev"]


# In[86]:


gunsales_clean13_df["monthyr_impact"] = (gunsales_clean13_df["monthyr_num"])
gunsales_clean13_df["monthyr_impact"]


# In[87]:


gunsales_clean13_df=pd.DataFrame(gunsales_clean13_df)
gunsales_clean13_df.head()


# In[88]:


massshoot_gunsales1_df=pd.merge(massshoot_impact1_df, gunsales_clean13_df, on="monthyr_prev", how="outer")
massshoot_gunsales1_df.head()


# In[89]:


massshoot_gunsales1_df=massshoot_gunsales1_df.drop(['monthyr_num_y', 'monthyr_impact_y'], axis=1)
massshoot_gunsales1_df.head()


# In[90]:


massshoot_gunsales1_df=massshoot_gunsales1_df.rename(columns={"Total Sales": "Total Sales_prev"})
massshoot_gunsales1_df.head()


# In[91]:


massshoot_gunsales1_df=massshoot_gunsales1_df.rename(columns={"monthyr_impact_x": "monthyr_impact"})
massshoot_gunsales1_df.head()


# In[92]:


massshoot_gunsales1_df=massshoot_gunsales1_df.rename(columns={"monthyr_num_x": "monthyr_num"})
massshoot_gunsales1_df.head()


# In[93]:


massshoot_gunsales2_df=pd.merge(massshoot_impact1_df, gunsales_clean13_df, on="monthyr_impact", how="outer")
massshoot_gunsales2_df.head()


# In[94]:


massshoot_gunsales2_df=massshoot_gunsales2_df.drop(['monthyr_num_y', 'monthyr_prev_y'], axis=1)
massshoot_gunsales2_df.head()


# In[95]:


massshoot_gunsales2_df=massshoot_gunsales2_df.rename(columns={"Total Sales": "Total Sales_impact", "monthyr_num_x": "monthyr_num", "monthyr_prev_x": "monthyr_prev"})
massshoot_gunsales2_df.head()


# In[96]:


massshoot_gunsales4_df = massshoot_gunsales1_df.merge(massshoot_gunsales2_df,how='outer', left_index=True, right_index=True)
massshoot_gunsales4_df.head()


# In[97]:


massshoot_gunsales4_df=massshoot_gunsales4_df.drop(['monthyr_num_y', 'Number of Incidents_y','Total Number of Victims in Month_y','Relative Value_y', 'monthyr_impact_y','monthyr_prev_y'], axis=1)
massshoot_gunsales4_df.head()


# In[98]:


massshoot_gunsales4_df.columns


# In[99]:


massshoot_gunsales4_df=massshoot_gunsales4_df.rename(columns={"monthyr_num_x": "monthyr_num", "Number of Incidents_x": "Number of Incidents", "Total Number of Victims in Month_x": "Total Number of Victims in Month", "Relative Value_x": "Relative Value", "monthyr_impact_x":"monthyr_impact","monthyr_prev_x":"monthyr_prev"})
massshoot_gunsales4_df.head()


# In[100]:


gunsales_clean14_df=gunsales_clean13_df.drop(['monthyr_prev', 'monthyr_impact'], axis=1)
gunsales_clean14_df.head()


# In[101]:


massshoot_gunsales5_df=pd.merge(massshoot_gunsales4_df, gunsales_clean14_df, on="monthyr_num", how="outer")
massshoot_gunsales5_df.head()


# In[102]:


gunsales_clean13=gunsales_clean13_df.to_csv("Resources/gunsales_clean13.csv", index=False, header=True)


# In[103]:


massshoot_impact1=massshoot_impact1_df.to_csv("Resources/massshoot_impact1.csv", index=False, header=True)


# In[104]:


massshoot_gunsales5=massshoot_gunsales5_df.to_csv("Resources/massshoot_gunsales5.csv", index=False, header=True)


# In[105]:


massshoot_gunsales5_df=massshoot_gunsales5_df.replace(201413, 201501)


# In[106]:


massshoot_gunsales5_df=massshoot_gunsales5_df.replace(201513, 201601)


# In[107]:


massshoot_gunsales5_df=pd.DataFrame(massshoot_gunsales5_df)
massshoot_gunsales5_df.head()


# In[108]:


massshoot_gunsales5_df['Total Sales_prev']=massshoot_gunsales5_df['Total Sales_prev'].fillna(984498)
massshoot_gunsales5_df.tail()


# In[109]:


massshoot_gunsales5_df['Total Sales_impact']=massshoot_gunsales5_df['Total Sales_impact'].fillna(1302140)
massshoot_gunsales5_df.tail()


# In[130]:


massshoot_gunsales5_df=pd.DataFrame(massshoot_gunsales5_df)
massshoot_gunsales5_df.head()


# In[131]:


massshoot_gunsales5_df = massshoot_gunsales5_df.dropna(how='any')
massshoot_gunsales5_df


# In[132]:


massshoot_gunsales5_df.dtypes


# In[133]:


totsale_prev_mean=massshoot_gunsales5_df["Total Sales_prev"].mean()
totsale_prev_mean


# In[134]:


totsale_impact_mean=massshoot_gunsales5_df["Total Sales_impact"].mean()
totsale_impact_mean


# In[135]:


totsale_mean=massshoot_gunsales5_df["Total Sales"].mean()
totsale_mean


# In[116]:


totsale_prev=massshoot_gunsales5_df["Total Sales_prev"]
totsale_impact=massshoot_gunsales5_df["Total Sales_impact"]
totsales_mean=massshoot_gunsales5_df["Total Sales"]


# In[117]:


stats.ttest_ind(totsale_prev, totsale_impact, equal_var=False)


# In[118]:


stats.ttest_ind(totsales_mean, totsale_impact, equal_var=False)


# In[119]:


plt.scatter(range(len(totsale_prev)), totsale_prev, label="Total Gun Sales Year Prior to Mass Shooting")
plt.scatter(range(len(totsale_impact)), totsale_impact, label="Total Gun Sales Month After a Mass Shooting")
plt.scatter(range(len(totsales_mean)), totsales_mean, label="Total Gun Sales the Month of a Mass Shooting")
plt.legend()


# In[120]:


plt.savefig("Gun_Sales_Scatter.png")


# In[121]:


plt.hist(totsale_prev, 10, density=True, alpha=0.7, label="Total Gun Sales Year Prior to Mass Shooting")
plt.hist(totsale_impact, 10, density=True, alpha=0.7, label="Total Gun Sales Month After a Mass Shooting")
plt.hist(totsales_mean, 10, density=True, alpha=0.7, label="Total Gun Sales the Month of a Mass Shooting")
plt.axvline(totsale_prev.mean(), color='k', linestyle='dashed', linewidth=1)
plt.axvline(totsale_impact.mean(), color='k', linestyle='dashed', linewidth=1)
plt.axvline(totsales_mean.mean(), color='k', linestyle='dashed', linewidth=1)
plt.legend()


# In[122]:


plt.savefig("Gun_Sales_Hist.png")


# In[123]:


x_axis=massshoot_gunsales5_df["monthyr_num"]
y_axis=massshoot_gunsales5_df["Total Number of Victims in Month"]
gun_sales=massshoot_gunsales5_df["Total Sales"]/1000
plt.plot(x_axis, y_axis, label="Total Number of Mass Shooting Victims per Month")
plt.plot(x_axis, gun_sales,label="Gun Sales per 1000")
plt.legend(loc="upper right")
plt.xlabel("Month and Year")


# In[124]:


plt.savefig("Gun_Sales_Mass Shooting Victims.png")


# In[127]:


#This is the file I used to do the analysis
massshoot_gunsales6=massshoot_gunsales5_df.to_csv("Resources/massshoot_gunsales6.csv", index=False, header=True)


# In[125]:


mj_clean4_df.head()


# In[126]:


#This is the clean MJ data that includes all of the information about the shooter
mj_clean4=mj_clean4_df.to_csv("Resources/mj_clean4.csv", index=False, header=True)


# In[136]:


massshoot_path25 = "Resources/massshoot_gunsales6.csv"


# In[137]:


massshoot_gunsales6 = pd.read_csv(massshoot_path25)


# In[140]:


totsale_prev=massshoot_gunsales6["Total Sales_prev"]
totsale_impact=massshoot_gunsales6["Total Sales_impact"]
totsales_mean=massshoot_gunsales6["Total Sales"]
tot_num_vics=massshoot_gunsales6["Total Number of Victims in Month"]
rel_val=massshoot_gunsales6["Relative Value"]


# In[142]:


stats.f_oneway(tot_num_vics, rel_val)


# In[143]:


massshoot_gunsales6.corr(method="pearson")


# In[146]:


x_axis=massshoot_gunsales6["monthyr_num"]
y_axis=massshoot_gunsales6["Total Number of Victims in Month"]
rel_val=massshoot_gunsales6["Relative Value"]
plt.plot(x_axis, y_axis, label="Total Number of Mass Shooting Victims per Month")
plt.plot(x_axis, gun_sales,label="Google Search Score for Shooting")
plt.legend(loc="upper right")
plt.xlabel("Month and Year")


# In[150]:


totsale_prev_std=massshoot_gunsales6["Total Sales_prev"].std()
totsale_prev_std


# In[151]:


totsale_impact_std=massshoot_gunsales6["Total Sales_impact"].std()
totsale_impact_std


# In[152]:


totsale_prev_mean=massshoot_gunsales6["Total Sales_prev"].mean()
totsale_prev_mean


# In[147]:


plt.savefig("Google Search Shooting and Number of Victims.png")

