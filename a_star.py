''' 
        Author : Abhinaya Ramachandran
        Python Version : 2.7.11
        Created : 18th October, 2017 
        Reference A* algorithm : https://www.redblobgames.com/pathfinding/a-star/introduction.html
'''


import data_structures as ds

def weight(a, b):

    '''
            A star algorithm keeps track of the distance 
            from the destination . 

            param a, b : source and destination nodes
            type a, b: Node, Node
            return :  distance 
            rtype : int
    '''
    (x1, y1) = a.x , a.y
    (x2, y2) = b.x , b.y
    return abs(x1-x2) + abs(y1-y2)

def a_star_search(graph, start, goal):
    '''
            The solution to the maze is determined here.
            At each point node a bfs is perfomed and weights
            are maintained. The path with the least weight is tracked.
            

            param start, goal: start and goal fields
            type start, goal : string

            return: List of nodes and how they were reached, 
                         List of costs

            rtype: dict [string] string , dict[string]int

    '''
    lives = 3
    queue = ds.PriorityQueue()
    queue.put(start, 0)
    came_from ,cost_so_far = {}, {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not queue.empty():
        current = queue.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next in  graph.mines:
                lives -= 1
                if lives == 0:
                    print "Stepped on a mine again , Sorry!!, no lives remaining, Game Over"
                    return None, None
                else:
                    print "Oops landed on a mine, lives remaining", lives 
                    # 999 is just a random constant added to the cost to pull down the 
                    # path with the mine to have a lower preference
                    new_cost += 999


            if next.id_no not in cost_so_far or new_cost < cost_so_far[next.id_no]:
                cost_so_far[next.id_no] = new_cost
                priority = new_cost + weight(graph.nodes[goal], graph.nodes[next.id_no])
                queue.put(next.id_no, priority)
                came_from[next.id_no] = current
    
    return came_from, cost_so_far


