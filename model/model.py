import networkx as nx

import database.DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self, anno, shape):
        self.graph.clear()
        states = database.DAO.DAO().getStates()
        # Nodi
        for s in states:
            self.graph.add_node(s.id)
            self.idMap[s.id] = s
        # Archi
        for n in states:
            if n.Neighbors != None:
                vicini = n.Neighbors.split(' ')
                for i in vicini:
                    if not self.graph.has_edge(n.id, i):
                        self.graph.add_edge(n.id, i, weight="")
        # Pesi
        pesi = database.DAO.DAO().getPeso(anno, shape)
        for edge in self.graph.edges:
            peso = pesi[(edge[0], edge[1])]
            self.graph[edge[0]][edge[1]]['weight'] = peso
        return self.graph
