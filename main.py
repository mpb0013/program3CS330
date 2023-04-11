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

g = Graph()
g.buildGraph('CS 330, Pathfinding, Graph AB Nodes v3.txt', 'CS 330, Pathfinding, Graph AB Connections v3.txt')
#g.printGraph()
Astar.find_path(g, 1, 29)