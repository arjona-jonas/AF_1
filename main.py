import numpy as np

matriz=np.genfromtxt("AF1_dados.txt",delimiter=",")

#matriz nova advinda da arquivo externo
print("matriz original:",matriz,sep="\n")

#mean das linhas
#quero colapsar colunas, logo axis=1
print('\nmedia das linhas: ',matriz.mean(axis=1))

#sum das colunas
#quero colapsar linhas, logo axis=0
print('\nsoma das colunas: ',matriz.sum(axis=0))

#median do array todo
print('\nmediana geral:',np.median(matriz))

#matriz transposta
matriz_transposta=matriz.T
print('\nmatriz transposta\n', matriz_transposta)

#transposta multiplicada por pi
print('\nmatriz transposta multiplicada por 3.1415\n', matriz_transposta*3.1415)

#produto escalar
matriz_auxiliar=np.arange(1,31).reshape(5,6)

print('\nproduto escalar entre duas matrizes \n',matriz @ matriz_auxiliar)

#filtrando matriz
result=matriz[matriz>matriz.mean()]
print('\nentradas maiores que a média da matriz:\n',result)

#opereção aritmética com matriz
print('\noperecao aritmetica:\n',(matriz/matriz.sum())*100)