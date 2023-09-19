"""
1. Sendo o vetor V igual a:
"""
import numpy as np

N = 10
V = [2, 6, 8, 3, 10, 9, 1, 21, 33, 14]

X = 2
Y = 4

print(V[X+1])
print(V[X+2])
print(V[X+3])
print(V[X*4])
print(V[X*1])
print(V[X*2])
print(V[X*3])
print(V[ V [X+Y]])
print(V[X+Y])
print(V[8-V[2]])
print("V[V[4]] Esta fora do range")
print("V[ V[ V[7]]] Esta fora do range")
print("V[V[1]*V[4]] Esta fora do range")
print(V[X+4])