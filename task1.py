#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install cobra')


# In[4]:


from cobra import Model,Reaction,Metabolite


# In[5]:


model=Model("the first model")


# In[8]:


r1=Reaction('r1')
r1.name='r1'
r1.lower_bound=0
r1.upper_bound=1000


# In[9]:


r2=Reaction('r2')
r2.name="r1"
r2.lower_bound=0
r2.upper_bound=1000


# In[25]:


r3=Reaction('r3')
r3.name='r3'
r3.lower_bound=.1
r3.upper_bound=.9


# In[26]:


r4=Reaction("r4")
r4.name="4"
r4.lower_bound=.1
r4.upper_bound=.9


# In[27]:


r0=Reaction("r0")
r0.name="r0"
r0.lower_bound=1
r0.upper_bound=1


# In[28]:


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[29]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[30]:


#r1  A======>B #
r1.add_metabolites({A:-1,B:1})

#r2  B======>C #
r2.add_metabolites({B:-1,C:1})

#r3  A======>ATP #
r3.add_metabolites({A:-1,ATP:1})

#v4  ATP======> #
r4.add_metabolites({ATP:-1})

#r0  ======>A #
r0.add_metabolites({A:1})

#M  C======> #
M.add_metabolites({C:-1})


# In[31]:


model.add_reactions([r0,r1,r2,r3,r4,M])


# In[32]:


model.objective='M'


# In[33]:


model.optimize()


# In[ ]:




