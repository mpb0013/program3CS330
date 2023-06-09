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

class Astar():
    def __init__(self) -> None:
        pass

    # Function to find the lowest cost node from a list of open nodes
    def find_lowest(graph, open_nodes):

        # Get the total cost of all open nodes
        total_costs = []
        for i in open_nodes:
            total_costs.append(graph.nodes[i].total)

        # Determine the lowest total cost of all open nodes
        lowest_total = min(total_costs)

        # Get the indexes of all open nodes with lowest total cost
        result_indexes = []
        for i in open_nodes:
            if lowest_total == graph.nodes[i].total:
                result_indexes.append(i)

        # Find the node number of the lowest total cost open node with the lowest index
        result = min(result_indexes)
        
        return result

    # Function to calculate the heuristic distance between two nodes
    def heuristic(graph, node1, node2):

        # Calculate the distance between the two nodes using their coordinates
        distance = math.sqrt((graph.nodes[node2].x - graph.nodes[node1].x)**2 + (graph.nodes[node2].z - graph.nodes[node1].z)**2)
        return distance

    # Function to get the connections for a given node
    def get_connections(graph, currentNode):
        # Get the indexes of all connections where the current node is the source node
        result = []
        for i in graph.connections:
            if i.from_node == currentNode:
                result.append(i)
                
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
        #set the desired nodes to their indexes
        firstIndex = first - 1
        lastIndex = last - 1

        #If it's the first time write to the file to clear it otherwise add to the current file
        if graph.firstTime:
            fileOp = "w"
            graph.firstTime = False
        else:
            fileOp = "a"

        #Write header into file
        with open("trace.txt", fileOp) as trace_file:
            trace_file.write("\nA* from " + str(first) + " to " + str(last) + "\n")
            trace_file.write("  itera  unvis   open  closed\n")

        #Reset all the nodes
        for n in graph.nodes:
            n.status = UNVISITED
            n.cost_so_far = float('inf')
            n.previous_node = UNDEFINED

        #create the openNodes Array
        openNodes = []

        #open the starting node and put into openNodes
        graph.nodes[firstIndex].status = OPEN
        graph.nodes[firstIndex].cost_so_far = 0
        iteration = 0
        openNodes.append(firstIndex)

        #print out status info to file
        Astar.show_iteration_status(graph, iteration, 0)
        
        #While there are openNodes keep finding connections
        while type(openNodes) != None:
            iteration = iteration + 1

            #find the lowest cost and lowest index node and set to current
            currentNode = Astar.find_lowest(graph, openNodes)

            #if the currentNode is the last one then break
            if currentNode == lastIndex:
                Astar.show_iteration_status(graph, iteration, 0)
                break

            #create current connection list
            currentCon = []
            #get connections of currentNode
            currentCon = Astar.get_connections(graph, currentNode + 1)

            #check each connection
            for con in currentCon:

                #find the connected next Node
                #and get cost to that node
                toNode = con.to_node - 1
                toCost = graph.nodes[currentNode].cost_so_far + con.cost

                #check the cost to the cost so far
                if toCost < graph.nodes[toNode].cost_so_far:
                    #open that node
                    graph.nodes[toNode].status = OPEN
                    #update its cost so far
                    graph.nodes[toNode].cost_so_far = toCost
                    #calculate the heuristic to end goal
                    graph.nodes[toNode].heuristic = Astar.heuristic(graph, toNode, lastIndex)
                    #add the heursitic and cost so far into node total
                    graph.nodes[toNode].total = graph.nodes[toNode].cost_so_far + graph.nodes[toNode].heuristic
                    #set the previous node of opened node to currentNode so we can retrieve the path
                    graph.nodes[toNode].previous_node = currentNode
                    #add the new Node to openNodes list
                    openNodes.append(toNode)
            
            #print currentNode to file
            Astar.show_iteration_status(graph, iteration, currentNode)

            #close currentNode and remove it
            graph.nodes[currentNode].status = CLOSED                  # Close current node.
            openNodes.remove(currentNode)              # Remove current node from open list.

        return graph

    #Function to retrieve the Path that was found by backtracking through the nodes
    def retrievePath(graph, first, last):
        #create finalPath array
        finalPath = []
        
        #set currentNode we are looking at to the last
        currentNode = last
        fail = 100
        
        #Starting at last node, append the currentNode to finalPath and then set previous node to current
        while currentNode != first and fail > 0:
            fail = fail - 1
            finalPath.append(currentNode)
            currentNode = graph.nodes[graph.nodes[currentNode - 1].previous_node].node_num
        
        #append the lastNode
        finalPath.append(first)
        #reverse the path
        finalPath.reverse()

        with open("output.txt", "a") as trace_file:
            #print out path and path cost to file
            trace_file.write("\n---------------------\n")
            trace_file.write("Path from " + str(first) + " to " + str(last) + "\n")
            trace_file.write("Path "  + str(finalPath) + "\n")
            trace_file.write("Cost = " + str(graph.nodes[last - 1].cost_so_far) + "\n")
            trace_file.write("---------------------\n")

        return finalPath






        
