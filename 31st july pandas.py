#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = { 'name' : ["vish",'sudh',"krish",'hitesh'],
       "emial_id" :["vishwanathpatil023@gmail.com","sudhanshu@ai.in","krish@ai.in","hitesh@ai.in"],
       "slary" : [100 , 300, 350,250],
       "addr" : ["blr","blr","blr","mum"]}


# In[3]:


pd.DataFrame(data)


# In[4]:


pd.DataFrame(data , columns =[0,1,2,3]) # it ll not give elements


# In[5]:


pd.DataFrame(data , index=[4,5,6,7])


# In[6]:


df = pd.DataFrame(data , index=[4,5,6,7])


# In[7]:


df


# In[8]:


df = pd.DataFrame(data , index=[0,1,2,3])


# In[9]:


df = pd.DataFrame(data) #removing custom indexes


# In[10]:


df.loc[5:6]  # loc always go for name indexes


# In[11]:


df.iloc[5:6] # iloc always go for default indexes


# In[12]:


df.iloc[1:3]


# In[13]:


pd.DataFrame(data , index=['vish','krish','sudh','patil'])


# In[14]:


data1 = {'pf_no' : [234,567,895,569],
       'income_tax': [4589,56689,45236,7854],
       'mobile_no' : [485965,55489,568789,34659],
       'courses' : ['ds' , 'bigdta' , 'web dev' , 'blockchain']}


# In[15]:


df1=pd.DataFrame(data1)


# In[16]:


df1


# In[17]:


pd.concat([df,df1])


# In[18]:


pd.concat([df,df1] , axis = 1) # vertical concat


# In[19]:


pd.concat([df,df1] , axis = 0) #horizontal concatation


# In[20]:


data2 = { '0' : ["vish",'sudh',"krish",'hitesh'],
       "1" :["vishwanathpatil023@gmail.com","sudhanshu@ai.in","krish@ai.in","hitesh@ai.in"],
       "2" : [100 , 300, 350,250],
       "3" : ["blr","blr","blr","mum"]}


# In[21]:


data3 = {'0' : [234,567,895,569],
       '1': [4589,56689,45236,7854],
    '2' : [485965,55489,568789,34659],
       '3' : ['ds' , 'bigdta' , 'web dev' , 'blockchain']}


# In[22]:


df2= pd.DataFrame(data2)


# In[23]:


df3=pd.DataFrame(data3)


# In[24]:


df2


# In[25]:


df3


# In[26]:


pd.concat([df2,df3])


# In[27]:


data4= {"emp_id" : [101,102,103,104],
        "salary" : [234,345,200,400],
        "pf" :[23,45,56,45],}


# In[28]:


data5 = {"emp_id" : [101,102,104,105],
        "mob_no" : [23456,45689,5648,36489],
        "house_no" :[235,845,456,645],}


# In[29]:


df4= pd.DataFrame(data4)


# In[30]:


df4


# In[31]:


df5=pd.DataFrame(data5)


# In[32]:


df5


# In[33]:


pd.merge(df4,df5)


# In[34]:


df4


# In[35]:


df5


# In[36]:


pd.merge(df4,df5, how = "left")


# In[37]:


pd.merge(df4,df5, how = "right")


# In[38]:


pd.merge(df4,df5, how = "right" , on = "emp_id")


# In[39]:


data6= {"emp_id1" : [101,102,103,104],
        "salary" : [234,345,200,400],
        "pf" :[23,45,56,45],
       
     }

data7 = {"emp_id2" : [101,102,104,105],
        "mob_no" : [23456,45689,5648,36489],
        "house_no" :[235,845,456,645],
     }



# In[40]:


df6= pd.DataFrame(data6)


# In[41]:


df7 = pd.DataFrame(data7)


# In[42]:


df6


# In[43]:


df7


# In[44]:


pd.merge(df6,df7)


# In[ ]:


pd.merge(df6,df7 , left_on="emp_id1" , right_on = "emp_id2" , how = "inner")


