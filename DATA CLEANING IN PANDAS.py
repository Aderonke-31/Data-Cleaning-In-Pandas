#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # Load the Datasets

# In[3]:


df = pd.read_excel(r"C:\Users\ADERONKE\Downloads\Customer Call List.xlsx")
df


# In[4]:


df.drop_duplicates()


# # Dropping unused or column not useful

# In[123]:


df = df.drop(columns = "Not_Useful_Column")
df


# # STRIP

# In[9]:


#Strip takes both sides. left or the rightstrip taked from lstip or strip side


# In[14]:


df["Last_Name"].str.strip()


# In[11]:


# Using left strip to take out the ...potter


# In[15]:


df["Last_Name"].str.strip("...")


# In[16]:


# Using lstrip to take out /white


# In[17]:


df["Last_Name"].str.strip("/")


# In[18]:


# Strip could be use in multiples and both left and right same time


# In[19]:


df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df


# In[20]:


# Strip in one shot


# In[21]:


df["Last_Name"].str.strip("123._/")


# In[60]:


# Cleaning up the phone number colunm to have equal digits. Using Replace to Cleaning/Standardizing Phone Numbers.


# In[26]:


# Formating using Lambda or for loop. This is Lambda


# In[40]:


#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')
#df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))


# In[48]:


df["Phone_Number"].apply(lambda x: str(x))


# In[62]:


df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')


# In[61]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))


# In[68]:


df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])


# In[69]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan','')
df["Phone_Number"] = df["Phone_Number"].str.replace('N/a','')
df


# # SPLITTING COLUMNS

# In[73]:


df["Address"].str.split(',',1)


# In[72]:


#OR


# In[75]:


df["Address"].str.split(',',2, expand=True)


# In[77]:


df[["Street_Address","State", "Zip_Code"]] = df["Address"].str.split(',',2, expand=True)
df


# In[124]:


#Drop Address columns after the split


# In[125]:


df = df.drop(columns = "Address")
df


# In[79]:


#Changing Yes to Y and No to N. to make it look consistent


# In[86]:


df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"].str.replace('No','N')


# In[87]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df


# In[88]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df


# In[89]:


#Romoving the N/a, NaN OR dropfillna(0)


# In[92]:


df.replace('N/a','')
df


# In[94]:


df.fillna(0)


# In[95]:


#OR


# In[97]:


df = df.fillna('')
df


# In[128]:


# Dropping Do_Not_Contact row that says Y
#df = df.dropna(subset="Phone_Number"), inplace=True  . For dropping null values


# In[99]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] =='Y':
        df.drop(x, inplace=True)
        
df


# In[100]:


# Dropping Blank Phone_Number rows


# In[101]:


for x in df.index:
    if df.loc[x, "Phone_Number"] =='':
        df.drop(x, inplace=True)
        
df


# In[117]:


#Reset/Rearrange the numbers


# In[119]:


df.reset_index(drop=True)


# In[126]:


df = df.reset_index(drop=True)
df


# In[ ]:




