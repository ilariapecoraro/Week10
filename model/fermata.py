from dataclasses import dataclass

# classi create per rappresentare dei dati
@dataclass
class Fermata:
    _id_fermata : int
    _nome : str
    _coordX : float
    _coordY : float

    # metodo per leggere la fermata (getter)
    @property
    def id_fermata(self): # -> int (lo scrive pycharm ma superfluo)
        return self._id_fermata

    @property
    def nome(self): # -> str:
        return self.nome

    @property
    def coordX(self):
        return self._coordX

    @property
    def coordY(self):
        return self._coordY

    def __str__(self):
        return f'Fermata({self.id_fermata}, {self.nome}, {self.coordX}, {self.coordY})'

    def __hash__(self):
        return hash(self.id_fermata)
        # hash della chiave: in questo modo siamo sicuri che la chiave sia univoca
        # e può essere inserita nel nodo del grafo

