import flet as ft
import networkx as nx

import database.DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        self.graph = None

    def fillDD(self):
        anni =[]
        i = 0
        while i < 2014:
            i += 1
            if i >1913:
                anni.append(i)
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))

        shapes = database.DAO.DAO().getShape()
        for s in sorted(shapes, key=lambda x: x):
            self._view.ddshape.options.append(ft.dropdown.Option(s))
        self._view.update_page()


    def handle_graph(self, e):
        anno = self._view.ddyear.value
        shape = self._view.ddshape.value
        self.graph = self._model.buildGraph(int(anno), shape)
        self._view.txt_result.controls.append(ft.Text(f'Numero nodi: {len(self.graph.nodes)} Numero archi: {len(self.graph.edges)}'))
        mappa = {}
        for nodo in self.graph.nodes:
            tot = 0
            vicini = nx.all_neighbors(self.graph, nodo)
            for v in vicini:
                tot += self.graph[nodo][v]['weight']
            mappa[nodo] = tot
        for i in mappa:
            self._view.txt_result.controls.append(ft.Text(f'Nodo {i}, somma pesi su archi = {mappa[i]}'))
        self._view.update_page()
    def handle_path(self, e):
        pass