import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        # il controller chiede al model di farlo
        self._model.crea_grafo(e)
        pass

    def handleCercaRaggiungibili(self,e):
        pass

    def populate_dropdown(self,dd):
        # dobbiamo chiedere al model di fornire tutte le fermate
        self._model.get_all_fermate()
        # le fermate le trovo nel model, in _lista_fermate

        for fermata in self._model._lista_fermate:
        # per popolare le dropdown con chiave, valore
            dd.options.append(ft.dropdown.Option( key= fermata.id_fermata,
                                                  text= fermata.nome))
