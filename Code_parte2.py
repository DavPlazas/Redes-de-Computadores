import csv
import random
import time
import pandas as pd
import numpy as np
from math import inf
import networkx as nx
import time



import matplotlib.pyplot as plt

def ejecucion():

    print("¿Desea cargar datos desde un archivo CSV? [Y/N]: ")
    respuesta = input()
    validas = ["Y","N"]
    
    if respuesta not in validas:
        a = 0
        while a == 0:
            print("Por favor responda con Y (Si) o N (No): ")
            respuesta = input()
            if respuesta in validas:
                a = 1
    
    if respuesta == "Y":
        print("Digite el nombre del archivo csv. (No olvide escribir la extensión .csv)")
        archivo = input()
        with open(archivo) as f:
            reader = csv.reader(f, delimiter = ";")
            matrix_aux = []
            
            for i in reader:
                arista = []
                arista.append(i[0])
                arista.append(i[1])
                arista.append(i[2])
                matrix_aux.append(arista)
            
            matrix_aux.pop(0)
            m = np.array(matrix_aux)
            
            nodos = set()
            for i in m:
                #for j in i:
                    nodos = nodos | set(i[0])| set(i[1])
                   # print(set(j[0]))
            n = list(nodos)
        a = len(n)
        inicio = time.time()
        
        return m, a ,n, inicio
    
    if respuesta == "N":
        validas2 = list(range(15, 51))
        print("Digite el número de nodos para el grafo (entre 15 y 50): ")
        try:
            respuesta2 = int(input())
        except:
            respuesta2 = 0
        if respuesta2 not in validas2:
            a = 0
            while a == 0:
                print("Por favor responda con un número entre 15 y 50: ")
                try:
                    respuesta2 = int(input())
                except:
                    respuesta2 = 0
                if respuesta2 in validas2:
                    a = 1
        num_nodos = respuesta2
    
    inicio = time.time()
    num_aristas = num_nodos + int(num_nodos/2)
    
    #print(num_aristas)
    
    
    nodos =  list(range(1, num_nodos + 1))
    # for i in range (0,len(nodos)):
    #     nodos[i] = str(nodos[i])
    
    nodos2 = []
    
  
    matrix_aux = []
    sin_bucles = {}
    
    o = 1
    
    for i in range(1,num_nodos):

        nodos.remove(o)
        nodos2.append(o)
        arista = []
        arista.append(o)
        peso = random.randint(1, 16)
        arista.append(peso)
        d = random.choice(nodos)
        arista.append(d)
        sin_bucles[o] = d
        o = d
        matrix_aux.append(arista)
    
    faltantes = num_aristas - num_nodos
    
    o = d
    nodos2.append(o)
    sin_bucles2 = {}
    sin_bucles[o] = 0
    nodos3 = []
    
    for i in range(1,faltantes + 1):
        nodos2.remove(o)
        nodos3.append(o)
        arista = []
        arista.append(o)
        peso = random.randint(1, 16)
        arista.append(peso)
        d = random.choice(nodos2)
        while d == sin_bucles[o]:
            d = random.choice(nodos2)
        arista.append(d)
        sin_bucles2[o] = d
        o = d
        matrix_aux.append(arista)
      
    for i in range(0,num_nodos-12):
        matrix_aux.append([1,random.randint(10,num_nodos),random.randint(1, 16)])
        
    matrix_aux.append([int(num_nodos/2),random.randint(10,num_nodos),random.randint(1, 16)])
    
    Nodos = []
    Nodos =  list(range(1, num_nodos + 1))


    
    m = np.array(matrix_aux)
    
    return m, num_nodos, Nodos, inicio

def dijkstra2(E,start,end):
    S = E
    L = {}
    Pred = {}
    camino = []
    
    for i in S:
        L[i] = inf
    L[start] = 0
    B = L.copy()
    #NodA = set()
    
    iteracion = 0
    while len(S) > 0:
        
        inicio_iter = time.time()
        iteracion += 1
        nodo =[x for x in B.keys() if L[x]==min(B.values())][0]
        
        #nodo = [x for x in L.keys() if L[x]==  min(set(L.values()) - NodA) and x in S][0]
        #NodA.add(nodo)
        
        for edge, weight in E[nodo].items():
            comp = weight + L[nodo]
            if comp < L[edge]:
                L[edge] = comp
                B[edge] = comp
                Pred[edge] = nodo
        S.pop(nodo)
        B.pop(nodo)
        final_iter = time.time()
        tiempo_iter = final_iter - inicio_iter 
        
    
    
    ubicacion = end
    
    while ubicacion != start:
        try:
            camino.append(ubicacion)
            ubicacion = Pred[ubicacion]
        except KeyError:
            print("No existe un camino del nodo " + start + " a el nodo " + end )
            break
    camino.append(start)
    camino = camino[::-1]
    if L[end] != inf:
         return camino, L[end], iteracion, tiempo_iter
    
    else:
        camino = []
        return camino, inf, iteracion, tiempo_iter


