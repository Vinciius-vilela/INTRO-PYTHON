#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("\n\n\n**********  PYTHON CALCULATOR  **********", "\n\nSelecione o número da operação que deseja realizar:\n\n\n1 - Soma", "\n2 - Subtração", "\n3 - Multiplicação", "\n4 - Divisão\n\n\n")


# In[2]:


escolhaUsuario = (int(input("Digite sua opção: \n")))


# In[3]:


numero1 = (float(input("\nDigite o primeiro número: \n")))


# In[ ]:


numero2 = (float(input("\nDigite o segundo número\n")))

if escolhaUsuario == 1:
    print(numero1, "+", numero2, "=", (numero1 + numero2))
elif escolhaUsuario == 2:
    print(numero1, "-", numero2, "=", (numero1 - numero2))
elif escolhaUsuario == 3:
    print(numero1, "x", numero2, "=", (numero1 * numero2))
elif escolhaUsuario == 4:
    print(numero1, "/", numero2, "=", (numero1 / numero2))
else:
    print("Você digitou uma opção inválida!!")

escolhaUsuario = (int(input("Digite sua opção: \n")))


# In[ ]:




