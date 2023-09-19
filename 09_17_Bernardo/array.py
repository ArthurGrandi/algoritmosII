import numpy as np

# define o tamanho do array
arraySize = 5

# inicializa o array com zeros em cada posição
vetor = np.zeros(arraySize)

# imprime os valores dentro do array
print(vetor)

# acessando uma posição do array
print(vetor[0])

# preenche o vetor com valores do tipo float 
for i in range(arraySize):
    vetor[i] = float(input(f"Informe um valor para V[{i}]: "))

# mostra os valores armazenados na estrutura
print(vetor)



# mostra o tipo da estrutura
print(type(vetor))

#soma2 = 
vetor.sum() # somatório

#media = 
vetor.mean() # média

#desvio = 
vetor.std() # desvio padrão

#max = 
vetor.max() # o maior valor

#min = 
vetor.min() # o menor valor

#argmax = 
vetor.argmax() # retorna a posição que contém o maior valor da estrutura

#argmin = 
vetor.argmin() # retorna a posição que contém o menor valor da estrutura

