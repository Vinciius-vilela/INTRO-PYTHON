#!/usr/bin/env python
# coding: utf-8

# # Dicionários Python

# In[3]:


# Criando lista
lista_estudantes = ["José", 25, "Dayelle", 26, "Benjamin", 27, "Naiara", 22]


# In[5]:


lista_estudantes


# In[8]:


# Criando um dicionário
dicionario_estudantes = {"José":25, "Dayelle":26, "Benjamin":27, "Naiara":22}


# In[12]:


dicionario_estudantes["José"]


# In[14]:


dicionario_estudantes["Naiara"]


# In[17]:


# adicionando um novo registro ao dicionário
dicionario_estudantes["Natan"] = 28


# In[19]:


# imprimindo a lista novamente, com o Natan já incluso
dicionario_estudantes


# In[26]:


#comando para limpar o dicionário -- vou colocar o .clear na frente do dicionário
dicionario_estudantes.clear()


# In[28]:


# tentando imprimir o dicionário que foi apagado
dicionario_estudantes
# trouxe apenas as chaves


# In[31]:


# apagando todo o dicionário com o comando del
del dicionario_estudantes


# In[33]:


# tentando imprimir o dicionario dos estudantes
dicionario_estudantes


# In[37]:


# criando novamente um dicionário, dessa vez vamos identificar que se trata de um dicionari apenas pela forma com abrimos
# e fechamos ele, isso é, através das chaves
trabalho = {"Marcos": 34, "Zé Ricardo": 35, "Muller": 30, "Vagner": 38}


# In[39]:


trabalho


# In[42]:


# usando a função len para verificar o comprimento, ou o tamanho do dicionário
len(trabalho)
# ele vai trazer apenas 4, porque temos apenas 4 combinações de chave e valor


# In[45]:


# podemos extrair, caso queiramos, apenas as chaves .keys() quanto apenas os valores .values()
trabalho.keys()


# In[47]:


trabalho.values()


# In[51]:


# posso também utilizar a função .items(), caso eu queira trazer chaves e valores, similar à impressão sem função
trabalho.items()


# In[53]:


# podemos utilizar a função update para atualizar um dicionário, com as informações de outro dicionário
trabalho2 = {"Lidiane": 28, "Adão": 32, "Morgana": 29}


# In[55]:


# usando o update para atualizar os dicionários
trabalho.update(trabalho2)


# In[57]:


trabalho


# In[ ]:




