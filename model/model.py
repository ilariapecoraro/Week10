import networkx as nx
from geopy.distance import geodesic

from database.DAO import DAO

class Model:
    def __init__(self):
        self._lista_di_fermate = []
        # dizionario di fermate (mappa di fermate)
        self._dizionario_fermate = {}
        self._grafo = None


    def get_all_fermate(self):
        # neanche il model ha le informazione sulle informazioni: le chiede al DAO
        fermate = DAO.read_all_fermate()
        # devo memorizzare le informazioni all'interno della classe model
        # uso una lista self._fermate per memorizzare
        self._lista_di_fermate = fermate
        for fermata in self._lista_di_fermate:
            self._dizionario_fermate[fermata.id_fermata] = fermata
            # così costruisco un dizionario di fermate,
            # con chiave id_fermata e valore l'oggetto fermata corrispondente

    def crea_grafo(self):
        self._grafo = nx.MultiGraph() # Posso avere più archi tra i nodi
        print(len(self._lista_di_fermate))
        for fermata in self._lista_di_fermate:
            self._grafo.add_node(fermata)
            # grafo semplice (no pesi e no archi multipli)

        # DOMANDE
        # è a senso unico? grafo orientato
        # è fa avanti e indietro ? grafo non orientato
        # tra due stazioni possono esserci più linee che le collegano? multi-grafo


        # PRIMO MODO DI AGGIUNGERE I NODI CON 619*619 QUERY SQL
        # modo lento

        """
        for u in self._grafo: # per ognuno dei 619 nodi
            for v in self._grafo: # per ognuno dei possibili nodi connessi
            # for v in self._grafo[u] sbagliato perchà ancora gli archi sono da aggiungere
            # nel valore del dizionario ci sono tutti i nodi a cui sono già connessi
            # come faccio a saperlo? devo chiederlo al database
                risultato = DAO.exists_conn_tra(u, v)
                if len(risultato) > 0: # c'è almeno una connessione e quindi creo un arco
                self._grafo.add_edge(u, v) # creo un arco
                print(f"Aggiunto arco tra {u} e {v}")
            """

        # SECONDO MODO DI AGGIUNGERE I NODI, CON 619 QUERY A CERCARE I NODI VICINI

        """
        for u in self._grafo:
            connessioni_vicini = DAO.search-vicini_a_fermata(u)
            # scandisco tutti i vicini
            for connessione in connessioni_vicini:
            
                # passaggio fondamentale !!!
                
                # connessione.id_stazA
                
                # questo è un id, ma a me serve un oggetto fermata che ho nella lista delle fermate
                # sarebbe meglio avere anche un dizionario delle fermate

                fermata_arrivo = self._dizionario_fermate[connessione.id_fermata]
                # così creo l' oggetto di tipo fermata
                self._grafo.add_edge(u, fermata_arrivo)
                print(f"Aggiunto arco tra {u} e {fermata_arrivo}")
                print(le(self._grafo.edges))
            """

        # COSTRUISCO UN GRAFO PESATO
        # TERZO MODO, con una sola query che estrae in un colpo solo tutte le connessioni

        """
        
        lista_connessioni = DAO.read_all_connessioni()
        for c in lista_connessioni:
            # dentro c ci sono gli id delle stazioni di partenza e arrivo,
            # ma attenzione! sono solo gli id, non gli oggetti stazione (che invece ho salvato nel dizionario)
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]
            # print(f"{self.esiste_arco(u_nodo, v_nodo)
            if self._grafo.has_edge(u_nodo, v_nodo): # c'è gia la funzione su nx
                self._grafo[u_nodo][v_nodo]["peso"] += 1
            else:
                self._grafo.add_edge(u_nodo, v_nodo, peso = 1)
            
            """

        # COSTRUISCO UN MULTI-GRAFO NEL QUALE IL PESO DEGLI ARCHI E' IL TEMPO DI PERCORRENZA
        lista_connessioni = DAO.read_all_connessioni()
        for c in lista_connessioni:
            # dentro c ci sono gli id delle stazioni di partenza e arrivo,
            # ma attenzione! sono solo gli id, non gli oggetti stazione (che invece ho salvato nel dizionario)
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]
            # print(f"{self.esiste_arco(u_nodo, v_nodo)
            # uso la funzione geodesic() che però ha bisogno di definire i punti con le loro coordinate
            punto_u = (u_nodo.coordX, u_nodo.coordY)
            punto_v = (v_nodo.coordx, v_nodo.coordY)
            distanza = geodesic(punto_u,punto_v).kilometres
            # questa funzione riceve anche l'unità di misura in cui vuole questi dati
            # partenza e l'oggetto arrivo e crea il grafo
            velocita = DAO.read_velocità(c._id_linea)
            print(f"Distanza: {distanza}, velocita: {velocita}")
            tempo_percorrenza = distanza / velocita * 60 # tempo di percorrenza in minuti
            self._grafo.add_edge(u_nodo, v_nodo, tempo = tempo_percorrenza)
            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}, peso: {self._grafo[u_nodo][v_nodo]}, tempo: {tempo_percorrenza}")
        print(self._grafo)

    # se io volessi calcolare il tempo di percorrenza: ho la distanza ma ho bisogno anche della velocità
    # nella tabella delle linee c'è scritto a che velocità va quella linea
