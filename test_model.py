from model.model import Model
# così vedo se sta funzionando

model = Model()
model.get_all_fermate()
print(model._lista_di_fermate)
# ci da delle info sul grafo (in questo caso ci dice che ha 619 nodi)
model.crea_grafo() # per vedere se funziona
# se voglio stampare il grado del mio grafo
for nodo in model._grafo.nodes:
    print(f"{nodo} grado :{model._grafo.in_degree(nodo)}")
    # questo metodo si trova su nx


