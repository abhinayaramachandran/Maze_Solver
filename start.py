
'''
	Author : Abhinaya Ramachandran
	Python Version : 2.7.11
	Created : 18th October, 2017 
'''

import maze_gen as maze
import sys

def start(name):
	'''
		Main function that reads the input file
		param name : name of the input file
		type  name : string
		return : List of nodes and how they were reached, 
                                     List of costs
                      rtype: dict [string] string , dict[string]int
	'''
	try :
		with open(name) as f :
			for line in f:
				print "*"*30
				contents = line.split("-")
				start = contents[0].find("(")
				end = contents[0].find(")")
				size = map(int, contents[0][start+1:end].split(","))
				print "Maze of size, {0} by {1}".format(size[0], size[1])
				
				start = contents[1].find("[")
				end = contents[1].find("]")
				maze_values = map(int, contents[1][start+1:end].split(","))
				a, b = maze.generate_solve_maze(size, maze_values)
				print "*"*30
			return a, b 
	except EnvironmentError:
		print "Error :Unable to read file !!"
		return None, None

start(sys.argv[1])