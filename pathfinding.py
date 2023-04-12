#   PROGRAM 3
#   Authors: Matthew Brown and Andrew Harkins
#   Class: CS 330 - 01
#   Date: April 16th, 2023
#==============================================

import math
from graph import Node
from graph import Connection
from graph import Graph

UNDEFINED = 0
UNVISITED = 1
OPEN      = 2
CLOSED    = 3

class Astar:
    def __init__(self) -> None:
        pass

    # Function to find the lowest cost node from a list of open nodes
    def find_lowest(graph, open_nodes):
        #     """
        # Astar.find.lowest(graph, open.nodes) 
        #     lowest.total   <- min(graph$nodes[open.nodes, TOTAL])                    # Determine lowest total cost of all open nodes
        #     result.indexes <- which(graph$nodes[open.nodes, TOTAL] == lowest.total)  # Find indexes of all open nodes with lowest total cost
        #     result         <- open.nodes[min(result.indexes)]                        # Find node number of lowest total cost open node with lowest index
        #     return(result)
        #     """

        # Get the total cost of all open nodes
        total_costs = [graph.nodes[node].total for node in open_nodes]
        # Determine the lowest total cost of all open nodes
        lowest_total = min(total_costs)
        # Get the indexes of all open nodes with lowest total cost
        result_indexes = [i for i, cost in enumerate(total_costs) if cost == lowest_total]
        # Find the node number of the lowest total cost open node with the lowest index
        result = min([open_nodes[i] for i in result_indexes])
        return result

    # Function to calculate the heuristic distance between two nodes
    def heuristic(graph, node1, node2):
        # """
        # Astar.heuristic(graph, node.1, node.2)
        # distance <- sqrt((graph$nodes[node.2, LOC.X] - graph$nodes[node.1, LOC.X])^2 +
        #         (graph$nodes[node.2, LOC.Z] - graph$nodes[node.1, LOC.Z])^2)
        # return(distance)
        # """

        # Calculate the distance between the two nodes using their coordinates
        distance = math.sqrt((graph.nodes[node2].x - graph.nodes[node1].x)**2 + (graph.nodes[node2].z - graph.nodes[node1].z)**2)
        return distance

    # Function to get the connections for a given node
    def get_connections(graph, current_node):

        # Get the indexes of all connections where the current node is the source node
        result = []
        for i in graph.connections:
            if i.from_node == current_node:
                result.append(i.from_node)
                
        return result


    # Function to convert a number to a string of a specified width with leading zeros
    def num_width(num, width, fill):
        return str(num).rjust(width, str(fill))     
    
    # Function to display the status of the algorithm at a given iteration
    def show_iteration_status(graph, iteration, current):
        fill_symbols = [".", "O", "X"]
        fill_display = ["?"] * len(graph.nodes)
        for i in range(len(graph.nodes)):
            fill_display[i] = fill_symbols[graph.nodes[i].status - 1]
        if current is not None:
            fill_display[current] = "C"
        
        with open("trace.txt", "a") as trace_file:
            trace_file.write("    " + Astar.num_width(iteration, 2, 0) + 
                            "     " + Astar.num_width(len([node for node in graph.nodes if node.status == UNVISITED]), 2, 0) + 
                            "     " + Astar.num_width(len([node for node in graph.nodes if node.status == OPEN]), 2, 0) + 
                            "     " + Astar.num_width(len([node for node in graph.nodes if node.status == CLOSED]), 2, 0) + 
                            "     " + "".join(fill_display) + "\n")

         

    def find_path(graph, first : int, last : int):
        firstIndex = first - 1
        lastIndex = last - 1
       
        with open("trace.txt", "a") as trace_file:
            trace_file.write("\nA* from " + str(first) + " to " + str(last) + "\n")
            trace_file.write("  itera  unvis   open  closed\n")

        for n in graph.nodes:
            n.status = UNVISITED
            n.cost_so_far = float('inf')
            n.previous_node = UNDEFINED

        openNodes = []

        graph.nodes[firstIndex].status = OPEN
        graph.nodes[firstIndex].cost_so_far = 0
        iteration = 0
        openNodes.append(firstIndex)

        Astar.show_iteration_status(graph, iteration, 0)
        lengthOpenNodes = len(openNodes)
        while lengthOpenNodes > 0:
            iteration = iteration + 1

            currentNode = Astar.find_lowest(graph, openNodes)
            if currentNode == lastIndex:
                Astar.show_iteration_status(graph, iteration)
                break

            currentCon = []
            currentCon = Astar.get_connections(graph, currentNode)

            for con in currentCon:

                toNode = graph.connections[con].to_node
                toCost = graph.nodes[currentNode].cost_so_far + graph.connections[con].cost

                if toCost < graph.nodes[toNode].cost_so_far:
                    graph.nodes[toNode].status = OPEN
                    graph.nodes[toNode].cost_so_far = toCost
                    graph.nodes[toNode].heuristic = Astar.heuristic(graph, toNode, lastIndex)
                    graph.nodes[toNode].total = graph.nodes[toNode].cost_so_far + graph.nodes[toNode].heuristic
                    graph.nodes[toNode].previous_node = currentNode
                    openNodes.append(toNode)
            
            Astar.show_iteration_status(graph, iteration, currentNode)

            graph.nodes[currentNode].status = CLOSED                  # Close current node.
            openNodes = openNodes.remove(currentNode)              # Remove current node from open list.
            print(openNodes)


            lengthOpenNodes = len(openNodes)

        return graph






        
