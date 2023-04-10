#   PROGRAM 3
#   Authors: Matthew Brown and Andrew Harkins
#   Class: CS 330 - 01
#   Date: April 16th, 2023
#==============================================

import math

UNDEFINED = 0
UNVISITED = 1
OPEN      = 2
CLOSED    = 3

showAstarIterations = False

class Astar:
    def __init__(self) -> None:
        pass

    # Function to find the lowest cost node from a list of open nodes
    def find_lowest(graph, open_nodes):
        """
    Astar.find.lowest(graph, open.nodes) 
        lowest.total   <- min(graph$nodes[open.nodes, TOTAL])                    # Determine lowest total cost of all open nodes
        result.indexes <- which(graph$nodes[open.nodes, TOTAL] == lowest.total)  # Find indexes of all open nodes with lowest total cost
        result         <- open.nodes[min(result.indexes)]                        # Find node number of lowest total cost open node with lowest index
        return(result)
        """
        # Get the total cost of all open nodes
        total_costs = [graph["nodes"][node]["TOTAL"] for node in open_nodes]
        # Determine the lowest total cost of all open nodes
        lowest_total = min(total_costs)
        # Get the indexes of all open nodes with lowest total cost
        result_indexes = [i for i, cost in enumerate(total_costs) if cost == lowest_total]
        # Find the node number of the lowest total cost open node with the lowest index
        result = min([open_nodes[i] for i in result_indexes])
        return result

    # Function to calculate the heuristic distance between two nodes
    def heuristic(graph, node1, node2):
        """
        Astar.heuristic(graph, node.1, node.2)
        distance <- sqrt((graph$nodes[node.2, LOC.X] - graph$nodes[node.1, LOC.X])^2 +
                (graph$nodes[node.2, LOC.Z] - graph$nodes[node.1, LOC.Z])^2)
        return(distance)
        """
        # Calculate the distance between the two nodes using their coordinates
        distance = math.sqrt((graph["nodes"][node2]["LOC.X"] - graph["nodes"][node1]["LOC.X"])**2 +
                        (graph["nodes"][node2]["LOC.Z"] - graph["nodes"][node1]["LOC.Z"])**2)
        return distance

    # Function to get the connections for a given node
    def get_connections(graph, current_node):
        """
        Astar.get.connections(graph, current.node)
        result <- which(graph$connections[, FROM.NODE] == current.node)
        return(result)
        """
        # Get the indexes of all connections where the current node is the source node
        result = [i for i, x in enumerate(graph["connections"][:, 0]) if x == current_node]
        return result


    # Function to convert a number to a string of a specified width with leading zeros
    def num_width(num, width, fill):
        return str(num).rjust(width, str(fill))     
    
    # Function to display the status of the algorithm at a given iteration
    def show_iteration_status(graph, iteration, current):
        """
    Astar.show.iteration.status(graph, iteration, current=NULL)
        fill.symbols <- c(".", "O", "X")
        fill.display <- rep("?", graph$n)
        fill.display[1:graph$n] <- fill.symbols[graph$nodes[1:graph$n, STATUS]]
        if (!is.null(current)) { fill.display[current] <- "C" }

        write.text(trace.file, paste(
            "    ",   num.width(iteration, 2, 0),
            "     ",  num.width(length(which(graph$node[, STATUS] == UNVISITED)), 2, 0),
            "     ",  num.width(length(which(graph$node[, STATUS] == OPEN)),      2, 0),
            "     ",  num.width(length(which(graph$node[, STATUS] == CLOSED)),    2, 0), 
            "     ",  paste(fill.display, collapse=""), sep=""))
        """
        fill_symbols = [".", "O", "X"]
        fill_display = ["?" for i in range(graph["n"])]
        for i in range(graph["n"]):
            fill_display[i] = fill_symbols[graph["nodes"][i]["STATUS"]]
        if current is not None:
            fill_display[current] = "C"
        
        trace_file = open("trace.txt", "a")
        trace_file.write("    " + Astar.num_width(iteration, 2, 0) + 
                        "     " + Astar.num_width(len([node for node in graph["nodes"] if node["STATUS"] == UNVISITED]), 2, 0) + 
                        "     " + Astar.num_width(len([node for node in graph["nodes"] if node["STATUS"] == OPEN]), 2, 0) + 
                        "     " + Astar.num_width(len([node for node in graph["nodes"] if node["STATUS"] == CLOSED]), 2, 0) + 
                        "     " + "".join(fill_display) + "\n")
        trace_file.close()

         

    def find_path(graph, first, last):
        """
    Astar.find.path(graph, first, last)
        if (showAstarIterations == TRUE) {
            write.text(trace.file, paste("\n", "A* from ", first, " to ", last, sep=""))
            write.text(trace.file, paste("  itera  unvis   open  closed"))
        }
        """ 
        if showAstarIterations:
            trace_file = open("trace.txt", "a")
            trace_file.write("\nA* from " + str(first) + " to " + str(last) + "\n")
            trace_file.write("  itera  unvis   open  closed\n")
            trace_file.close()      