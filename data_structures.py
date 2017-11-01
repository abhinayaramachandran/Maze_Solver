
'''
	Author : Abhinaya Ramachandran
	Python Version : 2.7.11
	Created : 18th October, 2017 
'''

'''
	Graph specific data - nodes, edges, mines
	Node specific data - row and column positions in the maze
				 - node id ,  the feature code associated 
				 with the node
	Priority Queue - used to determine the next path/ neighbor
	                             to traverse

'''




from collections import defaultdict
import heapq

class Graph:
	def __init__(self):
		# A dictionary of node and a list of neighbors 
		self.edges = defaultdict(list)
		# Dictionary of all the nodes
		self.nodes = {}
		# Mines ,  ids of the mines
		self.mines = []

	def neighbors(self, id):
		return self.edges[id]

	def add_neighbor(self, node, neighbor):
		self.edges[node]. append(neighbor)
			
	def get_neighbor(self, x, y, l, w):
		if 0 <= x < l and  0 <= y < w:
			for n in self.nodes.itervalues():
				if n.x == x and n.y == y:
					return n
			return None

	def add_mine(self, mine):
		self.mines.append(mine)

	def get_edges(self):
		return self.edges


class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.id_no = -1
		self.given_val = -1

	def  assign_id(self, id, given_val):
		self.id_no = id # Each node has a unique id
		self.given_val = given_val

	def hasId(self):
		return self.id_no != -1

	def get_node_id(self):
		return self.id_no


class PriorityQueue:
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0

	def put(self, item, priority = 0):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]



