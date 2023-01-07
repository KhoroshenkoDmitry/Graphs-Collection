from IGraph import IGraph
from DirectedGraph import DirectedGraph
from UndirectedGraph import UndirectedGraph

class GraphFabric():

    types_dict = {'Undirected':UndirectedGraph, 'Directed':DirectedGraph}
    @classmethod
    def create_graph(self, vertex_count: int, graph_type = 'Undirected') -> IGraph:
        if graph_type in self.types_dict.keys():
            return self.types_dict[graph_type](vertex_count)
        else:
            raise IndexError(f'You can not use {graph_type} as type. \nYou can use: {self.types_dict.keys()}')
