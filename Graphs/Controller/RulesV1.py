from IRules import IRules

class RulesV1(IRules):

    def __init__(self):
        self.__rules = ['exit','help','create_graph','get_names','delete_graph','graph_update_add_edge',
                        'graph_update_delete_edge','graph_update_add_vertex','graph_update_delete_vertex',
                        'graph_update_is_in_graph','show_graph']
    def get_rules(self) -> list:
        return self.__rules

