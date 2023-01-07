from GraphFabric import GraphFabric

class GraphCollection():
    
    def __init__(self):
        self.__graph_dict = {}
        self.__commands = {'create_graph':self.create_graph, 'get_names':self.get_names,
                         'delete_graph':self.delete_graph, 'graph_update':self.update_graph, 
                         'show_graph':self.show_graph}
    def create_graph(self, name: str, type: str, vertex_count: int) -> None:
        graph = GraphFabric.create_graph(vertex_count, type)
        if name not in self.__graph_dict.keys():
            self.__graph_dict[name] = graph
        else:
            raise ValueError(f'graph named {name} already exist!')

    def get_names(self) -> list:
        return self.__graph_dict.keys()

    def delete_graph(self, name: str) -> None:
        if name in self.__graph_dict.keys():
            self.__graph_dict.pop(name)
        else:
            raise KeyError(f'graph named {name} does not exist!')

    def show_graph(self, name: str) -> dict:
        print(self.__graph_dict[name].vertex_dict)
        return self.__graph_dict[name].vertex_dict

    def update(self, upd_type: str, upd_values = []):
        value = None
        length = len(upd_values)
        if upd_type in self.__commands.keys() or 'graph_update' in upd_type:
            if 'graph_update' in upd_type:
               value = self.__commands['graph_update'](upd_type, upd_values) 
            else:
                if length==0:
                    value = self.__commands[upd_type]()
                elif length==1:
                    value = self.__commands[upd_type](upd_values[0])
                elif length==3:
                    value = self.__commands[upd_type](upd_values[0],upd_values[1],upd_values[2])
        return value

    
    def update_graph(self, upd_type : str, upd_values = []):
        name = upd_values[0]
        value = self.__graph_dict[name].update(upd_type, upd_values[1:])
        return value