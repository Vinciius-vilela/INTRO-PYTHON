#!/usr/bin/env python
# coding: utf-8

# # Listas em Python

# In[2]:


# criando uma lista de mercado
listadomercado = ["ovos, farinha, leite, maças"]


# In[4]:


print (listadomercado)


# In[8]:


# criando a segunda lista
listadomercado2 = [ "ovos", "farinha", "leite", "maças"]


# In[10]:


print (listadomercado2)


# In[12]:


print (listadomercado[0])


# In[51]:


print (listadomercado2[0])


# In[54]:


print (listadomercado2)


# In[55]:


listadomercado2[2] = "chocolate"


# In[56]:


print (listadomercado2)


# In[17]:


lista3 = [25, 55, "isso"]


# In[34]:


lista3[0]
lista3[1]


# In[38]:


item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]


# In[49]:


print (item1, ",", item2, ",", item3)


# In[58]:


del listadomercado2[3]


# In[60]:


print (listadomercado2)


# In[63]:


# listas aninhadas
listas = [[10,11,12], ["A", "B","c"], ["teste1", "teste2","teste 3"]]


# In[65]:


# imprimindo as listas
listas


# In[67]:


listas[0]


# In[69]:


listas[1]


# In[71]:


listas[2]


# In[74]:


a = listas[0]


# In[77]:


a


# In[79]:


b = listas[1]


# In[82]:


c = listas[2]


# In[85]:


d = listas[3]


# In[87]:


# fatiamento

a[0]


# In[89]:


a[1]


# In[92]:


a[2]


# In[108]:


b


# In[110]:


listas[0]


# In[112]:


listas[0][0]


# In[114]:


listas[0][2]


# # teste com lista, utilizando o operador in

# In[116]:


lista_int = ["abd", "ofl", 1633, 5563]


# In[121]:


print ("abd" in lista_int)


# In[124]:


print (1633 in lista_int)


# In[ ]:




