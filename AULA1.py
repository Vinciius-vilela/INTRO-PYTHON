'''
COMENTARIO DE BLOCO
'''
#COMETÁRIO DE LINHA
TOTAL=2 #O QUE É UMA VARIÁVEL? É UM ESPAÇO ALOCADO EM MEMÓRIA
TOTAL=1
texto='texto'
verdade='True'
mentira='True' #Isso é uma variável do tipo booleano
lista=[1,2,3,10] 
print(lista)
'''
Operações com listas
'''
#Essa linha está trazendo a função print com 2 parâmetros.
#1º parametro é uma função que retorna a quantidade de itens dentro de uma lista.
#2º parametro é a impressão da lista na posição número 3
print(
  len(lista),lista[3]
)
lista2=[
  'nome', 222, False, 2.009, [
    'nome', 222, False, 2.009, [
      'nome', 222, False, 2.009, []
    ]
  ]
]
'''
A função "print" está imprimindo uma lista que se encontra na posição "4" que possui uma nova lista, na posição "4" e que possui um valor booleano na posição "2"
'''
print(lista2[4][4][2])

#dicionários
dicionario={
  'nome':'vinicius',
  'idade':24,
  'altura':1.80,
  'skills':['joga bola','anda de moto']
}
'''
Impressão de um dicionário na chave "nome"
'''
print(dicionario['nome'])

print('Olá mundo')

