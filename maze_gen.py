'''
	Author : Abhinaya Ramachandran
	Python Version : 2.7.11
	Created : 18th October, 2017 
'''

import a_star as a
import data_structures as ds

def generate_solve_maze(size, maze_values):
	'''
		Constructs a graph from the given maze maze_values and 
		calls the method to solve the maze

		param size : The  number of rows and columns in the array
		type size : list[int]

		param maze_values: Feature codes of the maze
		type maze_values: list[int]

		return: List of nodes and how they were reached, 
                         List of costs

            	rtype: dict [string] string , dict[string]int
	'''
	l,w = size
	i = 0
	given = []

	# Constructs a matrix from the given values
	while i < len(maze_values):
		given.append(maze_values[i : i+w])
		i += w
	id = 0

	'''
		The matrix is read from left to right and top to bottom. A graph adjacency list with the list of neighbors for
		each node is created. Since the nodes to the right and the bottom are unknown at the time a particular node
		is read, the conditions are checked again when a node is open to the left or top.

		Mines are added in a list, so that they can be used by the path finding algorithm later.

		Each node is given a numerical id except for the start and end nodes that are represented by a "S" and an "E"
		respectively. This enables back tracking the solution by pulling the path from  "E" to "S".

		As each node is created it is also added to a list of nodes. 

	'''

	feature_codes = {"UP":1, "RIGHT":2, "DOWN":4, "LEFT":8, "START":16, "END":32, "MINE":64}


	print ("Constructing the maze...")

	input_graph = ds.Graph()
	for r in xrange(l):
		for c in xrange(w):
			n = ds.Node(r, c)
			if given[r][c] & feature_codes["START"] :
				n.assign_id("S", given[r][c])


			if given[r][c] & feature_codes["END"]:
				n.assign_id("E", given[r][c])


			if given[r][c] & feature_codes["LEFT"]:
				if not n.hasId():
					n.assign_id(id, given[r][c])
				res = input_graph.get_neighbor(r, c-1, l, w)
				if res:
					input_graph.add_neighbor(n.get_node_id(), res)
					if res.given_val & feature_codes["RIGHT"]:
						input_graph.add_neighbor(res.get_node_id(), n)


			if given[r][c] & feature_codes["RIGHT"]:
				if not n.hasId():
					n.assign_id(id, given[r][c])
				res = input_graph.get_neighbor(r, c+1, l, w)
				if res:
					input_graph.add_neighbor(n.get_node_id(), res)


			if given[r][c] & feature_codes["UP"]:
				if not n.hasId():
					n.assign_id(id, given[r][c])
				res = input_graph.get_neighbor(r-1, c, l, w)
				if res:
					input_graph.add_neighbor(n.get_node_id(), res)
					if res.given_val & feature_codes["DOWN"]:
						input_graph.add_neighbor(res.get_node_id(), n)


			if given[r][c] & feature_codes["DOWN"]:
				if not n.hasId():
					n.assign_id(id, given[r][c])
				res = input_graph.get_neighbor(r+1, c, l, w)
				if res:
					input_graph.add_neighbor(n.get_node_id(), res)


			if given[r][c] & feature_codes["MINE"]:
				if not n.hasId():
					n.assign_id(id, given[r][c])
				input_graph.add_mine(n.get_node_id())

			input_graph.nodes[n.get_node_id()] = n
			id += 1
	

	print ("Finding the path ...")

	came_from, cost_so_far= a.a_star_search(input_graph, "S", "E" )
	if came_from == None or cost_so_far == None:
		print "Unable to find path"
		return


	b = []
	c = "E"
	b.append (c)
	while(c != None):
	    c = came_from[c]
	    if c == None:
	    	b.append("S")
	    else:
	    	b.append(c)
	b = b[::-1] #reversing the array

	print ("The steps to be followed are: ")
    	for k in xrange(0, len(b)-1):
    		step = get_steps(input_graph, b[k], b[k+1])
    		if step != None:
    			print "->"+step
    	return came_from, cost_so_far # Return value here is used in the unit test

	

def get_steps(graph, node1 , node2):
	'''
		Returns the steps taken based on the  
		coordinates of the nodes in returned by 
		the A star algorithm

		param graph : The graph containing the result nodes
		type graph : Graph

		param node1, node2 : The successive nodes
		type node1, node2 : Node, Node

		return : The turn to be made
		rtype: string
	'''
	x1 = graph.nodes[node1].x
	y1 = graph.nodes[node1].y
	x2 = graph.nodes[node2].x
	y2 = graph.nodes[node2].y
	if y2 > y1:
		return "right"
	if y2 < y1:
		return "left"
	if x2 > x1:
		return "down"
	if x1 > x2:
		return "up"



	