# Graphs-collection
It's a small pet-project that I created to try to make an MVC-app. 
## About architecture
So, as I said, it's an MVC-app. There are three general folders: 'MVC', 'interfaces' and 'main'.    

The 'MVC' folder includes a 'Model' folder, a 'View' folder and a 'Controller' folder.  

The 'Model' folder contains two interfaces: 'IGraph' and 'IModel'. Realizations of the first one are 'DirectedGraph' & 'UndirectedGraph', realization of the second one is 'Model'. 'GraphFabric' is a simple fabric of graphs; 'GraphCollection' is a collection of graphs.   
The 'View' folder contains three interfaces: 'IInput', 'IOutput' and 'IView'. It contains realization of them too: InputV1, OutputV1 and View.   
The 'Controller' folder contains four interfaces: 'IRules', 'INormalizator', 'IValidator' and 'IController'. Realizations of them are RulesV1, NormalizatorV1, ValidatorV1 and Controller. RulesV1 is a simple wrapper for a list that includes implemented commands; ValidatorV1 uses RulesV1 and makes sure that command inputted by user is implemented in the app; NormalizatorV1 forces command written by user to be formatted as required by the app.  

The 'interfaces' folder includes two interfaces: 'IObserver' and 'IObservable'. It's a simple realization of observer pattern. It also includes 'Interface' module that combines that two interfaces.   

The 'main' folder contains 'MVC' module that includes MVC to the 'main.py' and 'main.py'.   

## What can program do?
To be honest, nothing really special. It's a training project. But there are some commands:  
create_graph [name of graph] [type*] [count of vertex] - create a new graph  
*supported types: Undirected, Directed*  
get_names - get names of all graphs  
delete_graph [name of graph] - delete a graph  
graph_update_add_edge [name of graph] [first vertex] [second vertex] - create a new edge between first and second vertexes  
graph_update_delete_edge [name of graph] [first vertex] [second vertex] - delete an edge between first and second vertexes  
graph_update_add_vertex [name of graph] [vertex] - create a new vertex  
graph_update_delete_vertex [name of graph] [vertex] - delete the vertex  
graph_update_is_in_graph [name of graph] [vertex] - check if vertex named [vertex] exist in graph  
show_graph [name_of_graph] - show the list of graph  
help - show help  
exit - exit the program  