def dibujaGrafos(E):
    aristas = []
    aristas_peso = []
    nodos = []
    for i in E:
        valor = E.get(i)
        for j in E.get(i):
            aristas.append((i,j))
            nodos.append(i)
            nodos.append(j)
            aristas_peso.append((i,j,valor.get(j)))
            
            
    #print(aristas)
    #print(aristas_peso)
            
    
    G = nx.DiGraph()
    #G.add_edges_from(aristas)
    
    for i in aristas_peso:
        G.add_edge(i[0], i[1], weight = i[2])
    
    val_map = {'a': 1.0,
                'b': 0.5714285714285714,
                'c': 0.0
                }
    
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    
    edge_colours = ['black' for edge in G.edges()]
    black_edges = [edge for edge in G.edges()]
    
    labels = nx.get_edge_attributes(G, "weight")
    
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = 'yellow', node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    
def Matrix_to_dictionary(m,n):
    
    grafo = {}


    for i in range(1,n+2):
        grafo[str(i)] = dict()
        
    for i in m:
        for j in grafo:
            if str(i[0]) == j:
                grafo[j].update({str(i[1]):int(i[2])})
        
    return grafo

def dibujaArbole(P,Graphy):
    G = nx.DiGraph()
    aristas_peso = []
    
    nodos = {}
    for j in P:    
        E_resultado = {}
        for i in range (0,len(j[0])-1):
            E_resultado[j[0][i]] = j[0][i+1] 
            if i +1 == len(j[0])-1:
                nodos[j[0][i+1]] = j[1]
    
        aristas = []
        #aristas_peso = []
        #nodos = []
        for i in E_resultado:
            aristas.append((i,E_resultado.get(i)))
            aristas_peso.append((i,E_resultado.get(i),Graphy[i][E_resultado.get(i)]))
            #aristas_peso.append((i,j,valor.get(j)))
                
        for i in aristas_peso:
            G.add_edge(i[0], i[1], weight = i[2])
                
    
        #G.add_edges_from(aristas)
    
    #print(nodos)
    
    # for i in aristas_peso:
    #     G.add_edge(i[0], i[1], weight = i[2])
    
    val_map = {'a': 1.0,
                'b': 0.5714285714285714,
                'c': 0.0
                }
    
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    
    edge_colours = ['black' for edge in G.edges()]
    black_edges = [edge for edge in G.edges()]
    
    labels = nx.get_edge_attributes(G, "weight")
    
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = 'yellow', node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def tabla_enrutamiento(resultados):
    matrix_aux = []
    nombres = ['Nodo','Distancia','Antecesor']
    for i in resultados:
        try:
            arista = []
            arista.append(i[0][len(i[0])-1])
            arista.append(i[1])
            arista.append(i[0][len(i[0])-2])
    
            matrix_aux.append(arista)
        except:
            pass
    

    fig, ax =plt.subplots(1,1)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=matrix_aux,colLabels=nombres,loc="center")
    plt.show()
    

m,n,nodos,inicio = ejecucion()

print()
print("Matriz dispersa del grafo: ")
print()
print(m)


dibujaGrafos(Matrix_to_dictionary(m, n))

resultados = []
for i in nodos:
    copia = Matrix_to_dictionary(m, n).copy()
    a,b,c,d = dijkstra2(copia,'1',str(i))
    resultados.append((a,b))
    
#print(resultados)
dibujaArbole(resultados,Matrix_to_dictionary(m, n))

print()

tabla_enrutamiento(resultados)


final = time.time()

tiempo_total = final-inicio

print("En la sección gráficos, encontrará el grafo original, el árbol final con rutas más corta y la tabla de enrutamiento final.")
print()
print("Se realizaron " + str(c) + " iteraciones para el algortimo de Dijkstra.")
print()
print("El tiempo de la ejecución total, en segundos, es: " + str(tiempo_total))
print()
print("El tiempo de cada iteración, en segundos, es: " + str(d))