# In[ ]:


data8= {"emp_id" : [101,102,103,104],
        "salary" : [234,345,200,400],
        "pf"     :      [23,45,56,45],
       
     }

data9= {"emp_id" : [101,102,104,105],
        "salary" : [234,345,200,878],
    "house_no"   :[235,845,456,645],
     }


# In[ ]:


df8=pd.DataFrame(data8)


# In[ ]:


df9=pd.DataFrame(data9)


# In[ ]:


df8


# In[ ]:


df9


# In[ ]:


pd.merge(df8,df9 , on = ['emp_id' , 'salary'])


# In[ ]:


data9 = {"emp_id" : [101,102,104,105],
        "salary" : [234,345,200,878,54678],
        "house_no" :[235,845,456,645],
     } # changing the data set dimension changing, 5 elements in salary, dimension not going to effect


# In[ ]:


pd.merge(df8,df9 , on = ['emp_id' , 'salary'])


# In[47]:


data10= {"emp_id1" : [101,102,103,104],
        "salary1" : [234,345,200,400],
        "pf"     : [23,45,56,45],
       
     }

data11= {"emp_id2" : [101,102,104,105,452],
        "salary2" : [234,345,200,878,659],
    "house_no"   :[235,845,456,645,562],
         
     }


# In[49]:


df10 = pd.DataFrame(data10)


# In[50]:


df11 = pd.DataFrame(data11)


# In[51]:


df10


# In[52]:


df11


# In[53]:


df10 = pd.DataFrame(data10,index = ['a','b','c','d'])


# In[54]:


df11 = pd.DataFrame(data11,index = ['a','b','c','d','e'])


# In[55]:


df10


# In[56]:


df11


# In[57]:


df10.join(df11)


# In[58]:


pd.read_csv("G:\Downloads\sales_data_final.csv")


# In[59]:


df_sales = pd.read_csv("G:\Downloads\sales_data_final.csv")


# In[60]:


df_sales.head()


# In[61]:


def profit_flag(a):
    if a > 0 :
        return 'positive'
    else :
        return 'negative'


# In[62]:


profit_flag(-45)


# In[63]:


profit_flag(45)


# In[64]:


df_sales['falg_sales'] = df_sales['profit'].apply(profit_flag)


# In[65]:


df_sales.head()


# In[66]:


df_sales['len_cust_name'] = df_sales['customer_name'].apply(len)


# In[67]:


df_sales.head()


# In[68]:


def quantity_flag(a):
    if a < 10 :
        return 'low'
    elif a > 10 and a < 20 :
        return 'medium'
    else :
        return 'high'


# In[69]:


df_sales['falg_quantity'] = df_sales['quantity'].apply(quantity_flag)


# In[70]:


df_sales.head()


# In[72]:


df_sales


# In[73]:


df_sales['square_quantity'] = df_sales['quantity'].apply(lambda a : a**2)


# In[74]:


df_sales.head()


# In[75]:


import numpy as np


# In[76]:


np.array([2,3,5,6,6])


# In[77]:


type(np.array([2,3,5,6,6]))


# In[78]:


np.array([[2,3,4],[4,5,6]])


# In[81]:


np.array([[1,2,3,4],[2,3,4,5]])


# In[82]:


l = [[1,2,3,4],[2,3,4,5]]


# In[83]:


l[0][0]


# In[84]:


l[1][1]


# In[90]:


l[0][3]


# In[93]:


a = np.array([3,4,5,6] )


# In[94]:


a


# In[95]:


a = np.array([3,4,5,6] , ndmin = 5 )


# In[96]:


a


# In[97]:


a = np.array([3,4,5,6] , ndmin = 3 )


# In[98]:


a


# In[107]:


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[108]:


arr


# In[109]:


arr.ndim


# In[111]:


np.random.randint(1,10,(4,4))


# In[112]:


np.random.randint(1,10,(4,4,2))


# In[ ]:




