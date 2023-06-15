#!/usr/bin/env python
# coding: utf-8

# In[37]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# In[38]:


path=r"C:\Program Files (x86)\chromedriver.exe"


# In[39]:


browser = webdriver.Chrome()


# # L1(List containing all the links taken from website)

# In[13]:


l1=[]


# In[14]:


for page in range(2, 500):
    url = f"https://www.bproperty.com/en/bangladesh/properties-for-rent/page-{page}/"
    browser.get(url)
    input_search=browser.find_element(By.CLASS_NAME,'aeb96d72')
    child_elements = input_search.find_elements(By.XPATH, './/a')
    for child_element in child_elements:
        link = child_element.get_attribute('href')
        if link.endswith('.html'):
            l1.append(link)
            print(link)
         


# # Checking if data can be scrapped from a definite link from list

# In[15]:


l1=list(set(l1))


# In[16]:


len(l1)


# In[17]:


l1


# In[ ]:





# In[42]:


l1[1776]


# In[43]:


text = str(l1[1776])


# In[44]:


text


# In[ ]:


desired_class


# In[ ]:


new=desired_class.find_element(By.CLASS_NAME,'e5795c9b')


# In[ ]:


new1=new.find_element(By.CLASS_NAME,'_126656cb')


# In[ ]:


new1.text.replace('\n','')


# In[ ]:


q=new1.text


# In[ ]:


q.replace('\n','')


# In[ ]:


new2=new.find_element(By.CLASS_NAME,'_1f0f1758')


# In[ ]:


new2.text


# In[ ]:


new3=desired_class.find_element(By.CLASS_NAME,'_6f6bb3bc')


# In[ ]:


new3.text


# In[ ]:


p=new3.text


# In[ ]:


p


# In[ ]:


modified_string =p
beds, baths, sqft = modified_string.split('\n')
print(beds)
print(baths)
print(sqft)


# In[ ]:


beds.replace('Beds',"")


# In[ ]:


import re


# In[ ]:


numbers = re.findall(r'\d+(?:,\d+)?', p)


# In[ ]:


numbers


# In[22]:


l2=[]


# In[23]:


contents={}


# # Final Scraping information from the latest list

# In[45]:


for i in range(0,len(l1)):
    contents={}
    p=l1[i]
    text = str(l1[i])
    browser.get(text)
    desired_class = browser.find_element(By.CLASS_NAME,'_6803f627')
    new=desired_class.find_element(By.CLASS_NAME,'e5795c9b')
    new1=new.find_element(By.CLASS_NAME,'_126656cb')
    new2=new.find_element(By.CLASS_NAME,'_1f0f1758')
    new3=desired_class.find_element(By.CLASS_NAME,'_6f6bb3bc')
    new4 = desired_class.find_element(By.CLASS_NAME,'_033281ab')
    p1=new4.text.split()[1]
    p=new3.text
    modified_string =p
    beds, baths, sqft = modified_string.split('\n')
    print(new1.text.replace('\n',''))
    contents["address"]=new2.text
    contents["type"]=p1
    contents["rent"]=new1.text.replace('\n','')
    contents["beds"]=beds.replace('Beds','')
    contents["baths"]=baths.replace('Baths','')
    contents["sqft"]=sqft.replace('sqft','')
    
    l2.append(contents)

    
    

    
    


# In[46]:


len(l2)


# In[47]:


l2


# In[48]:


columns=["address","type","rent","beds","baths","sqft","Location","Area"]


# In[49]:


import pandas as pd


# # Converting into CSV file

# In[51]:


df=pd.DataFrame(data=l2,columns=columns)
df.to_csv("Dhakacity_new10.csv",index=False)


# In[ ]:





# # Data preprocessing and other manipulations

# In[52]:


df.info()


# In[54]:


df.isnull().sum()


# In[55]:


df1=df.copy()


# In[56]:


df1.head()


# In[57]:


df1["Location"] = df1['address'].apply(lambda x: x.split(" ")[-1])


# In[58]:


df1["Location"].value_counts()


# In[68]:


df1["type"].value_counts()


# In[59]:


df1.head()


# In[60]:


df1['rent']=df1['rent'].str.replace("BDT","")


# In[61]:


multipliers = {'Thousand': 1000, 'Lakh': 100000}

# Convert the 'rent' column to numeric values
df1['rent'] = df1['rent'].str.split().apply(lambda x: float(x[0]) * multipliers.get(x[1], 1))


# In[62]:


df1['Area'] = df1['address'].str.split(',').str[-2].str.strip()


# In[63]:


df1.head(20)


# # Final preprocessed data converted to CSV

# In[67]:


df=pd.DataFrame(data=df1,columns=columns)
df.to_csv("Dhakacity20.csv",index=False)


# In[ ]:





# In[ ]:




