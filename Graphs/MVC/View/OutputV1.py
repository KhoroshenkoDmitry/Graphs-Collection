from IOutput import IOutput

class OutputV1(IOutput):
    
    def __init__(self):
        self.__commands = {'create_graph':self.create_graph, 'get_names':self.get_names,
                         'delete_graph':self.delete_graph,'show_graph':self.show_graph, 
                         'graph_update_add_edge':self.graph_update_add_edge,'graph_update_delete_edge':self.graph_update_delete_edge,
                         'graph_update_add_vertex':self.graph_update_add_vertex,'graph_update_delete_vertex':self.graph_update_delete_vertex, 
                         'graph_update_is_in_graph':self.graph_update_is_in_graph,'show_graph':self.show_graph, 'help':self.help}
    def hello(self) -> None:
        string = 'Hello and welcome to "Graph Collection". This app is made as a pet-project, the author wanted to try to make MVC-app. \
        \nIf you do not know the commands, type "help".'
        self.output(string)
    
    def help(self) -> None:
        string = 'HELP: \
        \ncreate_graph [name of graph] [type*] [count of vertex] - create a new graph  \
        \n*supported types: Undirected, Directed \
        \nget_names - get names of all graphs \
        \ndelete_graph [name of graph] - delete a graph \
        \ngraph_update_add_edge [name of graph] [first vertex] [second vertex] - create a new edge between first and second vertexes \
        \ngraph_update_delete_edge [name of graph] [first vertex] [second vertex] - delete an edge between first and second vertexes \
        \ngraph_update_add_vertex [name of graph] [vertex] - create a new vertex \
        \ngraph_update_delete_vertex [name of graph] [vertex] - delete the vertex \
        \ngraph_update_is_in_graph [name of graph] [vertex] - check if vertex named [vertex] exist in the graph \
        \nshow_graph [name_of_graph] - show the list of the graph \
        \nhelp - show help \
        \nexit - exit the program'
        self.output(string)

    def create_graph(self, name: str, type: str, vertex_count: str) -> None:
        string = f'{type} graph {name} with {vertex_count} vertex(-es) succefully created!'
        self.output(string)

    def get_names(self, names: list) -> None:
        string = 'Names:'
        for name in names:
            string += f'\n{name}'
        self.output(string)

    def delete_graph(self, name: str) -> None:
        string = f'graph {name} succefully deleted!'
        self.output(string)

    def graph_update_add_edge(self, graph: str, vertex1: str, vertex2: str) -> None:
        string = f'edge between vertex {vertex1} and vertex {vertex2} in graph {graph} suceffully added!'
        self.output(string)

    def graph_update_delete_edge(self, graph: str, vertex1: str, vertex2: str) -> None:
        string = f'edge between vertex {vertex1} and vertex {vertex2} in graph {graph} suceffully deleted!'
        self.output(string)

    def graph_update_add_vertex(self, graph: str, vertex: str) -> None:
        string = f'vertex {vertex} in graph {graph} succefully added!'
        self.output(string)

    def graph_update_delete_vertex(self, graph: str, vertex: str) -> None:
        string = f'vertex {vertex} in graph {graph} succefully deleted!'
        self.output(string)

    def graph_update_is_in_graph(self, graph: str, vertex: str, flag: bool) -> None:
        if flag == True:
            string = f'vertex {vertex} in graph {graph} exist!'
        else:
            string = f'vertex {vertex} in graph {graph} does not exist!'
        self.output(string)

    def show_graph(self, name: str, graph: dict) -> None:
        string = f'graph {name} looks like: \n'
        for vertex in graph.keys():
            string += f'{vertex} ->'
            if len(graph[vertex])!=0:
                for out in graph[vertex]:
                    string+=f' {out}'
            else:
                string += ' nothing'
            string += '\n'
        self.output(string)

    def update(self, upd_type: str, upd_values=[]) -> None:
        length = len(upd_values)
        if length==0:
            self.__commands[upd_type]()
        elif length==1:
            self.__commands[upd_type](upd_values[0])
        elif length==2:
            self.__commands[upd_type](upd_values[0],upd_values[1])
        elif length==3:
            self.__commands[upd_type](upd_values[0],upd_values[1],upd_values[2])

    def output(self, string: str) -> None:
        print(string)
        print()

