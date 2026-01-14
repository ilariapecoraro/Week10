import networkx as nx
import flet as ft

# COME CREARE UN GRAFO

# GRAFO SEMPLICE
g = nx.Graph()

# FUNZIONE ADD_NODE
g.add_node(1) # funzione che mi permette di aggiungere un nodo a un grafo
# g.add_node("abc") # se volessi aggiungere come nodo una stringa
# a = Amico(2345, "M.Rossi")
# g.add_node(a) # posso aggiungere un oggetto
g.add_node(2)
g.add_edge(1, 2, attributo = "Pippo") # scelgo io qualunque attributo io vogli dare

# se i nodi che ho creato non esistono, li aggiungo
g.add_edge(2,3) # crea automaticamente il nodo 3 ancora inesistente
# riscrivere due volte lo stesso arco non ha alcun effetto su un grafo semplice
g.add_edge(2,3)
print(f"Arco tra 1 e 2: {g[1][2]}")

# potrei aggiungere anche insiemi di nodi e archi
altri_nodi = [4, 5, 8, 6, 7]
# sono riportati nell'ordine di inserimento:
# li rappresenta come dei dizionari: viene mantenuto l'ordine di inserimento
g.add_nodes_from(altri_nodi) # riceve una lista di nodi
# posso aggiungere anche una lista di archi
altri_archi = [ (2,4), (4,5), (6,7), (6,8), (1,4) ] # lista di tuple
g.add_edges_from(altri_archi)

# PER STAMPARE
print(g) # output: Graph with 8 nodes and 7 edges
# si descrive in inglese, ma non mi dà informazioni sui dettagli

# PER SAPERE I NODI
# esiste un attributo chiamato nodes
print(g.nodes) # stampa gli oggetti di tipo nodo

# PER SAPERE GLI EDGES
# attributo edges
print(g.edges)

# NODI COME DIZIONARI

primo_nodo = g[1] # Dizionario: nodo che ha quella chiave
print(primo_nodo) # mi stampa un altro dizionario
# output: due nodi collegati (2,4) al nodo 1, poi tra i due ci sono le informazioni sugli attributi

# FUNZIONI CHE POSSIAMO USARE SUI GRAFI

# 1) funzione per verificare se un arco/nodo esista nel grafo
# uso operatore in
if 12 in g:
    print("Nodo presente")
else:
    print("Nodo assente")

# 2) possiamo anche iterare sui grafi
# ricordiamo che è un dizionario
for nodo in g:
    print(nodo)

# 3) potremmo ciclare sui nodi vicini
print("Stampo i vicini del nodo 1")
for nodo in g[1]:
    print(nodo)

# 4) se voglio calcolare la densità del grafo
densità = nx.density(g)
print(f"Densità: {densità}")

# possiamo creare anche altri grafi

# GRAFO DIRETTO
dg = nx.DiGraph()
dg.add_nodes_from(altri_nodi)
dg.add_edges_from(altri_archi)
print(dg.nodes)
print(dg.edges)
print(dg[4]) # mi dice che esiste un arco verso 5
print(dg[5]) # mi dice che non esistono archi
# perchè il grafo è diretto

# MULTI GRAPH
mg = nx.MultiDiGraph()
mg.add_edge(1,2, weight = 5) #0
# scrivere più volte lo stesso arco ha invece effetto su un grafo multiplo
mg.add_edge(1,2)#1
mg.add_edge(1,2)#2
# se invece qua lo scrivo più volte
print(mg[1])
# stampa: chiave(2): valori( chiave(0): attributo dell'arco 0, chiave(1): attributo arco 1,chiave(2): attributo chiave 2)
print(f"Arco tra 1 e 2 in posizione 0: {mg[1][2][0]}")

# in generale c'è la documentazione con tutte le istruzioni