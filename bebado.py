'''
Autora: Julia Marcolan
Contato: juliamarcolant@gmail.com
'''

import matplotlib.pyplot as plt
import random

NB = 100000  #número de bebados 
N = 5000    #número de passos de cada bebado 
ne = 0 #numero de passos para a esquerda
nd = 0 #numero de passos para a direita
L = 1 #tamanho do passo do bebado 
x  = [] 


# Para cada bebado calculo as iterações para N passos 
for i in range(NB):
    for j in range(N):
        rand = random.random()
        if(rand > 0.5):
            #ne = ne + 1 
            ne += 1 
        else:
            nd +=  1
    d = (nd - ne)*L
    x.append(d) 
    ne = 0 
    nd = 0 
 
plt.hist(x, 1000)
plt.show()

    

    



        

