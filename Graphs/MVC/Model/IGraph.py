from abc import ABC, abstractmethod
class IGraph(ABC):

	@abstractmethod
	def __init__(self, vertex_count: str) -> None:
		pass
	@abstractmethod
	def add_edge(self, first_vertex: int, second_vertex: int) -> None:
		pass

	@abstractmethod
	def delete_edge(self, first_vertex: int, second_vertex: int) -> None:
		pass

	@abstractmethod
	def add_vertex(self, vertex: int) -> None:
		pass

	@abstractmethod
	def delete_vertex(self, vertex: int) -> None:
		pass

	@abstractmethod
	def is_in_graph(self, vertex: int) -> bool:
		pass

