# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:04:06 2021

@author: computer
"""

import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
# A = np.loadtxt("matrix4.txt")
# print(A)
# G = nx.from_numpy_matrix(A)
# nx.draw(G)
# plt.show()
# B = sorted(G.degree, key=lambda x: x[1], reverse=True)
# print(B)

# n=100
# A = np.random.randint(0,9,(n,n))
# G = nx.from_numpy_matrix(A)
# nx.draw(G)
# plt.show()
# B = sorted(G.degree, key=lambda x: x[1], reverse=True)
# print(B)

import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt

A = np.loadtxt("matrix.txt")
print(A)
G=nx.from_numpy_matrix(A,create_using=nx.DiGraph)
nx.draw(G)
plt.show()

sortA =  sorted(np.array(G.in_degree), key=lambda a_entry: a_entry[1]) 
print(sortA)