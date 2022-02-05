"""
Laços de repetição
O que vai determinar a estrutura, isso é, lista ou dicionário, são as chaves e colchetes
lista = []
dicionário = {}"""

nomes=[
  'paulo','joao','maria','carlos','sara'
]
'''
for item in nomes:
  print(item)
'''





dados = [
  "nome1","nome2",1,2,True,False,1.5,2.3,True
]

boleanos = []
numeros = []
textos = []

for item in dados:
  if isinstance(item,bool):
    boleanos.append(item)

  elif isinstance(item,int):
    numeros.append(item)

  elif isinstance(item,float):
    numeros.append(item)

  elif isinstance(item,str):
    textos.append(item)


'''
verifica se variavel item pertence a um tipo de dado
isinstance(item,tipo_de_dados)

funcao que adiciona novo elemento no final da lista[]
lista.append(novo_valor)
'''



















for i in range(4):
  if nomes[i]=='carlos':
    print('achei o carlos')
  elif nomes[i]!='carlos':
    print('nao é o carlos')
  elif nomes[i]=='sara':
    print('achei a sara')  
  else:
    print(nomes[i])