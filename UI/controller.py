import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        nazioni = self._model.get_nazioni()
        for c in nazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))


    def handle_graph(self, e):
        anno = int(self._view.ddyear.value)
        nazione = self._view.ddcountry.value
        self._model.crea_grafo(nazione, anno)
        num_nodi = self._model.num_nodi()
        num_archi = self._model.num_archi()
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {num_nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {num_archi}"))
        self._view.update_page()



    def handle_volume(self, e):
        diz = self._model.volume_vendita()
        for retailer, volume in diz.items():
            self._view.txtOut2.controls.append(ft.Text(f"{retailer} --> {volume}"))
        self._view.update_page()


    def handle_path(self, e):
        numero = int(self._view.txtN.value)
        costo, ciclo = self._model.get_ciclo_max(numero)
        print(costo)
        for n in ciclo:
            print(n)

