from dataclasses import dataclass

@dataclass
class Amico:
    _id : str
    _nome : str

    def __str__(self):
        return f"{self._id} {self._nome}"

    # NECESSARIO
    # Per poter utilizzare l'oggetto come nodo di un grafo
    # se non è hashable non può essere utilizzato (univoci)
    def __hash__(self):
        return hash(self._id)