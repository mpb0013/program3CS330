#   PROGRAM 3
#   Authors: Matthew Brown and Andrew Harkins
#   Class: CS 330 - 01
#   Date: April 16th, 2023
#==============================================

# Import necessary classes and functions from the support module
from pathfinding import Astar
from graph import Node
from graph import Connection
from graph import Graph

#build the graph
g = Graph()
g.buildGraph('CS 330, Pathfinding, Graph AB Nodes v3.txt', 'CS 330, Pathfinding, Graph AB Connections v3.txt')

with open("output.txt", "w") as fp:
    g.printGraph(fp)

#Calculate Each path using Astar Algorithm
Astar.find_path(g, 1, 29)
Astar.retrievePath(g, 1, 29)

Astar.find_path(g, 1, 38)
Astar.retrievePath(g, 1, 38)

Astar.find_path(g, 11, 1)
Astar.retrievePath(g, 11, 1)

Astar.find_path(g, 33, 66)
Astar.retrievePath(g, 33, 66)
                   
Astar.find_path(g, 58, 43)
Astar.retrievePath(g, 58, 43)