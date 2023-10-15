import numpy as np
import random as rm
import matplotlib.pyplot as plt

#DATOS
grupos = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]

transicion =    [["g11", "g12", "g13", "g14", "g15", "g16", "g17", "g18", "g19"],
                ["g21", "g22", "g23", "g24", "g25", "g26", "g27", "g28", "g29"],
                ["g31", "g32", "g33", "g34", "g35", "g36", "g37", "g38", "g39"],
                ["g41", "g42", "g43", "g44", "g45", "g46", "g47", "g48", "g49"],
                ["g51", "g52", "g53", "g54", "g55", "g56", "g57", "g58", "g59"],
                ["g61", "g62", "g63", "g64", "g65", "g66", "g67", "g68", "g69"],
                ["g71", "g72", "g73", "g74", "g75", "g76", "g77", "g78", "g79"],
                ["g81", "g82", "g83", "g84", "g85", "g86", "g87", "g88", "g89"],
                ["g91", "g92", "g93", "g94", "g95", "g96", "g97", "g98", "g99"]]

transicion_matriz =  np.array([[0.25, 0.06, 0.08, 0.15, 0.04, 0.02, 0.15, 0.15, 0.10],
                    [0.15, 0.15, 0.10, 0.22, 0.01, 0.02, 0.15, 0.10, 0.10],
                    [0.12, 0.00, 0.05, 0.24, 0.14, 0.04, 0.27, 0.07, 0.07],
                    [0.05, 0.13, 0.05, 0.30, 0.10, 0.10, 0.22, 0.05, 0.00],
                    [0.18, 0.20, 0.07, 0.20, 0.15, 0.05, 0.05, 0.05, 0.05],
                    [0.20, 0.10, 0.20, 0.05, 0.05, 0.10, 0.02, 0.15, 0.13],
                    [0.01, 0.05, 0.15, 0.14, 0.17, 0.10, 0.12, 0.10, 0.16],
                    [0.17, 0.15, 0.07, 0.07, 0.15, 0.10, 0.12, 0.09, 0.08],
                    [0.13, 0.11, 0.13, 0.03, 0.20, 0.20, 0.04, 0.15, 0.01]])


#Part 1

def gruposMarkov(iteraciones):
    actual = rm.randrange(0,8) #Estado inicial random grupo 1-9
    #print("Estado inicial: " + str(actual))
    listaGrupos = [grupos[actual]] #Se guarda el primer estado en una lista 
    for i in range(iteraciones):
        #Obtenemos la transición de grupo de último grupo + nuevo grupo utilizando np.random.choice
        #Ingresando como parametros el array del grupo actual + el array con las probabilidades del siguiente estado a partir del grupo actual
        change = np.random.choice(transicion[actual],replace=True,p=transicion_matriz[actual])
        actual = int(change[-1])-1 #Variable con el nuevo grupo
        listaGrupos.append(grupos[actual]) #se añade nuevo grupo a la lista de grupos
            
    #print("Lista final grupos: " + str(listaGrupos))
    return listaGrupos

iter = 100
aux = gruposMarkov(iter)

#Se cuenta cada vez que sale una canción del grupo x y se va sumando en el contador respectivo
countg1 = 0; countg2 = 0; countg3 = 0; countg4 = 0; countg5 = 0; countg6 = 0; countg7 = 0; countg8 = 0; countg9 = 0; k = 0

for k in range(iter):
    if aux[k] == "G1": countg1 += 1
    elif aux[k] == "G2": countg2 += 1
    elif aux[k] == "G3": countg3 += 1
    elif aux[k] == "G4": countg4 += 1
    elif aux[k] == "G5": countg5 += 1
    elif aux[k] == "G6": countg6 += 1
    elif aux[k] == "G7": countg7 += 1
    elif aux[k] == "G8": countg8 += 1
    else : countg9 += 1

print("G1: " + str(countg1) + " G2: " + str(countg2) + " G3: " + str(countg3) + " G4: " + str(countg4) + " G5: " + str(countg5) + " G6: " + str(countg6) + " G7: " + str(countg7) + " G8: " + str(countg8) + " G9: " + str(countg9))

#Probabilidad de que salga una canción de cada grupo G
prob_grupos = [countg1/iter, countg2/iter, countg3/iter, countg4/iter, countg5/iter, countg6/iter, countg7/iter, countg8/iter, countg9/iter]
print("Prob Grupos: " + str(prob_grupos))

#Gráfico de Probabilidades de que salga 0. de escuchadas de cada grupo
plt.plot(grupos, prob_grupos)
plt.title('Prob. que salga grupo x')
plt.xlabel('Grupos')
plt.ylabel('Probabilidades')
plt.show()


#Part 2

#La suma de cada fila de la matriz de transiciones da como resultado 1, por lo que la matriz es matriz estocástica en sus filas
# Se traspone la matriz para que así las transiciones correspondan a la multiplicación a la derecha por un vector columna.

transicion_matriz_t = transicion_matriz.T #Se traspone la matriz de probabilidades para calcular los eigenvectores. Esto para...
eigenvalores, eigenvectores = np.linalg.eig(transicion_matriz_t) #np.linalg.eig retorna en arrays los eigenvalores y eigenvectores de la derecha.
val_close1 = np.isclose(eigenvalores,1) #Retorna una matriz booleana donde es true si los eigenvalores son igual/cercano a 1 ( en este caso)
r_eigenvectores = eigenvectores[:, val_close1] #Toma los eigenvectores de las columnas que sean true en la matriz booleana.

distrib_estacionaria = r_eigenvectores/sum(r_eigenvectores) #Fórmula de distribución estacionaria
print("Distribución Estacionaria: " + str(distrib_estacionaria))

sum = 0
for p in range(9):
    sum += distrib_estacionaria[p]
print("Sum distrib_estacionaria: " + str(sum))