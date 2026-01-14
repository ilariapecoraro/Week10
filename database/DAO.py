from database.DB_connect import DBConnect
from model.fermata import Fermata
from model.connessione import Connessione

class DAO():
    pass

    # neanche il DAO ha le fermate
    @staticmethod
    # è un metodo statico: quando mi serve lo chiamo, senza passare all'oggetto stesso
    # DIFFERENZA: metodo statico = della classe stessa, metodo di istanza = dipende dall'oggetto specifico
    def read_all_fermate():
        connessione = DBConnect.get_connection()
        result = []
        # devo leggere tutte le info
        query = """SELECT * FROM Fermata"""
        cursor = connessione.cursor(dictionary=True)
        # cursore di tipo dizionario
        cursor.execute(query) # così prendo il dizionario,
        # non ho parametri quindi non mi serve mettere tuple con i parametri

        for row in cursor:
            fermata = Fermata(row["id_fermata"], row["nome"], row["coordX"], row["coordY"])
            result.append(fermata) # appendo il risultato
            print(row)
        cursor.close()
        connessione.close()
        return result     # così il DAO restituisce una lista di oggetti di tipo Fermata (DTO)

    #  PER IL SECONDO METODO: query che fa già la selezione
    @staticmethod # così non metto il self
    def exists_conn_tra(u : Fermata, v : Fermata): # fermate
        # verifica se esiste una connessione tra nodo u e v
        conn = DBConnect.get_connection()
        result = []
        query = """ SELECT * 
                    FROM connessione c
                    WHERE c.id_stazP = %s AND
                    c.id_stazA = %s
                    """

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata, v.id_fermata)) # Parametri
        for row in cursor:
            result.append(row)
            print(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def search_vicini_a_fermata(u : Fermata):
    # anzi che fare 619 * 619 query per verificare se esista un arco
            # """ SELECT *
            # FROM connessione c
            # WHERE c.id_stazP = %s
            # """
    # io prendo le 619 fermate e chiedo le stazioni di connessione che hanno (leggo le fermate)
    # quindi cerco le fermate collegate a quella passata come parametro
    # così riduco il tempo
    # il numero di righe che ho nel risultato mi dice quante connessioni ho
    # se metto il count, scopro quante connessioni ho "SELECT COUNT(*)"
        conn = DBConnect.get_connection()
        result = []
        query = """ SELECT * FROM connessione c 
                WHERE c.id_stazP = %s"""

        cursor = conn.cursor(dictionary=True)
        # cursore di tipo dizionario
        cursor.execute(query, (u.id_fermata,))  # Parametro con (, )
        # Parametri (a noi interessano gli id di quella fermata)

        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])

            result.append(connessione)  # appendo il risultato
            print(row)
        cursor.close()
        conn.close()
        return result

    # SELECT * FROM connessione
    # prende anche le connessione ripetute, ma noi abbiamo un grafo semplice

    # SELECT distinct id_stazP, id_stazA from connessione
    # grafo non direzionale
    # dobbiamo modificare il nostro grafo: costruire un DiGraph(), ovvero un grafo diretto
    # con archi bidirezionali

    # TERZO MODO, con una query senza parametri
    # leggo tutte le connessioni dalla tabella connessioni, crea oggetti connessione e restituisce
    # una lista di quegli oggetti

    @staticmethod
    def read_all_connessioni():
        conn = DBConnect.get_connection()
        result = []
        query = """ SELECT * FROM connessione c
                    """

        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)

        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])

            result.append(connessione)  # appendo il risultato
            print(row)
        cursor.close()
        conn.close()
        return result

    # per avere le info sulle linee: non c'è bisogno di fare una classe linea

    def read_velocità(id_linea):
        connessione = DBConnect.get_connection()
        result = []
        query = """SELECT * FROM linea WHERE id_linea = %s"""
        cursor = connessione.cursor(dictionary=True)
        # cursore di tipo dizionario
        cursor.execute(query, (id_linea, ))
        for row in cursor:
            # prendo solo la colonna velocità
            result.append(row["velocità"]) # appendo il risultato
            print(row)
        cursor.close()
        connessione.close()
        return result[0]
        # restituisco solo la prima riga, perchè tanto c'è una sola riga oer ogni id_linea
        # so già che le altre righe saranno vuote
