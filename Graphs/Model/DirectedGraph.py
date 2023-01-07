from calendar import firstweekday
from IGraph import IGraph

class DirectedGraph(IGraph):
    
    def __init__(self, vertex_count: str) -> None:
        dicts = {}
        keys = range(1,int(vertex_count)+1)
        for _ in keys:
            dicts[_] = [] 
        self.__vertex_dict = dicts
        self.__commands = {'graph_update_add_edge':self.add_edge, 'graph_update_delete_edge':self.delete_edge,
				'graph_update_add_vertex':self.add_vertex, 'graph_update_delete_vertex':self.delete_vertex,
				'graph_update_is_in_graph':self.is_in_graph}
    
    def add_edge(self, first_vertex: int, second_vertex: int) -> None:
        first_vertex = int(first_vertex)
        second_vertex = int(second_vertex)
        if second_vertex in self.__vertex_dict[first_vertex]:
            raise AttributeError(f'edge between {first_vertex} and {second_vertex} already exist!')
        else:
            self.__vertex_dict[first_vertex].append(second_vertex)

    def delete_edge(self, first_vertex: int, second_vertex: int) -> None:
        first_vertex = int(first_vertex)
        second_vertex = int(second_vertex)
        if second_vertex not in self.__vertex_dict[first_vertex]:
            raise AttributeError(f'edge between {first_vertex} and {second_vertex} does not exist!')
        else:
            self.__vertex_dict[first_vertex].remove(second_vertex)

    def add_vertex(self, vertex: int) -> None:
        vertex = int(vertex)
        if self.is_in_graph(vertex):
            raise AttributeError(f'vertex {vertex} already exist!')
        if vertex<=0:
            raise ValueError(f'{vertex} is equal or smaller than zero!')
        else:
            self.vertex_dict[vertex] = []

    def delete_vertex(self, vertex: int) -> None:
        vertex = int(vertex)
        if not self.is_in_graph(vertex):
            raise AttributeError(f'vertex {vertex} does not exist!')
        else:
            self.vertex_dict.pop(vertex)
            for _ in self.__vertex_dict.keys():
                if vertex in self.__vertex_dict[_]:
                    self.__vertex_dict[_].remove(vertex)

    def is_in_graph(self, vertex: int) -> bool:
        vertex = int(vertex)
        return  bool(vertex in self.__vertex_dict.keys())

    @property
    def vertex_dict(self) -> dict:
        return self.__vertex_dict
    
    def update(self, upd_type: str, upd_values = []):
        length = len(upd_values)
        if length==1:
            value = self.__commands[upd_type](upd_values[0])
        elif length==2:
            value =self.__commands[upd_type](upd_values[0], upd_values[1])
        return value


