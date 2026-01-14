# graph

# molti algoritmi che si basano sui graph sono risolvibili attraverso algoritmi RICORSIVI
# graph semplici: graph in cui ci sono dei nodi collegati da archi che non hanno una direzione
# esempio: metro di una città in cui i nodi sono le stazioni e gli archi sono i collegamenti
# di una linea di un determinato colore
# tra i nodi di un graph ci possono essere due o più linee che collegano le stazioni
# multigraph: più archi tra due nodi

# attributi sugli archi: potrebbero essere la velocità della linea, la lunghezza del collegamento,
# la frequenza dei treni ecc...
# vertice adiacente se esiste un collegamento, possono essere anche isolati
# grado: somma archi entranti e uscenti

# cicli: è possibile andare da un vertice, a uno stesso vertice
# albero: graph senza cili, foreste: insieme di alberi
# graph pesati hanno delle etichette

# quando voglio rappresentare un nodo uso gli oggetti, mentre quando voglio rappresentare
# un agge scrivo (V1,V2)

# Network x: libreria attraverso cui possiamo creare dei graph
# è possibile accedere a un nodo e avere informazioni
# possiamo memorizzare nodi e age di tipo diverso: veri e propri oggetti di classe